# -*- coding: utf-8 -*-
from krks.d3print.testing import KRKS_D3PRINT_FUNCTIONAL_TESTING
from krks.d3print.testing import KRKS_D3PRINT_INTEGRATION_TESTING
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from zope.component import getMultiAdapter
from zope.component.interfaces import ComponentLookupError

import unittest


class ViewsIntegrationTest(unittest.TestCase):

    layer = KRKS_D3PRINT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        api.content.create(self.portal, 'Folder', 'other-folder')
        api.content.create(self.portal, 'Document', 'front-page')

    def test_print_view_is_registered(self):
        view = getMultiAdapter(
            (self.portal['other-folder'], self.portal.REQUEST),
            name='print-view'
        )
        self.assertTrue(view.__name__ == 'print-view')
        # self.assertTrue(
        #     'Sample View' in view(),
        #     'Sample View is not found in print-view'
        # )

    def test_print_view_not_matching_interface(self):
        with self.assertRaises(ComponentLookupError):
            getMultiAdapter(
                (self.portal['front-page'], self.portal.REQUEST),
                name='print-view'
            )


class ViewsFunctionalTest(unittest.TestCase):

    layer = KRKS_D3PRINT_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
