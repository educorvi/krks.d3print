# -*- coding: utf-8 -*-

from Products.Five.browser import BrowserView
import requests
from plone import api


class UploadView(BrowserView):

    def __call__(self):

        blob = self.context.printmodell
        #ploneio = stream_data(blob)
        #myio = open(ploneio.name, 'rb')
        #myio = io.BytesIO(blob.data)
        temppath = '/tmp/%s' %blob.filename
        tempfile = open(temppath, 'wb')
        tempfile.write(blob.data)
        tempfile.close()
        myio = open(temppath, 'rb')
        #filename = 'max.gcode'
        #import pdb;pdb.set_trace()
        filename = blob.filename
        fle = {'file':myio, 'filename':filename}

        printer = api.content.get(UID=self.context.drucker)

        # printer.ipaddresse (+ Port)

        #Informationen muessen aus Printer-Objekt bezogen werden
        url='http://192.168.86.56:5001/api/files/{}'.format('local')
        #URL?
        payload={'select': 'true','print': 'true' }
        header={'X-Api-Key': '02AC33DA679D4A93BA6BF9EAB1CF01CC' }
        response = requests.post(url, files=fle,data=payload,headers=header)
        print(response)

        url = printer.absolute_url()+'/druckerview'
        
        return self.request.response.redirect(url)
