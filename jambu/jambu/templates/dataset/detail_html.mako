<%inherit file="../home_comp.mako"/>

<%def name="sidebar()">
    <div class="well">
        <h3>Cite</h3>
        <p>
            Arora, Aryaman. 2021. <em>Jambu</em>. Washington: Georgetown University.
        <h3>Compilers</h3>
        <p>
            Aryaman Arora
        </p>
    </div>
</%def>

<h2>Welcome to <i>Jambu</i></h2>

<p class="lead">
    <i>Jambu</i> [i.e. the Indian blackbery, jāmun, <em>Syzygium cumini</em>] is an online etymological dictionary of Indo-Aryan languages, meant to be a modern continuation of Ralph Lilley Turner's <em>Comparative Dictionary of the Indo-Aryan Languages</em> augmented with new data.
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
