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
    authors_raw = entry.get("author", "").replace("\n", " ").split(" and ")
    formatted_authors = []
    for name in authors_raw:
        parts = name.strip().split(",")
        if len(parts) == 2:
            last, firsts = parts[0].strip(), parts[1].strip()
            initials = " ".join([f"{x[0]}." for x in firsts.split() if x])
            full_name = f"{initials} {last}".strip()
            formatted_authors.append(full_name)
        else:
            # If no comma, just try initials on first part:
            name_parts = name.strip().split()
            if len(name_parts) >= 2:
                last = name_parts[-1]
                firsts = " ".join(name_parts[:-1])
                initials = " ".join([f"{x[0]}." for x in firsts.split() if x])
                full_name = f"{initials} {last}".strip()
                formatted_authors.append(full_name)
            else:
                formatted_authors.append(name.strip())
    
    # Insert "and" before the last author
    if len(formatted_authors) > 1:
        authors = ", ".join(formatted_authors[:-1]) + " and " + formatted_authors[-1]
    else:
        authors = formatted_authors[0] if formatted_authors else ""

    title = entry.get("title", "").replace("{", "").replace("}", "").replace("\n", " ")
    title = html.escape(title)
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

def bib_to_tsv(bibfile, tsvfile, paper_start_idx=1, category="manuscripts"):
    with open(bibfile, encoding="utf-8") as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)

    with open(tsvfile, "w", newline="", encoding="utf-8") as tsvfile_out:
        fieldnames = [
            "pub_date", "title", "venue", "excerpt",
            "citation", "url_slug", "paper_url", "slides_url",
            "bibtex_url", "category"
        ]
        writer = csv.DictWriter(tsvfile_out, fieldnames=fieldnames, delimiter="\t")
        writer.writeheader()

        month_map = {
            "jan": "01", "feb": "02", "mar": "03", "apr": "04",
            "may": "05", "jun": "06", "jul": "07", "aug": "08",
            "sep": "09", "oct": "10", "nov": "11", "dec": "12",
            "january": "01", "february": "02", "march": "03", "april": "04",
            "june": "06", "july": "07", "august": "08", "september": "09",
            "october": "10", "november": "11", "december": "12"
        }

        i = paper_start_idx
        for entry in bib_database.entries:
            fields = entry
            year = str(fields.get("year", "")).strip()
            month_raw = str(fields.get("month", "")).strip().lower()
            month = month_map.get(month_raw[:3], "")
            day = str(fields.get("day", "")).zfill(2) if "day" in fields else ""

            if year and month and day:
                pub_date = f"{year}-{month}-{day}"
            elif year and month:
                pub_date = f"{year}-{month}-01"
            elif year:
                pub_date = f"{year}-01-01"
            else:
                pub_date = ""

            title = fields.get("title", "").strip("{} \n")
            venue = fields.get("journal") or fields.get("booktitle") or ""
            citation = ieee_citation(fields)

            paper_url = f"http://jessica-hub.github.io/files/paper{i}.pdf"

            writer.writerow({
                "pub_date": pub_date,
                "title": title,
                "venue": venue,
                "excerpt": "",
                "citation": citation,
                "url_slug": slugify(title),
                "paper_url": paper_url,
                "slides_url": "",
                "bibtex_url": f"http://jessica-hub.github.io/files/{bibfile}",
                "category": category
            })
            i += 1

# Call the updated function
bib_to_tsv("pubs.bib", "publications_journals.tsv", paper_start_idx=1, category="manuscripts")
bib_to_tsv("proceedings.bib", "publications_proceedings.tsv", paper_start_idx=20, category="conferences")
