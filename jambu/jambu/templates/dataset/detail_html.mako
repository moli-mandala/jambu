<%inherit file="../home_comp.mako"/>

<%def name="sidebar()">
    <div class="well">
        <h3>Cite</h3>
        <p>
            Arora, Aryaman. 2021. <em>Jambu</em>. Washington: Georgetown University.
        <h3>Compilers</h3>
        <p>
            <ul>
                <li>Aryaman Arora</li>
                <li>Adam Farris</li>
            </ul>
        </p>
    </div>
</%def>

<h2>Welcome to <i>Jambu</i></h2>

<p class="lead">
    <i>Jambu</i> [i.e. the Indian blackberry, jāmun, <em>Syzygium cumini</em>] is an online etymological dictionary of Indo-Aryan languages, meant to be a modern continuation of Ralph Lilley Turner's <em>Comparative Dictionary of the Indo-Aryan Languages</em> augmented with new data.
</p>

<p>
The app is currently in development mode (it's a bit rough around the edges!) but should be fully functional, and the entire CDIAL is incorprated (albeit with some issues due to transcription errors in its parsing at the University of Chicago).
</p>

<p>
All credit for the data in this app goes to the creators, which each lexicon entry references. Some of this data is still in copyright; I do not intend to make money off of this, it's purely for use by linguistics researchers and language hobbyists, so please do not sue me.
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
<ul>
    <li>Ralph Lilley Turner. 1962–1966. A comparative dictionary of the Indo-Aryan languages. Oxford University Press.</li>
    <li>Liljegren, Henrik. 2019. Palula dictionary. Dictionaria. 1-2700. Jena: Max Planck Institute for the Science of Human History.</li>
    <li>Aryaman Arora. 2020–2021. Kholosi Dictionary.</li>
    <li>Hukam Chand Patyal. 1982. Etymological notes on some Maṇḍyāḷī words (Indo-Aryan Studies II). Indo-Iranian Journal 24. 289–294. Brill.</li>
    <li>Hukam Chand Patyal. 1991. Etymological notes on some Ḍogri words (Indo-Aryan Studies III). Indo-Iranian Journal 34. 123–124. Brill.</li>
    <li>Hukam Chand Patyal. 1983. Etymological notes on some Maṇḍyāḷī words (Indo-Aryan Studies IV). Indo-Iranian Journal 25. 41–49. Brill.</li>
    <li>Hukam Chand Patyal. 1984. Etymological notes on some Maṇḍyāḷī words (Indo-Aryan Studies V). Indo-Iranian Journal 27. 121–132. Brill.</li>
    <li>Hukam Chand Patyal. 1984. Etymological notes on some Maṇḍyāḷī words (Indo-Aryan Studies V). Indo-Iranian Journal 27. 121–132. Brill.</li>
    <li>Strand, Richard F. 1997–2021. Nuristân: Hidden Land of the Hindu-Kush.</lo>
</ul>

<b>Partial</b>
<ul>
    <li>Bhawnani, Murli D. 1979. Descriptive analysis of Thari: A dialect of Sindhi language. (Doctoral dissertation, Deccan College Post Graduate and Research Institute Pune).</li>
</ul>