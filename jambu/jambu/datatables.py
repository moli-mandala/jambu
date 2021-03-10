from sqlalchemy.orm import joinedload
from clld.web import datatables
from clld.web.datatables.base import LinkCol, Col, LinkToMapCol

from clld_glottologfamily_plugin.models import Family
from clld_glottologfamily_plugin.datatables import FamilyCol


from jambu import models




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
                Col(self, 'gloss'),
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
                Col(self, 'gloss'),
                Col(self, 'native'),
                Col(self, 'phonemic'),
                Col(self, 'description'),
                Col(
                    self,
                    'name',
                    model_col=models.Cognate_.name,
                    get_object=f,
                    sTitle='Cognate')
            ]


def includeme(config):
    """register custom datatables"""

    config.register_datatable('languages', Languages)
    config.register_datatable('values', Values)
