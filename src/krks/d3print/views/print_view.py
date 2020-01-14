# -*- coding: utf-8 -*-

from krks.d3print import _
from Products.Five.browser import BrowserView
from plone.namedfile.utils import stream_data
import io

import requests

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class PrintView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('print_view.pt')

    def printmodell(self):
        printmodell = self.context.printmodell
        return printmodell

    def get_file(self):
        blob = self.context.printmodell
        ploneio = stream_data(blob)
        #myio = open(ploneio.name, 'rb')
        #myio = io.BytesIO(blob.data)
        temppath = '/tmp/%s' %blob.filename
        tempfile = open(temppath, 'wb')
        tempfile.write(blob.data)
        tempfile.close()
        myio = open(temppath, 'rb')
        filename = 'max.gcode'
        import pdb;pdb.set_trace()
        #filename = blob.filename
        fle = {'file':myio, 'filename':filename}

        url='http://192.168.86.56:5001/api/files/{}'.format('local')
        payload={'select': 'true','print': 'false' }
        header={'X-Api-Key': '02AC33DA679D4A93BA6BF9EAB1CF01CC' }
        response = requests.post(url, files=fle,data=payload,headers=header)
        print(response)


    def vorschaubild(self):
        vorschaubild = self.context.vorschaubild
        return vorschaubild

    def pdfdoku(self):
        pdfdoku = self.context.pdfdoku
        return pdfdoku
