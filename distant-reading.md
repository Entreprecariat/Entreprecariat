---
description: And Similarity Analysis
---

# Distant reading

**\[DRAFT INTRO]** In "Macroanalysis", Jackers suggests a new approach to computational analysis of texts, based on the concept of distand reading as defined by Franco Moretti.&#x20;

> _This is no longer reading that we are talking about (Jockers 2013, 31)_

The approach of macroanalysis takes inspiration from the difference between "microeconomic" and "macroeconomic", suggesting a quantifiable inspections of big corpora, that allows to capture the main phenomena and tendencies.&#x20;

> _The underlying assumption is that by exploring the literary record writ large, we will better understand the context in which individual texts exist and thereby better understand those individual texts (Jockers 2013, 41)_

Trying to analyse and contextualize "Entreprecariat", the distant reading is a difficult and controversial path, since there is no literature about this new concept and it is difficult to put together and large, but still reliable corpus on the theme.&#x20;

We decided to procede with a semantic analysis of the text, by means of word embeddings, in order to inspect quantified textual data.&#x20;

**\[BASIC CONTEXT ANALYSIS]** Our analysis started from a corpus that could contain the word 'entreprecariat', in which the author is Silvio Lorusso, out of the tweets.&#x20;

We used the Python libraries spacy and gensim to process the text and do the word embeddings.&#x20;

The pipeline we followed in order to pre-process all the texts is the following:&#x20;

* Preprocessing the texts with Spacy&#x20;
* Removing all the stopwords and punctuation
* Sentence recognition
* Word embedding with Word2Vec

**\[SIMILARITY ANALYSIS]** For each word we assigned ten vectors, and from those vectorialization we made the following queries:&#x20;

* Which word is the most similar to entreprecariat?
* Which is the most dissimilar?

```python
from gensim.models import KeyedVectors

wv = KeyedVectors.load("vectors/word2vec.wordvectors", mmap='r')

#SIMILARITIES

print(wv.most_similar(""))

print("The similarity between ----- and ----- is:", wv.similarity("", ""))

#ANALOGY DIFFERENCE

#which word is to A as B is to C?
print(wv.most_similar(positive=["A", "B"], negative=["C"], topn=3))
```
