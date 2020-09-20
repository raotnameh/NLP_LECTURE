###### Tested on python 3.6

- To install the dependencies run
```
 pip install -r requirements.txt
```

Assumptions: 
1. To preprocess the input text file, first we split it in terms of paragraph if any (i.e., split on a '\n\n' symbol) and then apply sent\_tokenize on it. It worked better than just using the sent\_tokenize alone on the input text file.

2. word\_tokenize is used to split the sentences into tokens.

3. To create words we remove the punctuations from the tokens (in 2.).

3.1 Puncutaions used are: string.punctuations are used. 
Note: The functions are self explanatory with a mini readme inside each fucntion.

