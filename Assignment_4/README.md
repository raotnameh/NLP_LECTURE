###### Tested on python 3.6

##### quesiton.pdf has the questions for this assignment.

```
 assignment_4.ipynb: Python based script for the assignment 4.
 
 save/: contains the saved models and saved L1 for both glove and word2vec (w2v) embeddings. unzip save/save.zip.
 data/: put all the required dataset in this directory.
```

1. English-Hindi versiono f BingLiu lexicon L1 is save at save/L1.txt.
2. Two monolingual (word2vec and glove) word embedding of dimension 100 and word contexxt equals to 5. One for English and another for Hindi is saved at save/w2v_{eng/hindi}.model and save/{eng/hindi}vectors.txt. 
3. assignment_4.ipynb has all the code to find out 5 closest words each in the word-embedding space, i.e., five closest words of 'good' in the English word embedding model and five closest words of 'अछा' in Hindi word embedding.
4. assignment_4.ipynb has all the code: if a word in English closest list can be mapped to a word in the Hindi closest list using the bilingual dictionary, then add this pair to list L1.

> Using word2vec we were able to add 5 new words to the L1.txt and the updated L1 file is saved at save/w2v_L1.txt. The new 5 words are:
>>life जीवन, big बड़ा, very बहुत, display प्रदर्शन, wont नहीं.

> Using glove we were able to add 2 new words to the L1.txt and the updated L1 file is saved at save/glove_L1.txt. The new 5 words are:
>> data डेटा, offline ऑफ़लाइन


- For any queries please contact: hemantya@iiitd.ac.in

