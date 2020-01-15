# -*- coding: utf-8 -*-
# from plone.app.textfield import RichText
# from plone.autoform import directives
from plone.dexterity.content import Item
# from plone.namedfile import field as namedfile
from plone.supermodel import model
# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer

from krks.d3print.vocabularies import get_printers

from krks.d3print import _

from plone.namedfile.field import NamedBlobFile

class IGCodeDatei(model.Schema):
    """ Marker interface and Dexterity Python Schema for GCodeDatei
    """
    printmodell = NamedBlobFile(title="Druckdatei hochladen")

    drucker = schema.Choice(
        title=_(u'Auswahl des Druckers'),
        source=get_printers,
        required=True
    )

@implementer(IGCodeDatei)
class GCodeDatei(Item):
    """
    """
