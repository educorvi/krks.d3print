# -*- coding: utf-8 -*-

from krks.d3print import _
from Products.Five.browser import BrowserView

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class PrintView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('print_view.pt')

    def printmodell(self):
        printmodell = self.context.printmodell
        return printmodell

    def vorschaubild(self):
        vorschaubild = self.context.vorschaubild
        return vorschaubild

    def pdfdoku(self):
        pdfdoku = self.context.pdfdoku
        return pdfdoku
