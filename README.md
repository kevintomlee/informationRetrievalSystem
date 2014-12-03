informationRetrievalSystem
==========================

A simple implementation of an Enligsh text retrieval system

Indexer.py:
This file does the indexing:
It tokenizes each document(no special heuristic is used yet, for the momen it just break the document by space)
and build term, posting pair and store them in a dictionary and is eventually stored in a file on hard disk.
The format of the dictionary is:
term1 : [[tf,doc1], [tf,doc2], ...]
term2 : ...
This file also stores the total number of documents which is used to calculate the idf(inverse document frequency)

Retriever.py:
This file does the retriving:
It reads the index file, and the query, process the query and produce a query vector.
It calculates the cosine similarity between each document and the query and store the scores in a ordered list.
