# CDIAL

Various scripts and programs dealing with the *Comparative Dictionary of the Indo-Aryan Languages* by Ralph Lilley Turner (hosted on [SOAS by UChicago](https://dsal.uchicago.edu/dictionaries/soas/)).

You need Python 3.x; to run Jambu (CLLD app for CDIAL) do this:

```bash
pip install -r requirements.txt
python main.py
```

You can edit `main.py` to change the port and IP for hosting Jambu.

## Files

- `jambu/`: The CLLD app including the entire parsed CDIAL, plus Liljegren's Palula data, my Kholosi data, data from various papers of Patyal on Mandeali and Dogri (+more W. Pahari), and eventually even more extensions.
- `main.py`: Runs the server for `jambu/`

Other stuff:
- `parse.py`: Script that parses the CDIAL data to store in `data/all.json`
- `data/`: Various data in CSV and JSON format, used for `jambu/`. The CSVs are hand-compiled.
- `cldf.py`: Makes CLDF format data from the parsed CDIAL + manual extensions datasets.
- `cldf/`: The data used to build `jambu/`'s SQLite database.
- `scripts/`: Miscellaneous stuff for testing CDIAL parses before I made the CLLD app. Some of the data here is from Chundra Cathcart's parsed data.