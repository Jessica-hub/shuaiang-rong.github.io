# -*- coding: utf-8 -*-
"""
Created on Wed Oct  1 15:44:13 2025

@author: olivi
"""

import bibtexparser
import csv
import re
import html

def slugify(title):
    return re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')

def ieee_citation(entry):
    # build author string
    authors_raw = entry.get("author", "").replace("\n", " ").split(" and ")
    authors = ", ".join(a.strip() for a in authors_raw)
    title = entry.get("title", "").replace("{", "").replace("}", "").replace("\n", " ")
    title = html.escape(title)  # ensure quotes etc safe
    venue = entry.get("journal") or entry.get("booktitle") or ""
    year = entry.get("year", "")
    volume = entry.get("volume", "")
    number = entry.get("number", "")
    pages = entry.get("pages", "")

    citation = f"{authors}. &quot;{title}.&quot; <i>{venue}</i>"
    if volume:
        citation += f", vol. {volume}"
    if number:
        citation += f", no. {number}"
    if pages:
        citation += f", pp. {pages}"
    if year:
        citation += f", {year}."
    return citation

def bib_to_tsv(bibfile, tsvfile, paper_start_idx=1):
    with open(bibfile, encoding="utf-8") as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)

    with open(tsvfile, "w", newline="", encoding="utf-8") as tsvfile_out:
        fieldnames = [
            "pub_date", "title", "venue", "excerpt",
            "citation", "url_slug", "paper_url", "slides_url", "bibtex_url"
        ]
        writer = csv.DictWriter(tsvfile_out, fieldnames=fieldnames, delimiter="\t")
        writer.writeheader()

        month_map = {
            "jan": "01","feb": "02","mar": "03","apr": "04",
            "may": "05","jun": "06","jul": "07","aug": "08",
            "sep": "09","oct": "10","nov": "11","dec": "12"
        }

        i = paper_start_idx
        for entry in bib_database.entries:
            year = entry.get("year", "1900")
            month = entry.get("month", "01")
            month = month_map.get(month.lower(), month.zfill(2))
            pub_date = f"{year}-{month}-01"

            title = entry.get("title", "").strip("{}")
            venue = entry.get("journal") or entry.get("booktitle") or ""
            citation = ieee_citation(entry)

            # PDF files you named paper1.pdf, paper2.pdf etc.
            paper_url = f"http://jessica-hub.github.io/files/paper{i}.pdf"

            writer.writerow({
                "pub_date": pub_date,
                "title": title,
                "venue": venue,
                "excerpt": "",  # optional
                "citation": citation,
                "url_slug": slugify(title),
                "paper_url": paper_url,
                "slides_url": "",  # leave blank
                "bibtex_url": f"http://jessica-hub.github.io/files/{bibfile}"
            })
            i += 1

# Run for both bib files
bib_to_tsv("pubs.bib", "publications_journals.tsv", paper_start_idx=1)
bib_to_tsv("proceedings.bib", "publications_proceedings.tsv", paper_start_idx=20)  # adjust start idx if needed
