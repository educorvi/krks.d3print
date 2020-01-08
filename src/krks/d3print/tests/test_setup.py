# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from krks.d3print.testing import KRKS_D3PRINT_INTEGRATION_TESTING  # noqa: E501
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that krks.d3print is properly installed."""

    layer = KRKS_D3PRINT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if krks.d3print is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'krks.d3print'))

    def test_browserlayer(self):
        """Test that IKrksD3PrintLayer is registered."""
        from krks.d3print.interfaces import (
            IKrksD3PrintLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IKrksD3PrintLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = KRKS_D3PRINT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['krks.d3print'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if krks.d3print is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'krks.d3print'))

    def test_browserlayer_removed(self):
        """Test that IKrksD3PrintLayer is removed."""
        from krks.d3print.interfaces import \
            IKrksD3PrintLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IKrksD3PrintLayer,
            utils.registered_layers())
