<%inherit file="../home_comp.mako"/>

<%def name="sidebar()">
    <div class="well">
        <h3>Cite</h3>
        <p>
            Arora, Aryaman (2021–2022). <em>Jambu</em>. Washington: Georgetown University.
        <h3>Compilers</h3>
        <p>
            <ul>
                <li>Aryaman Arora</li>
                <li>Adam Farris</li>
                <li>Suresh Kolichala</li>
            </ul>
        </p>
    </div>
</%def>

<h2>Jambu</h2>

<p class="lead">
    <i>Jambu</i> [i.e. the Indian blackberry, jāmun, <em>Syzygium cumini</em>] is an online etymological dictionary of South Asian languages, meant to be a modern compilation of Turner's CDIAL and the DED(R), augmented with new data.
</p>

<p>
The dictionary will always be a work-in-progress but is fully functional, and the entire CDIAL and DEDR are incorprated with relatively minor data issues. A few other sources documenting individual languages with reference to those dictionaries have been included, as well as some completely new etymologies posited by us.
</p>

<p>
All credit for the data in this app goes to the original scraped source, which each lexicon entry directly references. Some of this data is probably still in copyright; I do not intend to make money off of this, it's purely for use by linguistics researchers and language hobbyists, so please do not sue me.
</p>

<p>
A brief overview:
<ul>
<li><a href="parameters">Parameters</a> is a list of the numbered CDIAL entries, plus any additions to them. Clicking on an entry gives a map, list of descendants/cognates, and the CDIAL headword line.</li>
<li><a href="values">Values</a> is the entire lexicon, all entries in all languages. Be warned that it is slow to load, since it's >170k entries.</li>
<li><a href="languages">Languages</a> is all of the languages referenced by CDIAL. Clicking a languages gives its lexicon.</li>
<li><a href="sources">Sources</a> is a list of references.</li>
</ul>
</p>

<h3>Works included</h3>
<p>(<span style="color: red;">▲</span> = partial.)
<ul>
    <li>Ralph Lilley Turner (1962–1966). <em><a href="https://dsal.uchicago.edu/dictionaries/soas/">A comparative dictionary of the Indo-Aryan languages</a></em>. Oxford University Press.</li>
    <li>T. Burrow and M. B. Emeneau (1984). <em><a href="https://dsal.uchicago.edu/dictionaries/burrow/">A Dravidian etymological dictionary</a></em>. 2nd ed. Oxford: Clarendon Press.</li>
    <li>Liljegren, Henrik (2019). <em><a href="https://dictionaria.clld.org/contributions/palula">Palula dictionary</a></em>. Dictionaria. 1-2700. Jena: Max Planck Institute for the Science of Human History.</li>
    <li>Hukam Chand Patyal (1982). Etymological notes on some Maṇḍyāḷī words (Indo-Aryan Studies II). <em>Indo-Iranian Journal</em> 24. 289–294. Brill.</li>
    <li>Hukam Chand Patyal (1991). Etymological notes on some Ḍogri words (Indo-Aryan Studies III). <em>Indo-Iranian Journal</em> 34. 123–124. Brill.</li>
    <li>Hukam Chand Patyal (1983). Etymological notes on some Maṇḍyāḷī words (Indo-Aryan Studies IV). <em>Indo-Iranian Journal</em> 25. 41–49. Brill.</li>
    <li>Hukam Chand Patyal (1984). Etymological notes on some Maṇḍyāḷī words (Indo-Aryan Studies V). <em>Indo-Iranian Journal</em> 27. 121–132. Brill.</li>
    <li>Hukam Chand Patyal (1984). Etymological notes on some Maṇḍyāḷī words (Indo-Aryan Studies V). <em>Indo-Iranian Journal</em> 27. 121–132. Brill.</li>
    <li>Richard F. Strand (1997–2021). <em><a href="http://nuristan.info/">Nuristân: Hidden Land of the Hindu-Kush</a></em>.</li>
    <li>Sonja Fritz (2002). <em>The Dhivehi language: a descriptive and historical grammar of Maldivian and its dialects</em>.</li>
    <li><span style="color: red;">▲</span> Matthew Toulmin (2006). <em>Reconstructing linguistic history in a dialect continuum: The Kamta, Rajbanshi, and Northern Deshi Bangla subgroup of Indo-Aryan</em> (PhD thesis). Australian National University.</li>
</ul>

<b>Etymologised by us</b>
<ul>
    <li>Aryaman Arora (2020–2021). <a href="https://aryamanarora.github.io/kholosi/Kholosi_Dictionary.pdf"><em>Kholosi Dictionary</em></a>.</li>
    <li><span style="color: red;">▲</span> Murli D. Bhawnani (1979). <a href="https://shodhganga.inflibnet.ac.in/handle/10603/169640"><em>Descriptive analysis of Thari: A dialect of Sindhi language</em></a> (PhD thesis). Deccan College Post Graduate and Research Institute Pune).</li>
    <li>Thomas Jouanne (2014). <em><a href="https://www.duo.uio.no/bitstream/handle/10852/43094/Masteroppgave-Sr-Adia-studier.pdf?sequence=1">A preliminary analysis of the phonological system of the Western Pahārī language of Kvār</a></em> (PhD thesis). University of Oslo.</li>
</ul>