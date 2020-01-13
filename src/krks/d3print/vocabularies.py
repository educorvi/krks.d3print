from zope.interface import provider
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary
from plone import api

@provider(IContextSourceBinder)
def get_printers(context):
    terms = []
    printers = api.content.find(portal_typ="Drucker")
    for i in printers:
        terms.append(SimpleVocabulary.createTerm(i.UID,i.UID,i.Title))
    return SimpleVocabulary(terms)
