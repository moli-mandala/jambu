from sqlalchemy.orm import joinedload
from clld.web import datatables
from clld.web.datatables.base import LinkCol, Col, LinkToMapCol, IdCol, DetailsRowLinkCol, IntegerIdCol, RefsCol, DataTable

from clld_glottologfamily_plugin.models import Family
from clld.web.util.htmllib import HTML
from clld.web.util.helpers import linked_references, map_marker_img
from clld.db.models.common import Value, ValueSet

from jambu.models import Variety, Concept, Lexeme

class FormCol(LinkCol):
    def order(self):
        return Lexeme.cognateset

class LanguageCol(LinkCol):
    def order(self):
        return Variety.order

    def format(self, item):
        return HTML.span(
            map_marker_img(self.dt.req, self.get_obj(item)),
            LinkCol.format(self, item))

class Parameters(datatables.Parameters):
    def col_defs(self):
        return [
            IntegerIdCol(self, 'count'),
            LanguageCol(
                self, 'name',
                model_col=Variety.name,
                get_object=lambda i: i.language,
                sTitle='Language'
            ),
            LinkCol(self, 'name'),
            Col(self, 'count', model_col=Concept.count)
        ]


class Languages(datatables.Languages):
    def col_defs(self):
        return [
            LanguageCol(self, 'name'),
            Col(self, 'family'),
            Col(self,
                'latitude',
                sDescription='<small>The geographic latitude</small>'),
            Col(self,
                'longitude',
                sDescription='<small>The geographic longitude</small>'),
            LinkToMapCol(self, 'm'),
        ]

def f(x):
    # print(x)
    return x.cognateset

class Values(datatables.Values):
    def base_query(self, query):
        if not any([self.language, self.parameter, self.contribution]):
            return query.join(ValueSet)\
                .join(ValueSet.language)\
                .join(ValueSet.parameter)\
                .options(
                    joinedload(Value.valueset).joinedload(ValueSet.language),
                    joinedload(Value.valueset).joinedload(ValueSet.parameter),
                )
        return datatables.Values.base_query(self, query)
        
    def col_defs(self):
        if self.language:
            return [
                FormCol(
                    self,
                    'parameter',
                    model_col=Concept.name,
                    get_object=lambda i: i.valueset.parameter,
                    sTitle='Etymon'
                ),
                LanguageCol(
                    self,
                    'language',
                    model_col=Concept.name,
                    get_object=lambda i: i.valueset.parameter.language,
                    sTitle='Source'
                ),
                LinkCol(self, 'name', sTitle='Form'),
                Col(self, 'gloss', model_col=Lexeme.gloss),
                Col(self, 'phonemic'),
                Col(self, 'description'),
                RefsCol(self, 'references', get_object=lambda i: i.valueset)
            ]
        if self.parameter:
            return [
                LanguageCol(
                    self, 'name',
                    model_col=Variety.name,
                    get_object=lambda i: i.valueset.language,
                    sTitle='Language'
                ),
                LinkCol(self, 'name', sTitle='Form'),
                Col(self, 'gloss', model_col=Lexeme.gloss),
                Col(self, 'phonemic'),
                Col(self, 'description'),
                RefsCol(self, 'references', get_object=lambda i: i.valueset)
            ]
        return [
            LanguageCol(
                self,
                'language',
                model_col=Variety.name,
                get_object=lambda i: i.valueset.language,
                sTitle='Language'
            ),
            LinkCol(self, 'name', sTitle='Form'),
            LanguageCol(
                self,
                'language',
                model_col=Concept.name,
                get_object=lambda i: i.valueset.parameter.language,
                sTitle='Source'
            ),
            LinkCol(
                self,
                'parameter',
                model_col=Concept.name,
                get_object=lambda i: i.valueset.parameter,
                sTitle='Etymon'
            ),
            Col(self, 'gloss', model_col=Lexeme.gloss),
            Col(self, 'phonemic'),
            Col(self, 'description')
        ]



def includeme(config):
    """register custom datatables"""

    config.register_datatable('languages', Languages)
    config.register_datatable('values', Values)
    config.register_datatable('parameters', Parameters)
