# -*- coding: utf-8 -*-
import requests
from time import sleep
from krks.d3print import _
from Products.Five.browser import BrowserView

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

post_headers={
    'Host': '192.168.86.56:5001', #Aus Content-Objekt
    'X-Api-Key': '02AC33DA679D4A93BA6BF9EAB1CF01CC', #Aus Content-Objekt
    'Content-Type': 'application/json' #konstant
    }

get_headers={
    'Host': '192.168.86.56:5001', #Aus Content-Objekt
    'X-Api-Key': '02AC33DA679D4A93BA6BF9EAB1CF01CC' #Aus Content-Objekt
    }

connect_json={
    'command': 'connect',
    'port': '/dev/ttyUSB0', #Aus Content-Objekt (Drop-Down)
    'baudrate': 250000, #Aus Content-Objekt (Drop-Down)
    'printerProfile': '_default',
    'save': 'true',
    'autoconnect': 'true'
    }

class Druckerview(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('druckerview.pt')

    def __call__(self):
        # Implement your own actions:
        self.msg = _(u'A small message')
        return self.index()

    def connect_printer(self):

        tooltemp = 'k.A'
        bedtemp = 'k.A'

        result = requests.post('http://192.168.86.56:5001/api/connection', headers=post_headers, json=connect_json)
        print(result.status_code)
        if result.status_code == 204:
            sleep(5)
            data = requests.get('http://192.168.86.56:5001/api/printer', headers=get_headers)
            datadict = data.json()

            if datadict:
                temp = datadict.get("temperature")
                if temp:
                    tooltemp = temp['tool0']['actual']
                    bedtemp = temp['bed']['actual']

        else:
            print("Error")
        return {'tooltemp':tooltemp, 'bedtemp':bedtemp}
