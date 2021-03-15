# CDIAL

Various scripts and programs dealing with the *Comparative Dictionary of the Indo-Aryan Languages* by Ralph Lilley Turner (hosted on [SOAS by UChicago](https://dsal.uchicago.edu/dictionaries/soas/)).

You need Python 3.x and `pip`; to run Jambu (CLLD app for CDIAL) do this:

```bash
pip install -r requirements.txt
cd jambu
python main.py
```

You can edit `main.py` to change the port and IP for hosting Jambu.

## Data sources
- Ralph Lilley Turner. 1962–1966. A comparative dictionary of the Indo-Aryan languages. Oxford University Press.
- Liljegren, Henrik. 2019. Palula dictionary. Dictionaria. 1-2700. Jena: Max Planck Institute for the Science of Human History.
- Aryaman Arora. 2020–2021. Kholosi Dictionary.
- Hukam Chand Patyal. 1982. Etymological notes on some Maṇḍyāḷī words (Indo-Aryan Studies II). Indo-Iranian Journal 24. 289–294. Brill.
- Hukam Chand Patyal. 1991. Etymological notes on some Ḍogri words (Indo-Aryan Studies III). Indo-Iranian Journal 34. 123–124. Brill.
- Hukam Chand Patyal. 1983. Etymological notes on some Maṇḍyāḷī words (Indo-Aryan Studies IV). Indo-Iranian Journal 25. 41–49. Brill.
- Hukam Chand Patyal. 1984. Etymological notes on some Maṇḍyāḷī words (Indo-Aryan Studies V). Indo-Iranian Journal 27. 121–132. Brill.

### To add
- Toulmin, Matthew William Stirling. 2006. Reconstructing linguistic history in a dialect continuum: The Kamta, Rajbanshi, and Northern Deshi Bangla subgroup of Indo-Aryan. (Doctoral dissertation, Faculty of Arts. School of Language Studies and The Australian National University).
- Claus Peter Zoller's Indus Kohistani
- Kalasha Dictionary
- Bhawnani, Murli D. 1979. Descriptive analysis of Thari: A dialect of Sindhi language. (Doctoral dissertation, Deccan College Post Graduate and Research Institute Pune).

## Files

- `jambu/`: The CLLD app including the entire parsed CDIAL, plus Liljegren's Palula data, my Kholosi data, data from various papers of Patyal on Mandeali and Dogri (+more W. Pahari), and eventually even more extensions.
- `main.py`: Runs the server for `jambu/`

Other stuff:
- `parse.py`: Script that parses the CDIAL data to store in `data/all.json`
- `data/`: Various data in CSV and JSON format, used for `jambu/`. The CSVs are hand-compiled.
- `cldf.py`: Makes CLDF format data from the parsed CDIAL + manual extensions datasets.
- `cldf/`: The data used to build `jambu/`'s SQLite database.
- `scripts/`: Miscellaneous stuff for testing CDIAL parses before I made the CLLD app. Some of the data here is from Chundra Cathcart's parsed data.

## Building the database

You probably don't need to do this since I commit the SQLite database directly to the repo. These instructions are for myself.

```bash
python parse.py
python clld.py
cd jambu
clld initdb development.ini --glottolog ../glottolog --cldf ../cldf/Wordlist-metadata.json
```

To test:

```bash
pserve --reload development.ini
```