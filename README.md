# Jambu

Various scripts and programs dealing with the *Comparative Dictionary of the Indo-Aryan Languages* by Ralph Lilley Turner (hosted on [SOAS by UChicago](https://dsal.uchicago.edu/dictionaries/soas/)).

You need Python 3.x and `pip`; to run Jambu (CLLD app for CDIAL) do this:

```bash
pip install -r requirements.txt
./run
```

You can edit `main.py` to change the port and IP for hosting Jambu.

## Data sources
Check the dataset front page.

## Files

- `jambu/`: The CLLD app including the entire parsed CDIAL, plus Liljegren's Palula data, my Kholosi data, data from various papers of Patyal on Mandeali and Dogri (+more W. Pahari), and eventually even more extensions.
- `main.py`: Runs the server for `jambu/`

## Building the database

You probably don't need to do this since I commit the SQLite database directly to the repo. These instructions are for myself.

```bash
python parse.py
python cldf.py
cd jambu
pip install -e .
clld initdb development.ini --glottolog ~/Downloads/glottolog-glottolog-cldf-6f1558e --cldf ~/Documents/computerscience/jambu-data/cldf/Wordlist-metadata.json
```

To test:

```bash
pserve --reload development.ini
```