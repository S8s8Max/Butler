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
    pke.base.lang_stopwords["ja_ginza"] = "japanese"
    spacy_model = spacy.load("ja_ginza")
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

    # Change a number of 'key_phrase' according to the length of the input text.
    if len(text) < 10:
        phrase_num = 1
    elif len(text) >= 10 and len(text) < 30:
        phrase_num = 2
    elif len(text) >= 30 and len(text) < 50:
        phrase_num = 3
    else:
        phrase_num = 4

    key_phrases = extractor.get_n_best(n=phrase_num)

    # "memo" won't be included.
    targets = []
    for phrase in key_phrases:
        if phrase[0] == "memo":
            continue
        else:
            targets.append(phrase[0])

    return targets
