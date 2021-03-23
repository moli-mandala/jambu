from sqlalchemy.orm import joinedload
from clld.web import datatables
from clld.web.datatables.base import LinkCol, Col, LinkToMapCol, IdCol, DetailsRowLinkCol, IntegerIdCol, RefsCol

from clld_glottologfamily_plugin.models import Family
from clld_glottologfamily_plugin.datatables import FamilyCol
from clld.web.util.helpers import linked_references
from clld.db.models.common import Value, ValueSet

from jambu import models

class Parameters(datatables.Parameters):
    def col_defs(self):
        return [
            IntegerIdCol(self, 'count'),
            LinkCol(self, 'name'),
            Col(self, 'count', model_col=models.Concept.count)
        ]


class Languages(datatables.Languages):
    def base_query(self, query):
        return query.join(Family).options(joinedload(models.Variety.family)).distinct()

    def col_defs(self):
        return [
            LinkCol(self, 'name'),
            FamilyCol(self, 'Family', models.Variety),
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
                LinkCol(
                    self,
                    'parameter',
                    model_col=models.Concept.name,
                    get_object=lambda i: i.valueset.parameter,
                    sTitle='Meaning'
                ),
                LinkCol(self, 'name', sTitle='Form'),
                Col(self, 'gloss', model_col=models.Lexeme.gloss),
                Col(self, 'native'),
                Col(self, 'phonemic'),
                Col(self, 'cognateset')
            ]
        if self.parameter:
            return [
                LinkCol(
                    self,
                    'language',
                    model_col=models.Variety.name,
                    get_object=lambda i: i.valueset.language,
                    sTitle='Language'
                ),
                LinkCol(self, 'name', sTitle='Form'),
                Col(self, 'gloss', model_col=models.Lexeme.gloss),
                Col(self, 'native'),
                Col(self, 'phonemic'),
                Col(self, 'description'),
                RefsCol(self, 'references', get_object=lambda i: i.valueset)
            ]
        return [
            LinkCol(
                self,
                'language',
                model_col=models.Variety.name,
                get_object=lambda i: i.valueset.language,
                sTitle='Language'
            ),
            LinkCol(self, 'name', sTitle='Form'),
            LinkCol(
                self,
                'parameter',
                model_col=models.Concept.name,
                get_object=lambda i: i.valueset.parameter,
                sTitle='Meaning'
            ),
            Col(self, 'gloss', model_col=models.Lexeme.gloss),
            Col(self, 'native'),
            Col(self, 'phonemic'),
            Col(self, 'description')
        ]



def includeme(config):
    """register custom datatables"""

    config.register_datatable('languages', Languages)
    config.register_datatable('values', Values)
    config.register_datatable('parameters', Parameters)
