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
**\[FRAMEWORK]** As advanced in [this paper](Maier D, Waldherr A, Miltner P, Wiedemann G, Niekler A, Keinert A, Adam S. Applying LDA topic modeling in communication research: toward a valid and reliable methodology. Commun Methods Meas. 2018;12(2–3):93–118.) and many other resources, the framework here adopted follows a three step pipeline: **pre-processing, topic modelling, and post-processing**, where the topic model Latent Dirichlet Allocation (unsupervised machine-learning model) is used, enriched by the Mallet TM library.
Transparency and reliability to exploit the hidden semantic structure in documents has been provided through the fine tuning of the parameters, set by subjective decision. It is important to state here that the LDA algorithm is stochastic, hence the corpus has been associated to 4 topics, each of which has generated 25 words, taken from the corpus itself.
--The surfaced topics These  ‘hidden’ topics are then surfaced based on the likelihood of word co-occurrence-

**\[DYNAMIC]** Furthermore, we'd like to prominently recall the "dynamic" characteristic of topic modelling to linger its generative approach and its keen eye on **innovation-oriented contexts**. Parliamo dei futri development qui

New documents of semantic and syntactic similarity between words are obtained directly from input data and specifically drawn through a dependency structure made available by the word embedding process. In this sense, the Topic Modelling pipeline includes the following corpus:

- Foti, A., General Theory of the Precariat: Great Recession, Revolution, Reaction, Institute of Network Cultures, 2017
- Lorusso, S., "On “Fuck You Startup World” and Entreprecariat at Large. We're all Richard", www.networkcultures.org, last checked: 20/11/2022
- Lorusso, S., "Entreprecariat: Everyone Is an Entrepreneur. Nobody Is Safe.", Onomatopee, 2018
- Barton, G., "Don't Get a Job... Make a Job. How to Make It As a Creative Graduage", Laurence King, 2016
- Berardi, F., "Precarious Rhapsody: Semiocapitalism and the Pathologies of Post-Alpha Generation", Autonomedia, 2009
- Bröckling U., "The Entrepreneurial Self. Fabricating a New Type of Subject", Translated by Steven Black, SAGE Publications, 2015
- Standing, G., "The Precariat: The New Dangerous Class", Bloomsbury USA Academic, 2014
- Scholz, T., "Uberworked and Underpaid: How Workers Are Disrupting the Digital Economy"

**\[MODELLING]** The real strenght of topic models here relies on "tracking down this otherness hidden in language (and, perhaps, in what language talks about)" (see for more [_Reading Machines_](bibliography.md)). Through a careful job of fine tuning, **4 topics** have been retrieved from the analysis (rif: fine tuning pieces in articles to copy and remix here).

**\[EDITING AND CURATION]** As a matter of fact, the process aimed to reach the most valuable index of held-out likelihood in order to prevent over/underf fitting. Meaning that we got our hands into practically **tuning the aspects of our interest during coding**. For example, here we don't mean to rely on chapters division based modelling, and we chose to add some nouns into the stop words collections, since it was resulting irrelevant for the initial purpose of the process (see:interactive topic modelling).

**\[AREAS OF POTENTIAL INTEREST]** As stated in the Research Question [chapter](the-project/research-questions.md), we asked ourselves: how can we manage to put a spot on the **neologism**, treating the book as an innovative piece of literature?

While going on with the mainly Python-based practice, we encountered an interesting piece of research from of the most relevant personalities in the field of topic modelling, i.e. professor David Mimno that, together with [other researchers](bibliography.md), explains how topic modeling for scientific papers differs in some ways from that related to fiction books.

Indeed, the attention towards innovative topic is not rarely found in scientific research paper studies; in that case it is shed a light on new techniques, new understanding, new terminologies.

In the era of Fourth Revolution, information is the most important currency, and this can also be read in Entreprecariat, and in other prevident books like the not less famous "The Gutemberg Galaxy" of Marshall McLuhan. &#x20;

**To consider the book "Entreprecariat" as a vademecum of the zeitgeist means leafing through it with a look on politics and social life not only of the Western World.

We talked about the possible future imporvements of the projects [here](conclusions.md), but in the meantime it can be stated that **innovation is hard to detect and attribute**. It involves communities, theories and practices and different methods.  We make this discourse [here](the-project/introduction.md), too.

**\[CONNECTING THE DOTS]** For what said until now, topic modelling approaches entered the work flow phisiologically, since it is based on the so-called "posterior inference", i.e. a practice clearly based on input data.&#x20;

**The act of inferring here is a pure act of reverse engineering**, than excellent when it comes to connecting the dots between topic models. Finally, we can say that topic modelling is a way of "Operationalising the concept of Distant Reading", or in Moretti's words:

> _**Taking a concept, and transforming it into a series of operations (Moretti, 2013)**_




