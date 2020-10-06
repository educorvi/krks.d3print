# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
# from plone.autoform import directives
from plone.dexterity.content import Container
# from plone.namedfile import field as namedfile
from plone.supermodel import model
# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer

from zope.interface import Invalid

import requests
from requests.exceptions import Timeout

import os
from plone.namedfile.field import NamedBlobImage
from plone.namedfile.field import NamedBlobFile

from krks.d3print.vocabularies import baudrate_vocabulary

class NotReachable(schema.ValidationError):
    """Diese IP-Adresse ist im Netzwerk leider nicht erreichbar. Bitte vergewissern Sie sich dass krks.d3print angeschlossen und mit dem Netzwerk verbunden ist, und dass Sie die richtige IP-Adresse eingegeben haben."""

def ipaddresse_constraint(ipaddresse):
    hostname = ipaddresse
    response = os.system("ping -c 1 " + hostname)

    if response != 0:
        raise NotReachable
    return True

class IDrucker(model.Schema):
    """ Marker interface and Dexterity Python Schema for Drucker
    """

    ipaddresse = schema.TextLine(title="IP-Adresse", constraint=ipaddresse_constraint)
    port = schema.TextLine(title="Portnummer")
    apikey = schema.TextLine(title="API-Key")
    baudrate = schema.Choice(title="Baudrate",
                             default='AUTO',
                             vocabulary=baudrate_vocabulary)

    #schnittstelle ...??

    druckerbild = NamedBlobImage(
            title="Druckerbild",
            required=False
    ) 
    handbuch = NamedBlobFile(
            title="Handbuch des Druckers",
            required=False 
    )
    haupttext = schema.Text(
            title="Wichtige Hinweise zum Drucker",
            required=False
    )
    # If you want, you can load a xml model created TTW here
    # and customize it in Python:

    # model.load('drucker.xml')

    # directives.widget(level=RadioFieldWidget)
    # level = schema.Choice(
    #     title=_(u'Sponsoring Level'),
    #     vocabulary=LevelVocabulary,
    #     required=True
    # )

    # text = RichText(
    #     title=_(u'Text'),
    #     required=False
    # )

    # url = schema.URI(
    #     title=_(u'Link'),
    #     required=False
    # )

    # fieldset('Images', fields=['logo', 'advertisement'])
    # logo = namedfile.NamedBlobImage(
    #     title=_(u'Logo'),
    #     required=False,
    # )

    # advertisement = namedfile.NamedBlobImage(
    #     title=_(u'Advertisement (Gold-sponsors and above)'),
    #     required=False,
    # )

    # directives.read_permission(notes='cmf.ManagePortal')
    # directives.write_permission(notes='cmf.ManagePortal')
    # notes = RichText(
    #     title=_(u'Secret Notes (only for site-admins)'),
    #     required=False
    # )


@implementer(IDrucker)
class Drucker(Container):
    """
    """
