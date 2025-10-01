# -*- coding: utf-8 -*-
"""
Created on Tue Sep 30 21:35:23 2025

@author: olivi
"""

import bibtexparser
import csv
import re

def slugify(title):
    return re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')

# Load your ORCID bib file
with open("works.bib", encoding="utf-8") as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

# Open TSV file for academicpages
with open("publications.tsv", "w", newline="", encoding="utf-8") as tsvfile:
    fieldnames = [
        "pub_date", "title", "venue", "excerpt",
        "citation", "url_slug", "paper_url", "slides_url"
    ]
    writer = csv.DictWriter(tsvfile, fieldnames=fieldnames, delimiter="\t")
    writer.writeheader()

    # Map month abbreviations to numbers
    month_map = {
        "jan": "01","feb": "02","mar": "03","apr": "04",
        "may": "05","jun": "06","jul": "07","aug": "08",
        "sep": "09","oct": "10","nov": "11","dec": "12"
    }

    for entry in bib_database.entries:
        year = entry.get("year", "1900")
        month = entry.get("month", "01")
        month = month_map.get(month.lower(), month.zfill(2))
        pub_date = f"{year}-{month}-01"

        title = entry.get("title", "").strip("{}")
        venue = entry.get("journal") or entry.get("booktitle") or ""
        url = entry.get("url") or (f"https://doi.org/{entry['doi']}" if "doi" in entry else "")
        citation = f"{entry.get('author','')}. ({year}). \"{title}.\" <i>{venue}</i>."

        writer.writerow({
            "pub_date": pub_date,
            "title": title,
            "venue": venue,
            "excerpt": "",  # optional: fill later
            "citation": citation,
            "url_slug": slugify(title),
            "paper_url": url,
            "slides_url": ""
        })
