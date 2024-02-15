# Bacon Ipsum Generator

This Python script allows you to generate Bacon Ipsum text using the Bacon Ipsum API. Bacon Ipsum is a placeholder text generator that provides dummy text similar to Lorem Ipsum but with a bacon-themed twist.

## Usage

1. Make sure you have Python 3.9 or higher installed on your system.
2. Install Poetry, a dependency management tool for Python, if you haven't already:
```commandline
curl -sSL https://install.python-poetry.org | python -
```
3. Install the required dependencies using Poetry:
```commandline
poetry install
```
4. Run the script with the desired parameters to generate Bacon Ipsum text. Here are some available options:
- `-t, --type`: Type of bacon text to generate (default: all-meat).
- `-p, --paras`: Number of paragraphs to generate (default: 5).
- `-l, --start-with-lorem`: Whether to start with "lorem" text (default: 1).
- `-f, --format`: Format of the response (default: json). Available options: json, text, html.
- `-s, --sentences`: Number of sentences (this overrides paragraphs).

Example usage:
```commandline
python bacon_ipsum_generator.py -t all-meat -p 3 -l 0 -f json
```

## Dependencies

- Python 3.9 or higher
- Poetry (dependency management)
- requests
- beautifulsoup4

Install Poetry and the project dependencies using the provided pyproject.toml file:
```commandline
curl -sSL https://install.python-poetry.org | python -
poetry install
```

---
