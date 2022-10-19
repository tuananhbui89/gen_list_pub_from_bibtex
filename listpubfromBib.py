#!/usr/bin/env python
# coding: utf-8


""" Publications markdown generator for academicpages
Takes a set of bibtex of publications and converts them to markdown for use in a personal website  

Ref: this code has been strongly copied from academicpages.github.io

    AUTHORS_LINK: dictionary of authors (first_name last_name) with link to their webpage. to add hyperlink to author. 
    HIGHLIGHT_NAME: list of authors name (your name in Bibtex) to be highlighted (i.e., Bold) when showing. 

Requires (either)
    proceedings.bib: file that contains your conference papers
    pubs.bib: file that contains your journals paper 
"""

from pybtex.database.input import bibtex
from time import strptime
import os
import numpy as np 
import math 

ADD_FIELDS = [
            "paper", 
            "code", 
            "poster", 
            "presentation"]

HIGHLIGHT_NAME = [
    "Anh Bui", 
    "Tuan-Anh Bui",
]

AUTHORS_LINK = {
    "Anh Bui": 'https://tuananhbui89.github.io/', 
    "Tuan-Anh Bui": 'https://tuananhbui89.github.io/', 
    "Trung Le": 'https://scholar.google.com/citations?user=gysdMxwAAAAJ&hl=en',
    "Dinh Phung": 'http://dinhphung.ml/',
    "He Zhao": 'https://ethanhezhao.github.io/', 
    "Ngai-Man Cheung": 'https://sites.google.com/site/mancheung0407/', 
    "Ngoc-Trung Tran": 'https://scholar.google.com/citations?user=9SE3GYMAAAAJ&hl=en',
}

#todo: incorporate different collection types rather than a catch all publications, requires other changes to template
publist = {
    "proceeding": {
        "file" : "proceedings.bib",
        "venuekey": "booktitle",
        "venue-pretext": "In the proceedings of ",
        "collection" : {"name":"publications",
                        "permalink":"/publication/"}
        
    },
    "journal":{
        "file": "pubs.bib",
        "venuekey" : "journal",
        "venue-pretext" : "",
        "collection" : {"name":"publications",
                        "permalink":"/publication/"}
    } 
}

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
    }

def html_escape(text):
    """Produce entities within text."""
    return "".join(html_escape_table.get(c,c) for c in text)


def standardize_bib(b): 

    for f in ADD_FIELDS: 
        if f not in b: 
            b[f] = ""
    
    if "booktitle" not in b: 
        b["booktitle"] = b["journal"] if b["journal"] else ""

    return b 

def highlight_author(author):
    writestr = author
    if author in AUTHORS_LINK:
        if author in HIGHLIGHT_NAME:
            writestr = "[**{}**]({})".format(author, AUTHORS_LINK[author])
        else: 
            writestr = "[{}]({})".format(author, AUTHORS_LINK[author])
    return writestr


def isnan(x):
    if type(x) is str: 
        return x is np.nan
    else: 
        return math.isnan(x)

def isvalid(x): 
    if x == "": 
        return False 
    else: 
        return not isnan(x)

# Write to only one mb file 

with open("list_pub.md", 'w') as f:
    for pubsource in publist:
        parser = bibtex.Parser()
        
        if not os.path.exists(publist[pubsource]["file"]):
            continue
        bibdata = parser.parse_file(publist[pubsource]["file"])

        #loop through the individual references in a given bibtex file
        for id, bib_id in enumerate(bibdata.entries):
            #reset default date
            pub_year = "1900"
            pub_month = "01"
            pub_day = "01"
            
            b = bibdata.entries[bib_id].fields

            b = standardize_bib(b)
            print('-----------')
            print(b.keys)
            print('-----------')

            #Build Citation from text
            citation = ""

            #citation authors - todo - add highlighting for primary author?
            for author in bibdata.entries[bib_id].persons["author"]:
                citation = citation + " " +\
                    highlight_author(author.first_names[0] + " " + author.last_names[0]) +\
                     ", "

            writestr = "\n[{}] {}'{}', {}, {}.".format(
                id+1, citation, b["title"], b["booktitle"], b["year"]
            )
            
            for k in ADD_FIELDS: 
                if isvalid(b[k]): 
                    writestr += ' [{}]({})'.format(k, b[k])

            writestr += '<br>'
            f.write(writestr)
            print(writestr)