A utility tool to determine the implementation status in [recipe-scrapers](https://github.com/hhursev/recipe-scrapers) of a specific website.
If no implementation is found, will determine if a [Recipe schema](https://schema.org/Recipe) is found in the website.

# Install
## Clone the repository
```
$ git@github.com:mlduff/recipe-scrapers-check.git
$ cd recipe-scrapers-check
```
## Install dependencies in virtual environment
```
$ python -m venv .venv --upgrade-deps
$ source .venv/bin/activate
$ pip install -r requirements.txt
```
# Usage
```
$ python check.py <URL>
```
Will return:
- `IMPLEMENTED` if `recipe-scrapers` has a scraper implementation
- `HAS_SCHEMA` if no implementation is found but the website supports the Recipe schema
- `NO_SCHEMA` if no implementation is found and the website doesn't support the Recipe schema
## Example
```
$ python check.py https://www.bestrecipes.com.au/recipes/aussie-meat-pie-recipe-2/34l4qr5q
```