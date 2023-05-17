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
    "Pashai": "FFD6F6",
    "Chitrali": "FFACEF",
    "Shinaic": "FF81E6",
    "Kohistani": "FF25D5",
    "Kashmiric": "FF00CD",
    "Kunar": "ff68e0",
    "Western Pahari": "B94E16",
    "Central Pahari": "9E521B",
    "Eastern Pahari": "79421B",
    "Lahndic": "a4d6f5",
    "Punjabic": "7164FF",
    "Sindhic": "0066FF",
    "Gujaratic": "00CF4A",
    "Rajasthanic": "6BCD00",
    "Marathi-Konkani": "D50000",
    "Insular": "AC0000",
    "Eastern": "FFDE54",
    "Bihari": "FFCD00",
    "Eastern Hindi": "FF9A54",
    "Western Hindi": "FF6600",
    "Migratory": "63666A",
    "MIA": "FFDEAD",
    "OIA": "E2DFD2",
    "Other": "FAF9F6",
    "Nuristani": "9132a8",
    "Bhil": "09AD02",
    "Khandeshi": "2FFF2F",
    "Halbic": "AB8900",
    "Brahui": "49796B",
    "South Dravidian I": "74C365",
    "South Dravidian II": "98FB98",
    "Central Dravidian": "29AB87",
    "North Dravidian": "4B6F44",
    "Old Dravidian": "679267",
    "Munda": "00ffd0",
    "Burushaski": "f3ff05",
    "Nihali": "ff9a00"
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
