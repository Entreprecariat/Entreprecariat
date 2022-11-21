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

<figure><img src=".gitbook/assets/Entreprecariat_TopicDetection_LDA_Mallet.JPG"><figcaption><p>Word cloud of the book "Entreprecariat" during the very first exploratory data analysis. Made in voyant-tools.org.</p></figcaption></figure>

A very first close attempt to the book is the word cloud, in which it is possible to see the most frequent word in the entire book, before the preprocessing of its text.

It is remarkable to say that the exploratory data analysis represents an evergreen step, that has been exterted for this research various times not only to have a visual hint, but to compare results from different processes and for mutual counter-proofs.

**\[TOPIC]** Here the "topic" in modelling is to be intended following the statistical meaning of the term, for which a "learning topic hierarchy" consisting in word->topic->document can be obtained through the pipeline described afterwards; hence, we do not define the level of abstraction formally, but we rely on the previous statistical language processing literature to design the aforementioned system.
**\[FRAMEWORK]** As advanced in [this paper](Maier D, Waldherr A, Miltner P, Wiedemann G, Niekler A, Keinert A, Adam S. Applying LDA topic modeling in communication research: toward a valid and reliable methodology. Commun Methods Meas. 2018;12(2–3):93–118.) and many other resources, the framework here adopted follows a three step pipeline: **pre-processing, topic modelling, and post-processing**, where the topic model Latent Dirichlet Allocation (unsupervised machine-learning model) is used, enriched by the Mallet TM library.
Transparency and reliability to exploit the hidden semantic structure in documents has been provided through the fine tuning of the parameters, set by subjective decision. It is important to state here that the LDA algorithm is stochastic, hence the corpus has been associated to 4 topics, each of which has generated 25 words, taken from the corpus itself.
<figure><img src="../.gitbook/assets/Entreprecariat_TopicDetection_LDA_Mallet.jpg" alt=""><figcaption><p>KNIME pipeline for topic detection. Here the grey nodes (i.e. modules) inglobe the preprocessing structure</p></figcaption></figure>

**\[DYNAMIC]** Furthermore, we'd like to prominently recall the "dynamic" characteristic of topic modelling to linger its generative approach and its keen eye on **innovation-oriented contexts**.

New documents of semantic and syntactic similarity between words are obtained directly from input data and specifically drawn through a dependency structure made available by the [word embedding process](wordEmbedding.py). In this sense, the Topic Modelling pipeline includes the following corpus:

- Foti, A., General Theory of the Precariat: Great Recession, Revolution, Reaction, Institute of Network Cultures, 2017
- Lorusso, S., "On “Fuck You Startup World” and Entreprecariat at Large. We're all Richard", www.networkcultures.org, last checked: 20/11/2022
- Lorusso, S., "Entreprecariat: Everyone Is an Entrepreneur. Nobody Is Safe.", Onomatopee, 2018
- Barton, G., "Don't Get a Job... Make a Job. How to Make It As a Creative Graduage", Laurence King, 2016
- Berardi, F., "Precarious Rhapsody: Semiocapitalism and the Pathologies of Post-Alpha Generation", Autonomedia, 2009
- Bröckling U., "The Entrepreneurial Self. Fabricating a New Type of Subject", Translated by Steven Black, SAGE Publications, 2015
- Standing, G., "The Precariat: The New Dangerous Class", Bloomsbury USA Academic, 2014
- Scholz, T., "Uberworked and Underpaid: How Workers Are Disrupting the Digital Economy"

**\[MODELLING]** The real strenght of topic models here relies on "tracking down this otherness hidden in language (and, perhaps, in what language talks about)" ([_Reading Machines_](bibliography.md)). Through a careful job of fine tuning, **5 topics** have been retrieved from the analysis. Though has been decided to mantain certin words in more than one topic, to avoid a large number of repetitions the preprocessing has been enriched making some tests in lemmatizing and stemming of the documents.

Technical Specifications:
No. of topics: 5
No. of words per topic: 25
Alpha: 0,4
Beta: 0,1
No. of iterations: 2000
No. of threads: 8

