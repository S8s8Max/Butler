# -*- coding: utf-8 -*-
import sys
import pke
import ginza
import nltk
import spacy
from spacy.lang.ja import stop_words

def NLP(text: str) -> str:
    """
    １、引数のテキストからキーフレーズを抽出。
    ２、上位三つをリターンする。
    """
    ### Initialization ###
    nltk.download('stopwords')
    pke.base.lang_stopwords["ja_ginza"] = "japanese"
    spacy_model = spacy.load("ja_ginza")
    print(spacy_model)
    stopwords = list(stop_words.STOP_WORDS)
    nltk.corpus.stopwords.words_org = nltk.corpus.stopwords.words
    nltk.corpus.stopwords.words = lambda lang : stopwords if lang == 'japanese' else nltk.corpus.stopwords.words_org(lang)
    ### Initialization ###

    extractor = pke.unsupervised.MultipartiteRank()
    extractor.load_document(
        input=text,
        language="ja_ginza",
        normalization=None,
        spacy_model=spacy_model
    )
    extractor.candidate_selection(pos={"NOUN","PROPN","ADJ","NUM"})
    extractor.candidate_weighting(threshold=0.74, method="average", alpha=1.1)

    key_phrases = extractor.get_n_best(n=3)

    targets = []
    for phrase in key_phrases:
        targets.append(phrase[0])

    return targets
