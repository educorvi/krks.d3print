# -*- coding: utf-8 -*-
from krks.d3print.content.g_code_datei import IGCodeDatei  # NOQA E501
from krks.d3print.testing import KRKS_D3PRINT_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class GCodeDateiIntegrationTest(unittest.TestCase):

    layer = KRKS_D3PRINT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            'Drucker',
            self.portal,
            'parent_container',
            title='Parent container',
        )
        self.parent = self.portal[parent_id]

    def test_ct_g_code_datei_schema(self):
        fti = queryUtility(IDexterityFTI, name='GCode Datei')
        schema = fti.lookupSchema()
        self.assertEqual(IGCodeDatei, schema)

    def test_ct_g_code_datei_fti(self):
        fti = queryUtility(IDexterityFTI, name='GCode Datei')
        self.assertTrue(fti)

    def test_ct_g_code_datei_factory(self):
        fti = queryUtility(IDexterityFTI, name='GCode Datei')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IGCodeDatei.providedBy(obj),
            u'IGCodeDatei not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_g_code_datei_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='GCode Datei',
            id='g_code_datei',
        )

        self.assertTrue(
            IGCodeDatei.providedBy(obj),
            u'IGCodeDatei not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('g_code_datei', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('g_code_datei', parent.objectIds())

    def test_ct_g_code_datei_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='GCode Datei')
        self.assertFalse(
            fti.global_allow,
            u'{0} is globally addable!'.format(fti.id)
        )
