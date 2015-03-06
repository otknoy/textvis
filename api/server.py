#!/usr/bin/env python
# coding: utf-8
from bottle import hook, response, route, request, run
import json

import nlp.preprocess
from nlp.vector_space_model import term_frequency, tf_idf


@hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'

@route('/tokenize')
def tokenize():
    text = request.query.get('text')
    text = nlp.preprocess.normalize(text.decode('utf-8'))
    terms = nlp.preprocess.tokenize(text)
    return json.dumps(terms, ensure_ascii=False)

@route('/tf')
def tf():
    terms = json.loads(request.query.get('terms'))
    tf = term_frequency(terms, normalize=True)
    return json.dumps(tf, ensure_ascii=False)

@route('/tfidf')
def tfidf():
    docs = json.loads(request.query.get('docs'))
    tfidf_list = tfidf(docs, normalize=True);
    return json.dumps(tfidf_list, ensure_ascii=False)


run(host='localhost', port=8888, debug=True, reloader=True)
