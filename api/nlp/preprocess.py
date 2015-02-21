#!/usr/bin/env python
# coding: utf-8
import MeCab
import unicodedata

def normalize(text):
    return unicodedata.normalize('NFKC', text)

def tokenize(s):
    '''
    Morphological analysis using MeCab
    '''
    u = s.encode('utf-8')
    m = MeCab.Tagger()
    node = m.parseToNode(u)

    terms = []
    while node:
        surface = node.surface.decode('utf-8')
        features = node.feature.decode('utf-8').split(u',')
        basic_form = features[6]
        if basic_form == u'*':
            basic_form = surface
        posid = node.posid

        terms.append(basic_form)

        node = node.next

    return terms[1:-1]


if __name__ == '__main__':
    import corpus
    
    # tokenize
    for text in corpus.texts:
        terms = tokenize(text)
        print text
        print ' '.join(terms)

    
    # unicode nomalization
    t = u'ＥＭＡＣＳ'
    print t
    print normalize(t)
