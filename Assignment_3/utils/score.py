from tqdm.auto import tqdm
import numpy as np
import os, glob, pickle
import pandas as pd
from collections import Counter
import re, string
from sklearn import metrics
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
import seaborn as sns
from collections import defaultdict, OrderedDict


def evaluate(expected, predicted, labels):
    save_dict = {}
    
    eps = 0
    dummy = OrderedDict()
    for i in labels:
        dummy[str(i)] = {str(j) : eps for j in labels}
    for r, i in enumerate(expected):
        dummy[str(i)][str(predicted[r])] +=1

    save_dict['conf_labels'] = [k for k in dummy.keys()]
    
    # confusion matrix
    conf_m = np.array([[j for j in i.values()] for i in dummy.values()]) # confusion matrix
    save_dict['conf_matrix'] =  conf_m.tolist()


    # macro
    ind = [i for i in range(len(conf_m)) if np.sum(conf_m[:,i]) == 0 and np.sum(conf_m[i,:]) == 0]
    conf_m = np.delete(conf_m,ind,1)
    conf_m = np.delete(conf_m,ind,0)
    pre = np.sum(conf_m,axis=0)
    rec = np.sum(conf_m,axis=1)
    p = []
    for i in range(len(pre)):
        if pre[i] !=0 : p.append(conf_m[i,i]/pre[i])
        else: p.append(0)

    r = []
    for i in range(len(pre)):
        if rec[i] !=0 : r.append(conf_m[i,i]/rec[i])
        else: r.append(0)
    save_dict['macro_prec_and_rec'] = [np.mean(np.array(p)), np.mean(np.array(r))]

    print("macro prec and recall --",sum(p)/len(p), sum(r)/len(r))

    # macro f1 score
    f_1 = 2*(((sum(p)/len(p))*(sum(r)/len(r))))/((sum(p)/len(p))+(sum(r)/len(r)))
    print(f" Macro F1 score: {f_1}")
    save_dict['macro_f1'] = f_1

    # accuracy
    acc = len([i for i in range(len(expected)) if expected[i]==predicted[i]])/len(expected)
    print(f"Accuracy: {acc}")
    save_dict['accuracy'] = acc
    
    return save_dict


