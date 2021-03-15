import collections

from pyramid.config import Configurator

from clld_glottologfamily_plugin import util

from clld.interfaces import IMapMarker, IValueSet, IValue, IDomainElement
from clldutils.svg import pie, icon, data_url

# we must make sure custom models are known at database initialization!
from jambu import models
import hashlib

sha = hashlib.sha256()

cognates = []

class LanguageByFamilyMapMarker(util.LanguageByFamilyMapMarker):
    def __call__(self, ctx, req):
        
        mapping = {}
        count = -1
        if IValueSet.providedBy(ctx):
            c = ctx.values[0].cognateset
            while len(cognates) <= c:
                sha.update('aa'.encode())
                cognates.append(sha.hexdigest()[:6])
            return data_url(icon('c' + cognates[c]))
    
        return super(LanguageByFamilyMapMarker, self).__call__(ctx, req)



def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('clld.web.app')

    config.registry.registerUtility(LanguageByFamilyMapMarker(), IMapMarker)

    return config.make_wsgi_app()
