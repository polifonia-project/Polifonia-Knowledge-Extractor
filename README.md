# Polifonia Knowledge Extractor

The Polifonia Knowledge Extractor is a software that allows to extract knowledge from text.
It uses Abstract Meaning Representation (AMR) to parse sentences into semantic graphs and offers the possibility to search within large AMR graph banks.

### Pipeline

The pipeline of the Polifonia Knowledge Extractor is depicted in the figure below.

![pipeline](figs/pipeline.png)

__Step 1 - input__.
The model takes as input a textual corpus.
For our work we used as corpus the **[Polifonia Textual Corpus](https://github.com/polifonia-project/Polifonia-Corpus)** (PTC).

__Step 2 - sampling__.
The large size of the PTC doesn't allow to easily analyze the results of our methodology for knowledge extraction.
For this reason, we decided to conduct our experiments on a sample of the PTC.

__Step 3 - cleaning__.
The PTC contains a large portion of historical documents that have been obtained using Optical Character Recognition technologies.
It thus contains errors that must be corrected in order to avoid parsing inaccuracies.
Furthermore, the PTC contains long documents that cannot be parsed as a whole but have to be split into sentences.
This step leads to possible loss of information especially regarding the use of coreferences.
For this reason, we decided to adopt a coreference resulotion module and to substitute pronouns with actual names.
As coreference resolution module we adopted **[SpaCy neuralcoref](https://spacy.io/universe/project/neuralcoref)**.
We focused only on nouns and pronouns mentioned in a span of 5 sentences.

__Step 3 - parsing__.
Once the sentences have been cleaned and pronouns have been replaced with proper names, it is possible to pass them to an AMR parser.
As AMR parser we used **[SPRING](https://github.com/SapienzaNLP/spring)** to obtain an initial set of AMR graphs from the sampled and preprocessed corpus.

__Step 4 - filtering__.
Given that we are using non standard texts (historical documents) the results of the AMR parser may be inaccurate.
For this reason we decided to use a back-translated approach, that convert the generated graphs back to sentences.
We used SPRING also for this task.
With the back-translated sentences we are in a position to compute similarity scores among the original sentences and the generated ones.
This score serves to determine the quality of the AMR graphs.
The rationale behind this is that if starting from the generted graph, the model is able to produce a sentences that is similar enough to the original sentence this is a signal of the good quality of the graph.
Another, strategy to validate the quality of the AMR graphs consists in the development of a web application that allows human validators to check the correctness of specific portions of the graphs.

__Step 5 - graph bank__.
The final step of our pipeline consist in obtaining a large set of (prosumibly) good quality graphs that can be queried and used in other applciations such as Knowledge Graph construction and/or Question Answering.

## The graph bank