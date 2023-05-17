from zope.interface import implementer
from sqlalchemy import (
    Column,
    String,
    Unicode,
    Integer,
    Boolean,
    ForeignKey,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship, backref, joinedload
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.ext.hybrid import hybrid_property

from clld import interfaces
from clld.db.meta import Base, CustomModelMixin
from clld.db.models import common, HasSourceNotNullMixin, PolymorphicBaseMixin, IdNameDescriptionMixin, HasDataMixin, HasFilesMixin, HasSourceMixin

from clld_glottologfamily_plugin.models import HasFamilyMixin
from clld_cognacy_plugin.models import Cognate

#-----------------------------------------------------------------------------
# specialized common mapper classes
#-----------------------------------------------------------------------------

@implementer(interfaces.ILanguage)
class Variety(CustomModelMixin, common.Language, HasFamilyMixin):
    pk = Column(Integer, ForeignKey('language.pk'), primary_key=True)
    order = Column(Integer)
    glottocode = Column(Unicode)
    family = Column(Unicode)

@implementer(interfaces.IParameter)
class Concept(CustomModelMixin, common.Parameter):
    pk = Column(Integer, ForeignKey('parameter.pk'), primary_key=True)
    language_pk = Column(Integer, ForeignKey('language.pk'))
    language = relationship(Variety, backref=backref('concept'))
    description = Column(Unicode)
    etyma = Column(Unicode)
    count = Column(Integer)

@implementer(interfaces.IValue)
class Lexeme(CustomModelMixin, common.Value):
    pk = Column(Integer, ForeignKey('value.pk'), primary_key=True)
    gloss = Column(Unicode)
    native = Column(Unicode)
    phonemic = Column(Unicode)
    description = Column(Unicode)
    cognateset = Column(Integer)