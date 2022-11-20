---
description: Against one's conception
---

# Topic modelling

## The perspective remains alien but interpretable

> _The meanings of words are found in their contexts, and the Ngram Viewer provides only a small peephole into context._&#x20;
>
> _What is needed in order to capture theme are collocations of collocations on a much larger scale._&#x20;
>
> _(Jockers 2013, 148)_

Starting from this considerations we decided to procede with the topic modelling.

> _Topic models are, to use a familiar idiom, the mother of all collocation tools. (Jockers 2013, 148)_

> _Topic models explore and summarize document collections outside the context of any specific information need, when we do not necessarily know what we are looking for. (Boyd-Graber 2017, 21)_

At the very beginning of a data-related work it can be useful first to have some visual rendering of our raw data.

<figure><img src=".gitbook/assets/exploratoryDataAnalysis_entreprecariat.png" alt=""><figcaption><p>Word cloud of the book "Entreprecariat" during the very first exploratory data analysis. Made in voyant-tools.org.</p></figcaption></figure>

A very first close attempt to the book is the word cloud, in which it is possible to see the most frequent word in the entire book, before the preprocessing of its text.

It is remarkable to say that the exploratory data analysis represents an evergreen step, that has been exterted for this research various times not only to have a visual hint, but to compare results from different processes and for mutual counter-proofs.

**\[TOPIC]** Here the "topic" in modelling is to be intended following the statistical meaning of the term, for which a "learning topic hierarchy" consisting in word->topic->document can be obtained through the pipeline described afterwards; hence, we do not define the level of abstraction formally, but we rely on the previous statistical language processing literature to design the aforementioned system.

**\[DYNAMIC]** Furthermore, we'd like to prominently recall the "dynamic" characteristic of topic modelling to linger its generative approach and its keen eye on **innovation-oriented contexts**.

New documents of semantic and syntactic similarity between words are obtained directly from input data and specifically drawn through a dependency structure made available by the word embedding process.

**\[MODELLING]** The real strenght of topic models here relies on "tracking down this otherness hidden in language (and, perhaps, in what language talks about)" (see for more [_Reading Machines_](bibliography.md)).

**\[EDITING AND CURATION]** As a matter of fact, the process aimed to reach the most valuable index of held-out likelihood in order to prevent over/underf fitting. Meaning that we got our hands into practically **tuning the aspects of our interest during coding**. For example, here we don't mean to rely on chapters division based modelling, and we chose to add some nouns into the stop words collections, since it was resulting irrelevant for the initial purpose of the process (see:interactive topic modelling).

**\[AREAS OF POTENTIAL INTEREST]** As stated in the Research Question [chapter](the-project/research-questions.md), we asked ourselves: how can we manage to put a spot on the **neologism**, treating the book as an innovative piece of literature?

While going on with the mainly Python-based practice, we encountered an interesting piece of research from of the most relevant personalities in the field of topic modelling, i.e. professor David Mimno that, together with [other researchers](bibliography.md), explains how topic modeling for scientific papers differs in some ways from that related to fiction books.

The attention towards innovatiove topic is not rarely found in scientific research paper studies- Indeed, in that case it is shed a light on new techniques, new understanding, new terminolgies.

In the era of Fourth Revolution, information is the most important currency, and this can also be read in Entreprecariat, and in other prevident books like the not less famous "The Gutemberg Galaxy" of Marshall McLuhan. &#x20;

To consider the book "Entreprecariat" as a vademecum of the zeitgeist means leafing through it with a look on politics and social life not only of the Western World.

We talked about the possible future imporvements of the projects [here](conclusions.md), but in the meantime it can be stated that **innovation is hard to detect and attribute**. It involves communities, theories and practices and different methods.  We refer to this discourse [here](the-project/introduction.md), too.

**\[CONNECTING THE DOTS]** For what said until now, topic modelling approaches entered the work flow phisiologically, since it is based on the so-called "posterior inference", i.e. a practice clearly based on input data.&#x20;

**The act of inferring here is a pure act of reverse engineering**, than excellent when it comes to connecting the dots between topic models. Finally, we can say that topic modelling is a way of "Operationalising the concept of Distant Reading", or in Moretti's words:

> _**Taking a concept, and transforming it into a series of operations (Moretti, 2013)**_

**\[TECHNICAL DEVELOPMENT]**

**\[THE FRAMEWORK]**






