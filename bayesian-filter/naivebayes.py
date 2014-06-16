# -*- coding: utf-8 -*-
import math
import sys

import morphological

class NaiveBayse:
    def __init__(self):
        self.vocabularies = set()
        self.wordcount = {}
        self.catcount = {}

    def wordcountup(self, word, cat):
        self.wordcount.setdefault(cat, {})
        self.wordcount[cat].setdefault(word, 0)
        self.wordcount[cat][word] += 1
        self.vocabularies.add(word)

    def catcountup(self, cat):
        self.catcount.setdefault(cat, 0)
        self.catcount[cat] += 1

    def train(self, doc, cat):
        word = getwords(doc)
        for w in word:
            self.wordcountup(w, cat)
        self.catcountup(cat)
        
def getwords(doc):
    words = [s.lower() for s in morphological.split(doc)]
    return  tuple(w for w in words)



