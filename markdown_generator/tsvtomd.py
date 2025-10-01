# -*- coding: utf-8 -*-
"""
Created on Wed Oct  1 15:45:06 2025

@author: olivi
"""

import pandas as pd, os

def tsv_to_md(tsvfile, outdir, category):
    pubs = pd.read_csv(tsvfile, sep="\t", header=0)

    for _, item in pubs.iterrows():
        md_filename = str(item.pub_date) + "-" + item.url_slug + ".md"
        html_filename = str(item.pub_date) + "-" + item.url_slug

        md = "---\n"
        md += f'title: "{item.title}"\n'
        md += "collection: publications\n"
        md += f"category: {category}\n"
        md += f"permalink: /publication/{html_filename}\n"
        if len(str(item.excerpt)) > 5:
            md += f"excerpt: '{item.excerpt}'\n"
        md += f"date: {item.pub_date}\n"
        md += f"venue: '{item.venue}'\n"
        md += f"paperurl: '{item.paper_url}'\n"
        md += f"bibtex_url: '{item.bibtex_url}'\n"
        md += f"citation: '{item.citation}'\n"
        md += "---\n\n"
      #  md += f"Recommended citation: {item.citation}\n"

        os.makedirs(outdir, exist_ok=True)
        with open(os.path.join(outdir, md_filename), "w", encoding="utf-8") as f:
            f.write(md)

# Generate md files with correct category tags
tsv_to_md("publications_journals.tsv", "../_publications/", category="manuscripts")
tsv_to_md("publications_proceedings.tsv", "../_publications/", category="conferences")
