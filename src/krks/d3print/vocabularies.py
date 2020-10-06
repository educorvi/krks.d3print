from zope.interface import provider
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from plone import api

@provider(IContextSourceBinder)
def get_printers(context):
    terms = []
    printers = api.content.find(portal_type="Drucker")
    # import pdb;pdb.set_trace()
    for i in printers:
        terms.append(SimpleVocabulary.createTerm(i.UID,i.UID,i.Title))
    return SimpleVocabulary(terms)


baudrate_vocabulary = SimpleVocabulary((
    SimpleTerm(value=9600, token=9600, title=9600),
    SimpleTerm(value=19200, token=19200, title=19200),
    SimpleTerm(value=38400, token=38400, title=38400),
    SimpleTerm(value=57600, token=57600, title=57600),
    SimpleTerm(value=115200, token=115200, title=115200),
    SimpleTerm(value=250000, token=250000, title=250000),
    SimpleTerm(value=u'AUTO', token=u'AUTO', title=u'AUTO')
    ))
