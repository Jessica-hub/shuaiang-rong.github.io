import bibtexparser, csv, re

def slugify(title):
    return re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')

month_map = {
    "jan": "01","feb": "02","mar": "03","apr": "04",
    "may": "05","jun": "06","jul": "07","aug": "08",
    "sep": "09","oct": "10","nov": "11","dec": "12"
}

def bib_to_tsv(bibfile, outfile):
    with open(bibfile, encoding="utf-8") as f:
        bibdb = bibtexparser.load(f)

    with open(outfile, "w", newline="", encoding="utf-8") as tsvfile:
        fieldnames = ["pub_date","title","venue","excerpt",
                      "citation","url_slug","paper_url","bibtex_url"]
        writer = csv.DictWriter(tsvfile, fieldnames=fieldnames, delimiter="\t")
        writer.writeheader()

        for idx, entry in enumerate(bibdb.entries, start=1):
            year = entry.get("year","1900")
            month = entry.get("month","01").lower()[:3]
            month = month_map.get(month, "01")
            pub_date = f"{year}-{month}-01"

            title = entry.get("title","").strip("{}")
            venue = entry.get("journal") or entry.get("booktitle") or ""
            citation = f"{entry.get('author','')}. ({year}). \"{title}.\" <i>{venue}</i>."

            writer.writerow({
                "pub_date": pub_date,
                "title": title,
                "venue": venue,
                "excerpt": "",
                "citation": citation,
                "url_slug": slugify(title),
                "paper_url": f"http://academicpages.github.io/files/paper{idx}.pdf",
                "bibtex_url": f"http://academicpages.github.io/files/{bibfile}"
            })

# Generate TSVs
bib_to_tsv("pubs.bib", "publications_journals.tsv")
bib_to_tsv("proceedings.bib", "publications_proceedings.tsv")
