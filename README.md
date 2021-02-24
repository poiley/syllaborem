# :open_book: Syllaborem
Syllaborem is a Django web app who's goal is to turn your Syllabus into something more pleasant.

## :inbox_tray: Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.

```bash
pip install -r requirements.txt
```

## :hammer_and_wrench: Usage

```python
from apps import reader

r = reader.core.Reader()

print(r.read_file('Syllabus.pdf'))

```

## :pencil2: Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## :pushpin: License
[The Unlicence](https://unlicense.org/)