# -*- coding: utf-8 -*-
from krks.d3print.content.printer import IPrinter  # NOQA E501
from krks.d3print.testing import KRKS_D3PRINT_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class PrinterIntegrationTest(unittest.TestCase):

    layer = KRKS_D3PRINT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_printer_schema(self):
        fti = queryUtility(IDexterityFTI, name='printer')
        schema = fti.lookupSchema()
        self.assertEqual(IPrinter, schema)

    def test_ct_printer_fti(self):
        fti = queryUtility(IDexterityFTI, name='printer')
        self.assertTrue(fti)

    def test_ct_printer_factory(self):
        fti = queryUtility(IDexterityFTI, name='printer')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IPrinter.providedBy(obj),
            u'IPrinter not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_printer_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='printer',
            id='printer',
        )

        self.assertTrue(
            IPrinter.providedBy(obj),
            u'IPrinter not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('printer', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('printer', parent.objectIds())

    def test_ct_printer_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='printer')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_printer_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='printer')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'printer_id',
            title='printer container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
