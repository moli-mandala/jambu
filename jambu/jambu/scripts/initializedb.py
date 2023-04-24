import itertools
import collections

from nameparser import HumanName
from pycldf import Sources
from clldutils.misc import nfilter, slug
from clldutils.color import qualitative_colors
from clld.cliutil import Data, bibtex2source
from clld.db.meta import DBSession
from clld.db.models import common
from clld.lib import bibtex

from tqdm import tqdm

import jambu
from jambu import models
import re

families = [
    "OIA",
    "MIA",
    "Nuristani",
    "Pashai",
    "Chitrali",
    "Shinaic",
    "Kohistani",
    "Kunar",
    "Kashmiric",
    "Western Pahari",
    "Central Pahari",
    "Eastern Pahari",
    "Lahndic",
    "Punjabic",
    "Sindhic",
    "Gujaratic",
    "Bhil",
    "Rajasthanic",
    "Marathi-Konkani",
    "Insular",
    "Halbic",
    "Eastern",
    "Bihari",
    "Eastern Hindi",
    "Western Hindi",
    "Migratory",
    "Old Dravidian",
    "South Dravidian I",
    "South Dravidian II",
    "Central Dravidian",
    "North Dravidian",
    "Brahui",
    "Munda",
    "Burushaski",
    "Other",
]
order = {x: chr(i + 65) for i, x in enumerate(families)}
print(order)


def iteritems(cldf, t, *cols):
    cmap = {cldf[t, col].name: col for col in cols}
    for item in cldf[t]:
        for k, v in cmap.items():
            item[v] = item[k]
        yield item


def main(args):

    assert args.glottolog, 'The --glottolog option is required!'

    data = Data()
    ds = data.add(
        common.Dataset,
        jambu.__name__,
        id=jambu.__name__,
        name='Jambu',
        domain='jambu-clld.herokuapp.com',
        publisher_name="Georgetown University",
        publisher_place="Washington",
        publisher_url="http://gucl.georgetown.edu/",
        license="http://creativecommons.org/licenses/by/4.0/",
        jsondata={
            'license_icon': 'cc-by.png',
            'license_name': 'Creative Commons Attribution 4.0 International License'},

    )

    for i, name in enumerate(['Aryaman Arora']):
        common.Editor(
            dataset=ds,
            ord=i,
            contributor=common.Contributor(id=slug(HumanName(name).last), name=name)
        )


    contrib = data.add(
        common.Contribution,
        None,
        id='cldf',
        name=args.cldf.properties.get('dc:title'),
        description=args.cldf.properties.get('dc:bibliographicCitation'),
    )

    print("Languages...")
    for lang in iteritems(args.cldf, 'LanguageTable', 'id', 'name', 'glottocode', 'longitude', 'latitude', 'Clade'):
        data.add(
            models.Variety,
            lang['id'],
            id=lang['id'],
            name=lang['name'],
            latitude=lang['latitude'],
            longitude=lang['longitude'],
            glottocode=lang['glottocode'],
            family=lang['Clade'],
            order=order[lang['Clade']] + '_' + lang['name']
        )

    for rec in bibtex.Database.from_file(args.cldf.bibpath, lowercase=True):
        data.add(common.Source, rec.id, _obj=bibtex2source(rec))

    refs = collections.defaultdict(list)

    counts = collections.defaultdict(set)
    print("Forms...")
    for form in tqdm(iteritems(args.cldf, 'FormTable', 'id', 'form', 'languageReference', 'parameterReference', 'source')):
        counts[form['parameterReference']].add(form['languageReference'])

    print("Params...")
    for param in tqdm(iteritems(args.cldf, 'ParameterTable', 'ID', 'Name', 'Language_ID', 'Description')):
        data.add(
            models.Concept,
            param['ID'],
            id=param['ID'],
            name='{} [{}]'.format(param['Name'], param['ID']),
            language=param['Language_ID'],
            description=param['Description'],
            etyma=param['Etyma'],
            count=len(counts[param['ID']])
        )

    print("Forms...")
    for form in tqdm(iteritems(args.cldf, 'FormTable', 'id', 'form', 'languageReference', 'parameterReference', 'source')):
        l = re.split(r";|\+", form['parameterReference'])
        for i, paramref in enumerate(l):
            if paramref == '?': continue
            vsid = (form['languageReference'], paramref)
            vs = data['ValueSet'].get(vsid)
            if not vs:
                vs = data.add(
                    common.ValueSet,
                    vsid,
                    id='-'.join(vsid),
                    language=data['Variety'][form['languageReference']],
                    parameter=data['Concept'][paramref],
                    contribution=contrib,
                )
                
            for ref in form.get('source', []):
                sid, pages = Sources.parse(ref)
                refs[(vsid, sid)].append(pages)
                
            data.add(
                models.Lexeme,
                form['id'] + '-' + str(i) if len(l) > 1 else form['id'],
                id=form['id'] + '-' + str(i) if len(l) > 1 else form['id'],
                name=form['form'],
                gloss=form['Gloss'],
                native=form['Native'],
                phonemic='/' + form['Phonemic'] + '/' if form['Phonemic'] else None,
                description=form['Description'],
                cognateset=form['Cognateset'],
                valueset=vs,
            )

    print("Refs...")
    for (vsid, sid), pages in tqdm(refs.items()):
        if sid not in data['Source']:
            print(sid)
        else:
            DBSession.add(common.ValueSetReference(
                valueset=data['ValueSet'][vsid],
                source=data['Source'][sid],
                description='; '.join(nfilter(pages))
            ))

    # print("Glottolog families...")
    # load_families(
    #     Data(),
    #     [(l.glottocode, l) for l in data['Variety'].values()],
    #     glottolog_repos=args.glottolog,
    #     isolates_icon='tcccccc',
    #     strict=False,
    # )



def prime_cache(args):
    """If data needs to be denormalized for lookup, do that here.
    This procedure should be separate from the db initialization, because
    it will have to be run periodically whenever data has been updated.
    """
