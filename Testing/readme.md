Testing and Evaluation of LEXIS !

All files in this folder are written by Sindhu Mukunda.

##testcases.txt
This file contains all the 20 questions that were used to test LEXIS against 3 other 
Chatbots : pandorabot, cleverblt and aztekium
The same set of questions are used to test Sphynx speech recogniton model as well as QA approach- Wiki

##word_error_rate.txt
This file contains the code to calculate the error rate associated wth each word in a sentence.
Error rate = (Substitutions + Insertions + Deletions) / Number of words
This is used for the speech recognition model , where we are trying to calculate the average error rate of a input question recognition.
Accuracy = 1- word error rate
