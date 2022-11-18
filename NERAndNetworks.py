#Import the requisite library
import spacy
import re
import networkx as nx
import matplotlib.pyplot as plt
from fuzzywuzzy.process import dedupe 
import json
from collections import deque
import pandas as pd

def normalize(string):
    text = re.sub(r"\n.*", "", string)
    text = re.sub(r"'s$", "", text)
    return text

directory = "corpus" #insert the name of the directory with the text files (or with folders that contains text files) to process

def retrieveEntities(file, type):
    #Build upon the spaCy Large Model
    nlp = spacy.load("en_core_web_lg")
    #Sample text
    with open (file, "r", encoding="utf-8") as f:
        text = f.read()
    doc = nlp(text)

    person_all = []
    variants = {}

    if type == "PERSON":

        #extract entities
        for ent in doc.ents:
            if ent.label_ == type:
                text = normalize(ent.text)
                person_all.append(text)
        person_cleaned = set(dedupe(person_all))

        for person in person_cleaned: 
            names = person.split(" ")
            for name in names: 
                if name in person_all: 
                    if name not in variants:
                        variants[name] = person

    network = nx.Graph()

    #extract entities
    
    entitiesRating = {}

    for sent in doc.sents:
        entities = deque()
        for ent in sent.ents:
            if ent.label_ == type:
                text = normalize(ent.text)
                if text in variants: 
                    text = variants[text]
                entities.append(text)
                if text not in entitiesRating:
                    entitiesRating[text] = 1
                else: 
                    entitiesRating[text] += 1
        for i in range(len(entities)):
            source = entities.popleft()
            for entity in list(entities): 
                network.add_edge(source, entity)
                entities.append(source)

    nx.draw_spring(network, with_labels = True)
    plt.show()

    #rating of cited entities

    df = pd.DataFrame(list(entitiesRating.items()),columns = ['Entity','Count']).sort_values(by=["Count"], ascending=False)
    plt.barh(df["Entity"].head(10), df["Count"].head(10))

    # setting x-label as entity
    plt.xlabel("OCCURRENCES")
    
    # setting y_label as price
    plt.ylabel(type)  
    plt.title("Horizontal bar graph of entities occurrences")
    plt.show()