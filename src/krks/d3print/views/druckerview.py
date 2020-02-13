# -*- coding: utf-8 -*-
import requests
from time import sleep
from krks.d3print import _
from Products.Five.browser import BrowserView

from requests.exceptions import Timeout
from plone import api

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class Druckerview(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('druckerview.pt')

    def __call__(self):
        print("Call me maybe")
        self.msg = _(u'A small message')
        self.mygcodes = self.get_gcodes()
        try:
            response = requests.get('http://'+self.context.ipaddresse+':'+self.context.port, timeout=1)
        except Timeout:
            print('The request timed out')
            return self.request.response.redirect(self.context.absolute_url()+'/error-view')
        return self.index()

    def get_gcodes(self):
        mygcodes = []
        all_gcodes = api.content.find(portal_type="GCode Datei")
        for i in all_gcodes:
            obj = i.getObject()
            if obj.drucker == self.context.UID():
                mygcodes.append(obj)
        print(mygcodes)
        return mygcodes


    # Preparing get_bilder
    
#    def get_bilder(self):
#        bilder = self.context.ListFolderContents(
#                contentFilter = {portal_type="Image"}
#                )

# Begin Header definition section
    def post_headers(self):
        host = self.context.ipaddresse+':'+self.context.port
        post_headers = {
            'Host': self.context.ipaddresse+':'+self.context.port,
            'X-Api-Key': self.context.apikey,  # Aus Content-Objekt
            'Content-Type': 'application/json'  # konstant
            }
        return post_headers
    
    def get_headers(self):
        host = self.context.ipaddresse+':'+self.context.port
        get_headers = {
            'Host': self.context.ipaddresse+':'+self.context.port,
            'X-Api-Key': self.context.apikey,  # Aus Content-Objekt
            }
        return get_headers

    def connect_json(self):
        host = self.context.ipaddresse+':'+self.context.port
        baudrate_context = self.context.baudrate
        connect_json = {
            'command': 'connect',
            'port': '/dev/ttyUSB0',  # Aus Content-Objekt (Drop-Down)
            'baudrate': baudrate_context,  # Aus Content-Objekt (Drop-Down)
            'printerProfile': '_default',
            'save': 'true',
            'autoconnect': 'true'
        }
        return connect_json
# End Headers definition section


    def aktualisieren(self):
        url = self.context.absolute_url() + '/druckerview'
        return url

    def haupttext(self):
        haupttext = self.context.haupttext
        return haupttext

    def druckerbild(self):
        druckerbild = self.context.druckerbild
        return druckerbild

    def connect_printer(self):

        ipaddresse = self.context.ipaddresse+':'+self.context.port
        httpip = ('http://'+ipaddresse)

        apicall_job = httpip+'/api/job'
        apicall_connection = httpip+'/api/connection'
        apicall_printer = httpip+'/api/printer'

        tooltemp = 'k.A'
        bedtemp = 'k.A'
        tooltemp_target = 'k.A.'
        bedtemp_target = 'k.A.'
        state = 'k.A.'

        print(u'Seppo ist klug')

        print('The request did not time out')

        jobstateresult = requests.get(apicall_job, headers=self.get_headers(), timeout=2)
        jobstatedict = jobstateresult.json()
        if jobstateresult:
            jobstatezwischenergebnis1 = jobstatedict.get("job")
            if jobstatezwischenergebnis1:
                jobname = jobstatezwischenergebnis1['file']['name']

            jobstatezwischenergebnis2 = jobstatedict.get("progress")
            if jobstatezwischenergebnis2:
                remainingtime = jobstatezwischenergebnis2['printTimeLeft']

        print(jobname)
        print(remainingtime)

        remainingtime = "ca. " + str(remainingtime) + " Sekunden verbleibend"

        if jobname == None:
            jobname = "Kein Druckauftrag"
            remainingtime = "Kein Druckauftrag"

        connectionresult = requests.get(apicall_connection, headers=self.get_headers(), timeout=2)
        connectiondict = connectionresult.json()
        if connectiondict:
            result1 = connectiondict.get("current")
            if result1:
                state = result1['state']

        if state == "Operational" or state == "Printing":

            data = requests.get(apicall_printer, headers=self.get_headers())
            datadict = data.json()

            if datadict:
                temp = datadict.get("temperature")
                if temp:
                    tooltemp = temp['tool0']['actual']
                    bedtemp = temp['bed']['actual']
                    tooltemp_target = temp['tool0']['target']
                    bedtemp_target = temp['bed']['target']
                #return {'tooltemp': tooltemp, 'bedtemp': bedtemp, 'tooltemp_target': tooltemp_target,'bedtemp_target': bedtemp_target, 'state': state, 'jobname': jobname, 'remainingtime': remainingtime}


        else:

            result = requests.post(apicall_connection, headers=self.post_headers(), json=self.connect_json())
            print(result.status_code)
            if result.status_code == 204:
                sleep(5)
                data = requests.get(apicall_printer, headers=self.get_headers())
                datadict = data.json()

                if datadict:
                    temp = datadict.get("temperature")
                    if temp:
                        tooltemp = temp['tool0']['actual']
                        bedtemp = temp['bed']['actual']
                        tooltemp_target = temp['tool0']['target']
                        bedtemp_target = temp['bed']['target']

                connectionresult = requests.get(httpip+'/api/connection', headers=self.get_headers())
                connectiondict = connectionresult.json()
                if connectiondict:
                    result1 = connectiondict.get("current")
                    if result1:
                        state = result1['state']

            else:
                print("Error")

        return {'tooltemp': tooltemp, 'bedtemp': bedtemp, 'tooltemp_target': tooltemp_target, 'bedtemp_target': bedtemp_target, 'state': state, 'jobname': jobname, 'remainingtime': remainingtime}
