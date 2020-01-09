# -*- coding: utf-8 -*-
from krks.d3print.content.druckobjekt import IDruckobjekt  # NOQA E501
from krks.d3print.testing import KRKS_D3PRINT_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class DruckobjektIntegrationTest(unittest.TestCase):

    layer = KRKS_D3PRINT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_druckobjekt_schema(self):
        fti = queryUtility(IDexterityFTI, name='Druckobjekt')
        schema = fti.lookupSchema()
        self.assertEqual(IDruckobjekt, schema)

    def test_ct_druckobjekt_fti(self):
        fti = queryUtility(IDexterityFTI, name='Druckobjekt')
        self.assertTrue(fti)

    def test_ct_druckobjekt_factory(self):
        fti = queryUtility(IDexterityFTI, name='Druckobjekt')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IDruckobjekt.providedBy(obj),
            u'IDruckobjekt not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_druckobjekt_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Druckobjekt',
            id='druckobjekt',
        )

        self.assertTrue(
            IDruckobjekt.providedBy(obj),
            u'IDruckobjekt not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('druckobjekt', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('druckobjekt', parent.objectIds())

    def test_ct_druckobjekt_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Druckobjekt')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_druckobjekt_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Druckobjekt')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'druckobjekt_id',
            title='Druckobjekt container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
