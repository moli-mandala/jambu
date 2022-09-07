import collections

from pyramid.config import Configurator

from clld_glottologfamily_plugin import util

from clld.interfaces import IMapMarker, IValueSet, IValue, IDomainElement, ILanguage
from clldutils.svg import pie, icon, data_url

# we must make sure custom models are known at database initialization!
from jambu import models
import hashlib

sha = hashlib.sha256()

colors = {
    "Dardic": "0000FF",
    "Western Pahari": "00FFFF",
    "Central Pahari": "6F8FAF",
    "Eastern Pahari": "1434A4",
    "Lahndic": "00A36C",
    "Punjabic": "008080",
    "Sindhic": "A52A2A",
    "Gujaratic": "F0E68C",
    "Rajasthanic": "808000",
    "Marathi-Konkani": "FFAC1C",
    "Insular": "CC5500",
    "Eastern": "FF00FF",
    "Bihari": "FFC0CB",
    "Eastern Hindi": "5D3FD3",
    "Western Hindi": "51414F",
    "Migratory": "722F37",
    "MIA": "FFDEAD",
    "OIA": "E2DFD2",
    "non-IA": "FAF9F6",
    "Nuristani": "FF10F0",
    "Bhil": "93C572",
    "Halbic": "FF568E",
    "Brahui": "49796B",
    "South Dravidian I": "74C365",
    "South Dravidian II": "98FB98",
    "Central Dravidian": "29AB87",
    "North Dravidian": "4B6F44",
    "Old Dravidian": "#679267"
}

cognates = []

# class CoblMapMarker(MapMarker):
#     def __call__(self, ctx, req):
#         color, shape = None, 'c'
#         if IValueSet.providedBy(ctx):
#             v = ctx.values[0]
#             if v.cognates:
#                 color = v.cognates[0].cognateset.color
#             else:
#                 color = '#fff'
#             if ctx.language.historical:
#                 shape = 'd'

#         if ILanguage.providedBy(ctx):
#             color = ctx.color
#             if ctx.historical:
#                 shape = 'd'

#         if color:
#             if color.startswith('#'):
#                 color = color[1:]
#             return svg.data_url(svg.icon(shape + color))

#         return super(CoblMapMarker, self).__call__(ctx, req)

class LanguageByFamilyMapMarker(util.LanguageByFamilyMapMarker):
    def __call__(self, ctx, req):
        
        mapping = {}
        count = -1
        shape = 'c'
        if IValueSet.providedBy(ctx):
            c = colors[ctx.language.family]
            if ctx.language.family in ['MIA', 'OIA'] or 'Old' in ctx.language.name or 'Proto' in ctx.language.name:
                shape = 'd'
            return data_url(icon(shape + c))

        if ILanguage.providedBy(ctx):
            c = colors[ctx.family]
            if ctx.family in ['MIA', 'OIA'] or 'Old' in ctx.name or 'Proto' in ctx.name:
                shape = 'd'
            return data_url(icon(shape + c))
    
        return super(LanguageByFamilyMapMarker, self).__call__(ctx, req)



def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('clld.web.app')

    config.registry.registerUtility(LanguageByFamilyMapMarker(), IMapMarker)

    return config.make_wsgi_app()
