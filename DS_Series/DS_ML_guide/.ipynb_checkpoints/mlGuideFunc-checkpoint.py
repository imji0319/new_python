#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 23:31:03 2020

@author: jihye
"""

from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix
from sklearn.preprocessing import Binarizer

# 오차 행렬, 정확도, 정밀도, 재현율 
def get_clf_eval(y_test, pred):
    
    confusion = confusion_matrix(y_test, pred)
    accuracy = accuracy_score(y_test, pred)
    precision = precision_score(y_test, pred)
    recall = recall_score(y_test, pred)
    
    return confusion, accuracy, precision, recall 

# 임계값 변경 

def get_eval_by_threshold(y_test, pred_proba_c1, threshold):
    
    capr = []
    # threshold list 객체 내의 값을 차례로 iteration 하면서 Evaluation 수행
    for custom_th in threshold: 
        binarizer = Binarizer(threshold = custom_th).fit(pred_proba_c1)
        custom_pred = binarizer.transform(pred_proba_c1)
        
        for i in  get_clf_eval(y_test, custom_pred):
            capr.append(i)

        
    return capr


    
    