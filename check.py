import sys
from enum import Enum

from recipe_scrapers import scrape_me, WebsiteNotImplementedError

class Status(Enum):
    IMPLEMENTED = 0
    HAS_SCHEMA = 1
    NO_SCHEMA = 2

def check(url):
    """
    Returns the status of the website in the recipe-scrapers package.
    If the package has a scraper for this site, will return IMPLEMENTED.
    If the packaga has no scraper for this site, but a Recipe schema is detected, will return HAS_SCHEMA.
    If the package has no scraper for the site and no Recipe schema is detected, will return NO_SCHEMA.
    """
    try:
        scrape_me(url)
        return Status.IMPLEMENTED
    except WebsiteNotImplementedError:
        try:
            scrape_me(url, wild_mode=True)
            return Status.HAS_SCHEMA
        except:
            return Status.NO_SCHEMA

def main():
    if len(sys.argv) < 2:
        print("URL not provided.")
        return
    
    url = sys.argv[1]
    
    status = check(url)

    match status:
        case Status.IMPLEMENTED:
            print("IMPLEMENTED")
        case Status.HAS_SCHEMA:
            print("SCHEMA FOUND")
        case Status.NO_SCHEMA:
            print("NO SCHEMA FOUND")

if __name__ == "__main__":
    main()
