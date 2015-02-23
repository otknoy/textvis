#!/usr/bin/env python
# coding: utf-8
from bottle import route, request, run
import json

import nlp.preprocess


@route('/tokenize', method='POST')
def tokenize():
    text = request.forms.get('text')
    text = nlp.preprocess.normalize(text.decode('utf-8'))
    terms = nlp.preprocess.tokenize(text)
    return json.dumps(terms, ensure_ascii=False)

@route('/test')
def test():
    text = '本日は晴天なり'
    text = nlp.preprocess.normalize(text.decode('utf-8'))
    terms = nlp.preprocess.tokenize(text)
    return json.dumps(terms, ensure_ascii=False)


run(host='localhost', port=8888, debug=True, reloader=True)
