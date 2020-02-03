# -*- coding: utf-8 -*-

from krks.d3print import _
from Products.Five.browser import BrowserView

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class ErrorView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('error_view.pt')

    def __call__(self):
        import pdb;pdb.set_trace()
        # Implement your own actions:
        self.msg = _(u'A small message')
        return self.index()
