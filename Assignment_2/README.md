###### A2_PhD20017_Hemant_yadav


###### I have shown results for markov assumption length 1 only in this readme. To get the results for markov assumptinolength 2. please look into the folder markov_2/ Everything is similar except the numbers.

+ Folder structure: 
    + home folder = contains the main python jupyter notebook, quest_3.pdf and a README.md.
        + markov_1/2 = contains the saved results for markow assumption length 1 and 2. which can be used to visualize them later. The files are stats.json and q3.txt. Both the files can be opened using a standard editor as both of them are normal text.

###### Note: The functions in the jupyter notebbok are self explanatory with a mini readme inside each fucntion.

### Question-1

1. The required code is in assignment.ipynb. 
   1. Each function and class in the script has a mini readme. Thus the functions are self expainatory.
   2. The smoothing assumptin is, I simple do the absolute discounting of 0.7 as in good turing method.
   3. To change the markow assumption length. set one variable in the first cell as (maro-assumption-length+1). The variable name is "n_gram"
   4. The **reported scores are macro average for markov assumption length 1**. The result files are save in folder markov_1. 
   5. For length 2 everything is similar, it's just in the folder markov_2/
   
2. precision, recall and F1 score are as follows: 
    + fold_0 = (0.37,0.29,0.32)
    + fold_1 = (0.54,0.44,0.48)
    + fold_2 = (0.55,0.45,0.50)
    + Average precision, recall and F1 score are as follows: (0.48,0.40,0.43)
3. Tag wise precision, recall and F1 score = It's hard to put this in a readme. The results are save at markov_(assumption-length) folder in a file named **stats.json**. the key value pair are as follows for each fold: 
    + "key_10": "fold_0_scores_conf_m":"macro_classwise_prec_and_rec",
    + "key_11": "fold_1_scores_conf_m":"macro_classwise_prec_and_rec",
    + "key_12": "fold_2_scores_conf_m":"macro_classwise_prec_and_rec" 
4. confusion matrix, it's also saved in **stat.json**. 
    + "key_10": "fold_0_scores_conf_m":"conf_m",
    + "key_11": "fold_1_scores_conf_m":"conf_m",
    + "key_12": "fold_2_scores_conf_m":"conf_m" 

5. Statistic of tag set are as follows: 
    + "vocab_len": 49809,
        "pos_tag_len": 472,
        "max_len": 221.0,
        "min_len": 1.0,
        "average_len": 21.057067730528605,
        "standard_deviation_len": 14.796601080432245,
        "num_word_types_more_than_1_pos_tag": 9582,
        "num_of_tag_vs_word_types": {
            "15": 1,
            "13": 1,
            "11": 1,
            "10": 2,
            "9": 5,
            "8": 10,
            "7": 23,
            "6": 75,
            "5": 176,
            "4": 463,
            "3": 1594,
            "2": 7231
        }
    + **For detailed statistics please look at the *stat.json*. It also has these 2 addiotional info** 
        + "word_type_to_num_of_tag",
        + "tag_2_num_word_types"

**Note I prefer micro scores over macro, since there is serious class imbalance**

+ Micro precision, recall and F1 score are as follows: 
    + fold_0 = (0.840,0.840,0.840)
    + fold_1 = (0.861,0.861,0.861)
    + fold_2 = (0.862,0.862,0.861)
    + Average precision, recall and F1 score are as follows: (0.854,0.854,0.854)

### Question-2

1. The answer is in quest_2.pdf in the same folder.


### Question-3

+ Different statistics are stored in **q3.txt** file.
+ Percentage of words incorrectly classified: 43.6 %.
+ The word types which are most frequently tagged incorrectly are mostly the ones which have more than **1** pos-tag. as can be seen by the below results. Therefore it's because of the amiguity of thesame word type belonging to the **N** number of tags.
   
    + Word types predicted incorrectly atleast 10 times are:
    
            word type (A) predicted incorrectly 5980 times
            word type (TO) predicted incorrectly 3600 times
            word type (IN) predicted incorrectly 2801 times
            word type (THAT) predicted incorrectly 2492 times
            word type (HIS) predicted incorrectly 2031 times
            word type (BUT) predicted incorrectly 1437 times
            word type (ON) predicted incorrectly 1355 times
            word type (IT) predicted incorrectly 1078 times
            word type (THERE) predicted incorrectly 716 times
            word type (NO) predicted incorrectly 645 times
            word type (HER) predicted incorrectly 595 times
            word type (:) predicted incorrectly 542 times
            word type (() predicted incorrectly 495 times
            word type (OF) predicted incorrectly 491 times
            word type (THE) predicted incorrectly 489 times
            word type (MORE) predicted incorrectly 487 times
            word type (SO) predicted incorrectly 485 times
            word type (,) predicted incorrectly 464 times
            word type (AS) predicted incorrectly 413 times
            word type (ABOUT) predicted incorrectly 404 times
            word type (BY) predicted incorrectly 333 times
            word type (LIKE) predicted incorrectly 297 times
            word type (THAN) predicted incorrectly 296 times
            word type (BEFORE) predicted incorrectly 291 times
            word type (OVER) predicted incorrectly 284 times
            word type (YOU) predicted incorrectly 272 times
            word type (SOME) predicted incorrectly 267 times
            word type (VERY) predicted incorrectly 264 times
            word type (AND) predicted incorrectly 255 times
            word type (FOR) predicted incorrectly 250 times
            word type (.) predicted incorrectly 245 times
            word type (AFTER) predicted incorrectly 240 times
            word type (BECAUSE) predicted incorrectly 238 times
            word type (MOST) predicted incorrectly 224 times
            word type (MUCH) predicted incorrectly 212 times
            word type (ONE) predicted incorrectly 205 times
            word type (SINCE) predicted incorrectly 197 times
            word type (THROUGH) predicted incorrectly 195 times
            word type (WHILE) predicted incorrectly 188 times
            word type (TOO) predicted incorrectly 188 times
            word type (NEW) predicted incorrectly 165 times
            word type (RIGHT) predicted incorrectly 163 times
            word type (OUT) predicted incorrectly 154 times
            word type (LITTLE) predicted incorrectly 152 times
            word type (UPON) predicted incorrectly 151 times
            word type (THOUGH) predicted incorrectly 131 times
            word type (SUCH) predicted incorrectly 124 times
            word type (AROUND) predicted incorrectly 112 times
            word type (PUBLIC) predicted incorrectly 97 times
    +   Word types with more than **1** POS-tag are: 
            [('that', 15),
            ('a', 13),
            ('to', 11),
            ('in', 10),
            ('out', 9),
            ('right', 9),
            ('it', 9),
            (':', 9),
            ('you', 8),
            ('little', 8),
            ('more', 8),
            ('on', 7),
            ('for', 7),
            ('as', 7),
            ('one', 7),
            ('much', 6),
            ('like', 6),
            ('after', 6),
            ('before', 6),
            ('no', 6),
            ('by', 6),
            ('the', 6),
            ('most', 6),
            ('over', 6),
            ('too', 6),
            ('of', 6),
            ('about', 6),
            ('and', 6),
            ('than', 5),
            ('so', 5),
            (',', 5),
            ('there', 5),
            ('some', 5),
            ('but', 5),
            ('his', 5),
            ('new', 4),
            ('through', 4),
            ('while', 4),
            ('though', 4),
            ('public', 4),
            ('very', 4),
            ('(', 3),
            ('because', 3),
            ('such', 3),
            ('upon', 3),
            ('since', 3),
            ('her', 3),
            ('around', 3),
            ('.', 2)]

###### For any quries please contact hemantya@iiitd.ac.in