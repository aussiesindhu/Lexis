QA-Approach-Wiki : Its a different question answering system using Wikipedia as the database for comparing results with the Lexis. 


All files in this folder were used in the above task and written by Bhavnit Kaur.

1. Steps with StanfordNLP.txt  :  contains the steps to follow for configuring and running Stanford CoreNLP.

2. Scraping2.py  – get all the links in the websites("http://www.50states.com/facts/”) for all the 50 states of US.

3. get.py :  to get the facts for each of the state and stored in a text file by giving input file as the output of the above script(Scraping2.py).

4. wiki.py : to get data from wikipedia in small chunks[first paragraph] related to a query. Used wiki2plain.py and wikipedia.py as references python files.

5. pynlp.py : to implement Coreference resolution. 
