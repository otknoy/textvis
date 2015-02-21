#!/usr/bin/env python
# coding: utf-8
from nlp.corpus import texts
import nlp.preprocess as preprocess

docs = []
for text in texts:
    text = preprocess.normalize(text)
    terms = preprocess.tokenize(text)
    docs.append(terms)


import cgi
import cgitb
cgitb.enable()

import json
# form = cgi.FieldStorage()
print json.dumps(docs, ensure_ascii=False)



