###### Tested on python 3.6

- To install the dependencies run
```
 pip install -r requirements.txt
```

### Assumptions: 
1. To preprocess the input text file, first we split it in terms of paragraph if any (i.e., split on a '\n\n' symbol) and then apply sent\_tokenize on it. It worked better than just using the sent\_tokenize alone on the input text file.

2. word\_tokenize is used to split the sentences into tokens.

3. To create words we remove the punctuations from the tokens (in 2.).

	3.1 Puncutaions used are: string.punctuations are used. 

4. For Task 4,5,6: enter the exact word you want to search for. Example, "you" and "you." will be treated differently. For task 5, we have also added some punctuations that even if the use does not they will be ignored. Please look at the task 5 fucntion for a deatiled readme.
 


#### Note: The functions in the jupyter notebbok are self explanatory with a mini readme inside each fucntion.

For any queries please contact: hemantya@iiitd.ac.in

