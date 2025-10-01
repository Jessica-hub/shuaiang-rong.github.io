
# coding: utf-8

# # Publications markdown generator for academicpages
# 
# Takes a TSV of publications with metadata and converts them for use with [academicpages.github.io](academicpages.github.io). This is an interactive Jupyter notebook, with the core python code in publications.py. Run either from the `markdown_generator` folder after replacing `publications.tsv` with one that fits your format.
# 
# TODO: Make this work with BibTex and other databases of citations, rather than Stuart's non-standard TSV format and citation style.
# 

# ## Data format
# 
# The TSV needs to have the following columns: pub_date, title, venue, excerpt, citation, site_url, and paper_url, with a header at the top. 
# 
# - `excerpt` and `paper_url` can be blank, but the others must have values. 
# - `pub_date` must be formatted as YYYY-MM-DD.
# - `url_slug` will be the descriptive part of the .md file and the permalink URL for the page about the paper. The .md file will be `YYYY-MM-DD-[url_slug].md` and the permalink will be `https://[yourdomain]/publications/YYYY-MM-DD-[url_slug]`


# ## Import pandas
# 
# We are using the very handy pandas library for dataframes.

# In[2]:
import pandas as pd
import os

# -------------------
# 1. Load TSV
# -------------------
publications = pd.read_csv("publications.tsv", sep="\t", header=0)

# -------------------
# 2. Escape for YAML
# -------------------
html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
}

def html_escape(text):
    """Safely escape special chars for YAML/HTML"""
    if pd.isna(text) or text is None:
        return ""
    text = str(text)
    return "".join(html_escape_table.get(c, c) for c in text)

# -------------------
# 3. Generate Markdown files
# -------------------
for _, item in publications.iterrows():
    pub_date = str(item.pub_date) if not pd.isna(item.pub_date) else "1900-01-01"
    url_slug = str(item.url_slug) if not pd.isna(item.url_slug) else "untitled"

    md_filename = f"{pub_date}-{url_slug}.md"
    html_filename = f"{pub_date}-{url_slug}"
    year = pub_date[:4]

    # YAML frontmatter
    md = "---\n"
    md += f'title: "{html_escape(item.title)}"\n'

    # Use category from TSV if exists, else default
    category = item.get("category", "manuscripts")
    if pd.isna(category) or category == "":
        category = "manuscripts"
    md += f"collection: {category}\n"

    md += f"permalink: /publication/{html_filename}\n"

    if not pd.isna(item.excerpt) and len(str(item.excerpt)) > 5:
        md += f"excerpt: '{html_escape(item.excerpt)}'\n"

    md += f"date: {pub_date}\n"
    md += f"venue: '{html_escape(item.venue)}'\n"

    if not pd.isna(item.paper_url) and len(str(item.paper_url)) > 5:
        md += f"paperurl: '{item.paper_url}'\n"

    md += f"citation: '{html_escape(item.citation)}'\n"
    md += "---\n"

    # -------------------
    # Body Content
    # -------------------
    if not pd.isna(item.paper_url) and len(str(item.paper_url)) > 5:
        md += f"\n<a href='{item.paper_url}'>Download paper here</a>\n"

    if not pd.isna(item.slides_url) and len(str(item.slides_url)) > 5:
        md += f"\n<a href='{item.slides_url}'>Slides</a>\n"

    if not pd.isna(item.excerpt) and len(str(item.excerpt)) > 5:
        md += "\n" + html_escape(item.excerpt) + "\n"

    md += "\nRecommended citation: " + html_escape(item.citation)

    # -------------------
    # Save File
    # -------------------
    os.makedirs("../_publications", exist_ok=True)
    with open(os.path.join("../_publications", md_filename), "w", encoding="utf-8") as f:
        f.write(md)

    print(f"✔ Created {md_filename}")
