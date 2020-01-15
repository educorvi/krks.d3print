# -*- coding: utf-8 -*-

from krks.d3print import _
from Products.Five.browser import BrowserView
from plone.namedfile.utils import stream_data
import io
from plone import api

import requests

from krks.d3print.vocabularies import get_printers 

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class PrintView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('print_view.pt')

    def printmodell(self):
        printmodell = self.context.printmodell
        return printmodell


    def get_files(self):
        templatelist=[]
        filelist = self.context.getFolderContents()
        for i in filelist:
            druckdatei={}
            druckdatei['url']=i.getURL() + '/upload_view'
            druckdatei['title']=i.Title
            obj = i.getObject()
            drucker = obj.drucker
            druckdatei['druckername'] = get_printers(self.context).getTerm(drucker).title
            templatelist.append(druckdatei)

        return(templatelist)
            


    def vorschaubild(self):
        vorschaubild = self.context.vorschaubild
        return vorschaubild

    def pdfdoku(self):
        pdfdoku = self.context.pdfdoku
        return pdfdoku
