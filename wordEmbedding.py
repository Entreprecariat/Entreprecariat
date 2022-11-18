import os
import re
import spacy
from gensim.models.word2vec import Word2Vec
from gensim.models.phrases import Phrases, Phraser
from gensim.test.utils import datapath
from collections import defaultdict
import pandas as pd

def removePunctuation(text):  
    text = re.sub("[\.:;?!~,`\"|()<>\{\}\[\]_—'…%$/#]", " ", text) #except - since words like co-occurrence etc. must not be separated
    return text

def clean_text(text): 
    text = re.sub("\s?I+\.I*\s", "", text)
    
    stopwords = ["i","me","my","myself","we","our","ours", "us", "ourselves","you","your","yours","yourself","yourselves",
                "he", "hes", "him","his","himself","she", "shes", "her","hers","herself","it", "its","itself","they", "theyre", "them","their",
                "theirs","themselves","what","which","who", "whos", "whom","this","that","thats", "these","those","am","is", "isnt", "are", "arent", "was",
                "were", "wasnt", "werent", "be","been","being","have","has","had", "hadnt", "havent", "hasnt", "having","do","does","did", "dont", "doesnt", "didnt", "doing","a","an","the","and",
                "but","if","or","because","as","until","while","of","at","by","for","with","about","against","between",
                "into","through","during","before","after","above","below","to","from","up","down","in","out","on","off",
                "over","under","again","further","then","once","here","there","when","where","why","how","all","any","both",
                "each","few","more","most","other","some","such","no","nor","not","only","own","same","so","than","too","very",
                "s","t", "can", "cant", "cannot", "could", "couldnt", "will", "wont", "would", "wouldnt", "just","don","should", "shouldnt", "now", "etc", "id", "im", "ie", "oh", "&", "vs", "d", "ve"
                ]

    text = text.lower()
    words = text.split()

    new_text = []
    for word in words:
        wordToCheck = removePunctuation(word)
        wordToCheck = wordToCheck.replace(" ", "")
        if wordToCheck not in stopwords:
            new_text.append(word)

    text = " ".join(new_text)

    return text


def clean_tweet(tweet):
    emoji_pattern = re.compile("["
            u"\U0001F600-\U0001F64F"  # emoticons
            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            u"\U0001F680-\U0001F6FF"  # transport & map symbols
            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                            "]+", flags=re.UNICODE)
    tweet = emoji_pattern.sub(r'', tweet) # no emoji
    plainText = re.sub(r"https:\/\/t\.co\/.*", " ", tweet)
    plainText = plainText.replace("RT ", " ")
    return plainText


def create_sentences(processedText, filename):
            
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(processedText)

    sentences = []

    for sent in doc.sents:
        sentence = sent.text
        sentence = removePunctuation(sentence)

        #manage all the exceptions
        sentence = re.sub("[0-9]+(?!d\s|s)[\s$]", "", sentence)
        sentence = re.sub(" s ", " ", sentence) #it remains both in gerundive ('s) and decades (e.g. 90s)
        sentence = re.sub("f lux", "f.lux", sentence)
        sentence = re.sub(" w o ", " without ", sentence)
        sentence = re.sub("personalexcellence co", " personalexcellence.co ", sentence)
        sentence = re.sub("o neil ", " O'Neil ", sentence) #O'Neil and Chelsy O are the only case of 'o' alone
        sentence = re.sub(" o ", "Odunu", sentence) #taking for granted that Chelsy O is Chelsea Odunu, the error comes from the author, we decide to manage it like this
        sentence = re.sub(" ll ", " ", sentence) #contracted will cannot be managed otherwise since I'll lowecase and without punctuation e.g. would be ill and it is also a word
        sentence = re.sub(" a b ", " a/b ", sentence) #it's the a/b test -> or just "" to avoid overfitting
        sentence = re.sub(" j g ", "", sentence) #it's j.g. a name abbreviation
        sentence = re.sub(" e j ", "", sentence) #it's e.j. a name abbreviation
        sentence = re.sub(" j l ", "", sentence) #it's j.l. a name abbreviation -> those must be substituted with the extended version
        sentence = re.sub(" r ", "", sentence) #it's R60/2 the model of BMW
        words = sentence.split()
        sentences.append(words)

    return sentences

def wordEmbedding(directory):
    AllSentences = []
    for folder in os.listdir(directory):
        path = os.path.join(directory, folder)
        for filename in os.listdir(path):
            text = os.path.join(path, filename)
            if os.path.isfile(text):  
                if text[-3:] == "csv":
                    file = pd.read_csv(text)
                    tweets = file["Tweet"]
                    sentences = []
                    for tweet in tweets:
                        plainText = clean_tweet(tweet)
                        processedText = clean_text(plainText)
                        sentence = removePunctuation(processedText)
                        sentences.append(sentence)
                    AllSentences.extend(sentences)
                else:
                    with open (text, "r", encoding="utf-8") as f:
                        text = f.read()
                    processedText = clean_text(text)
                    sentences = create_sentences(processedText, filename)
                    AllSentences.extend(sentences)

    phrases = Phrases(AllSentences, min_count=30, progress_per=10000)
    
    bigram = Phraser(phrases)
    
    sentences = phrases[AllSentences]
    word_freq = defaultdict(int)

    for sent in sentences:
        for i in sent:
            word_freq[i]+=1
    
    print ("Training model now...")
    w2v_model = Word2Vec(bigram[AllSentences],
                        min_count=1,
                        window=2,
                        vector_size=10,
                        sample=6e-5,
                        alpha=0.03,
                        min_alpha=0.0007,
                        negative=20)
    w2v_model.build_vocab(sentences, progress_per=10000)
    w2v_model.train(sentences, total_examples=w2v_model.corpus_count, epochs=30, report_delay=1)
    word_vectors = w2v_model.wv
    word_vectors.save("vectors/word2vec.wordvectors")

directory = 'corpus'
print(wordEmbedding(directory))