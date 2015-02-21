#!/usr/bin/env python
import math
from util import uniq

def term_frequency(terms, normalize=False):
    """
    normalize: Harman
    """
    tf = {}
    for t in terms:
        if not tf.has_key(t):
            tf[t] = 0
        tf[t] += 1
    if normalize:
        for t, f in tf.items():
            tf[t] = math.log(tf[t] + 1) / math.log(len(terms))
    return tf

def document_frequency(docs):
    df = {}
    for terms in docs:
        for t in uniq(terms):
            if not df.has_key(t):
                df[t] = 0
            df[t] += 1
    return df

def inverse_document_frequency(docs, normalize=False):
    """
    normalize: Sparck Jones
    """
    df = document_frequency(docs)
    n = len(docs)
    idf = {}
    for t in df.keys():
        if normalize:
            idf[t] = math.log(float(n)/df[t])+1
        else:
            idf[t] = 1.0/df[t]
    return idf

def tf_idf(docs, normalize=False):
    tfidf_list = []
    idf = inverse_document_frequency(docs, normalize=normalize)
    for terms in docs:
        tf = term_frequency(terms, normalize=normalize)
        tfidf = {}
        for t in idf.keys():
            if not tf.has_key(t):
                tfidf[t] = 0.0
            else: 
                tfidf[t] = tf[t] * idf[t]
        tfidf_list.append(tfidf)
    return tfidf_list

if __name__ == '__main__':
    import corpus
    from preprocess import tokenize 
    from util import flatten

    def print_dict(d):
        print "{%s}" % ', '.join(["%s: %f" % (k, v) for k, v in d.items()])

    texts = [tokenize(text) for text in corpus.texts[:3]]

    # tf
    print 'Term Frequency'
    text = flatten(texts)
    print_dict(term_frequency(text))
    print_dict(term_frequency(text, normalize=True))
    print 

    # df
    print 'Document Frequency'
    print_dict(document_frequency(texts))
    print

    # idf
    print 'Inverse Document Frequency'
    print_dict(inverse_document_frequency(texts))
    print_dict(inverse_document_frequency(texts, normalize=True))
    print


    def print_array_of_dict(a):
        for d in a:
            print_dict(d)

    # tfidf
    print 'TFIDF'
    print_array_of_dict(tf_idf(texts))
    print 'TFIDF (normalized)'
    print_array_of_dict(tf_idf(texts, normalize=True))
