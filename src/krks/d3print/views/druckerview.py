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

    def aktualisieren(self):
        url=self.context.absolute_url()+'/druckerview'
        return url

    def connect_printer(self):

        tooltemp = 'k.A'
        bedtemp = 'k.A'
        tooltemp_target = 'k.A.'
        bedtemp_target = 'k.A.'
        
        connectionresult = requests.get('http://192.168.86.56:5001/api/connection', headers=get_headers)
        connectiondict = connectionresult.json()
        if connectiondict:
            result1 = connectiondict.get("current")
            if result1:
                state = result1['state']

        if state == "Operational":
            
            data = requests.get('http://192.168.86.56:5001/api/printer', headers=get_headers)
            datadict = data.json()

            if datadict:
                temp = datadict.get("temperature")
                if temp:
                    tooltemp = temp['tool0']['actual']
                    bedtemp = temp['bed']['actual']
                    tooltemp_target = temp['tool0']['target']
                    bedtemp_target = temp['bed']['target']
                return {'tooltemp':tooltemp, 'bedtemp':bedtemp, 'tooltemp_target':tooltemp_target, 'bedtemp_target':bedtemp_target}
                    

        else:

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
                        tooltemp_target = temp['tool0']['target']
                        bedtemp_target = temp['bed']['target']

            else:
                print("Error")
            return {'tooltemp':tooltemp, 'bedtemp':bedtemp, 'tooltemp_target':tooltemp_target, 'bedtemp_target':bedtemp_target}
