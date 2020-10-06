# -*- coding: utf-8 -*-

from Products.Five.browser import BrowserView
import requests
from plone import api

import tempfile


class UploadView(BrowserView):

    def __call__(self):

        blob = self.context.printmodell
        temppath = '/tmp/%s' %blob.filename
        tempfile = open(temppath, 'wb')
        tempfile.write(blob.data)
        tempfile.close()

#        tempfile = tempfile.TemporaryFile()
#        tempfile.write(blob.data)

        myio = open(temppath, 'rb')
        filename = blob.filename

#        tempfile.seek(0)
#        rudi = tempfile.seek(0)
#        myio = rudi.decode('ascii')

        fle = {'file':myio, 'filename':filename}

        printer = api.content.get(UID=self.context.drucker)

        url='http://'+printer.ipaddresse+':'+printer.port+'/api/files/{}'.format('local')
        payload={'select': 'true','print': 'true' }
        header={'X-Api-Key': printer.apikey}
        response = requests.post(url, files=fle,data=payload,headers=header)
        print(response)

        url = printer.absolute_url()+'/drucker-view'
        
        return self.request.response.redirect(url)