<figure><img src=".gitbook/assets/Entreprecariat_BagOfWords_TM.JPG"><figcaption><p>Word cloud obtained from the Topic Detection</p></figcaption></figure>

**\[EDITING AND CURATION]** As a matter of fact, the process aimed to reach the most valuable index of held-out likelihood in order to prevent over/underf fitting. Meaning that we got our hands into practically **tuning the aspects of our interest trhough the whole pipeline**. For example, here we don't mean to rely on chapters division based modelling, and we chose to add some nouns into the stop words collections, since it was resulting irrelevant for the initial purpose of the process (see for more [here](https://link.springer.com/article/10.1007/s10994-013-5413-0)). 


Topics have been detected as follows:
- Topic_0: POLICY
- Topic_1: SHARING_ECONOMY
- Topic_2: ENTREPRECARIAT_LIFE
- Topic_3: CAPITALISM_CRISIS
- Topic_4: ZEITGEIST

Words per topic:

*Topic_0*

labour | 
social | 
country | 
benefit | 
migrant | 
society | 
cent | 
security | 
firm | 
woman | 
temporary | 
rights | 
public | 
wages | 
cost | 
form | 
service | 
million | 
global | 
grow | 
move | 
policy | 
status | 
call | 
age | 

*Topic_1*

platform | 
digital | 
company | 
internet | 
datum | 
user | 
service | 
write | 
online | 
social | 
call | 
exploitation | 
value | 
media | 
design | 
cooperative | 
start | 
crowd | 
book | 
chapter | 
business | 
site | 
day | 
share | 
term | 

*Topic_2*

project  | 
individual | 
self | 
social | 
creative | 
human | 
power | 
subject | 
quality | 
contract | 
management | 
form | 
theory | 
practice | 
experience | 
model | 
idea | 
force | 
mean | 
action | 
sense | 
competition | 
follow | 
success | 

*Topic_3*

social | 
europe | 
union | 
america | 
precarity | 
power | 
neoliberalism | 
global | 
recession | 
unemployment | 
revolution | 
rate | 
financial | 
populism | 
democracy | 
wage | 
capitalist | 
green | 
form | 
war | 
basic | 
defeat | 
demand | 
lead | 
national | 

*Topic_4*

social | 
process | 
human | 
cognitive | 
form | 
mind | 
effect | 
intellectual | 
depression | 
century 
body | 
power | 
production | 
attention | 
war | 
sign | 
condition | 
organism | 
capitalist | 
information | 
knowledge | 
word | 
productive | 
sphere | 
desire | 


--
**\[AREAS OF POTENTIAL INTEREST]** As stated in the Research Question [chapter](the-project/research-questions.md), we asked ourselves: how can we manage to put a spot on the **neologism**, treating the book as an innovative piece of literature?

While going on with through the work practice, we encountered an interesting piece of research from of the most relevant personalities in the field of topic modelling, i.e. professor David Mimno that, together with [other researchers](bibliography.md), explains how topic modeling for scientific papers differs in some ways from that related to fiction books.

Indeed, the attention towards innovative topic is not rarely found in scientific research paper studies; in that case it is shed a light on new techniques, new understanding, new terminologies provided by the text.

**To consider the book "Entreprecariat" as a vademecum of the zeitgeist means leafing through it with a look on politics and social life not only of the Western World.

We talked about the possible future imporvements of the projects [here](conclusions.md), but in the meantime it can be stated that **innovation is hard to detect and attribute**. It involves *communities, theories and practices and different methods.*  We make this discourse [here](the-project/introduction.md), too.

**\[CONNECTING THE DOTS]** For what said until now, topic modelling approaches entered the work flow phisiologically, since it is based on the so-called "posterior inference", i.e. a practice clearly based on input data.&#x20;

**The act of inferring here is a pure act of reverse engineering**, than excellent when it comes to connecting the dots between topic models. Finally, we can say that topic modelling is a way of "Operationalising the concept of Distant Reading" ([Applications of Topic Models](bibliography.md)), or in Moretti's words:

> _**Taking a concept, and transforming it into a series of operations (Moretti, 2013)**_




