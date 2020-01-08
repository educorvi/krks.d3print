# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import krks.d3print


class KrksD3PrintLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=krks.d3print)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'krks.d3print:default')


KRKS_D3PRINT_FIXTURE = KrksD3PrintLayer()


KRKS_D3PRINT_INTEGRATION_TESTING = IntegrationTesting(
    bases=(KRKS_D3PRINT_FIXTURE,),
    name='KrksD3PrintLayer:IntegrationTesting',
)


KRKS_D3PRINT_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(KRKS_D3PRINT_FIXTURE,),
    name='KrksD3PrintLayer:FunctionalTesting',
)


KRKS_D3PRINT_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        KRKS_D3PRINT_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='KrksD3PrintLayer:AcceptanceTesting',
)
