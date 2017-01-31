# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from brainelechateau.urban.dataimport.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of brainelechateau.urban.dataimport into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if brainelechateau.urban.dataimport is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('brainelechateau.urban.dataimport'))

    def test_uninstall(self):
        """Test if brainelechateau.urban.dataimport is cleanly uninstalled."""
        self.installer.uninstallProducts(['brainelechateau.urban.dataimport'])
        self.assertFalse(self.installer.isProductInstalled('brainelechateau.urban.dataimport'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IBrainelechateauUrbanDataimportLayer is registered."""
        from brainelechateau.urban.dataimport.interfaces import IBrainelechateauUrbanDataimportLayer
        from plone.browserlayer import utils
        self.failUnless(IBrainelechateauUrbanDataimportLayer in utils.registered_layers())
