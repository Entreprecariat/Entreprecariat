---
description: Actors
---

# Network Analysis

> **Entities** are words in a text that correspond to a specific type of data. They can be _numerical_, such as cardinal numbers; _temporal_, such as dates; _nominal_, such as names of people and places; and _political_, such as geopolitical entities (GPE). In short, an entity can be anything the designer wishes to designate as an item in a text that has a corresponding label. (Mattingly, 2021)

We wanted to inspect the people (nominal entities) involved by Silvio Lorusso in his book, i.e., all the entities related to the world of entreprecariat-ism, by following this workflow:&#x20;

* Tokenization
* POS tagging
* NER recognition

First we extracted all the Named-Entities, by means of the Python library Spacy. We did this for two groups of entities, separately:&#x20;

* People
* Organization

Then, we proceded building a network from the people/organizations who co-occured in the sentences. Lastly, we inspected the most cited people/organizations.

Both the graph visualization and the horizontal bar chart have been produced through the python library matplotlib.&#x20;

