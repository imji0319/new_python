#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 23:31:03 2020

@author: jihye
"""

from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.preprocessing import Binarizer


# 오차 행렬, 정확도, 정밀도, 재현율 
def get_clf_eval(y_test, pred):
    
    confusion = confusion_matrix(y_test, pred)
    accuracy = accuracy_score(y_test, pred)
    precision = precision_score(y_test, pred)
    recall = recall_score(y_test, pred)
    f1 = f1_score(y_test, pred)
    auc = roc_auc_score(y_test, pred)
    
    print("오차행렬")
    print(confusion)
    print("정확도 : {:.4f} , 정밀도 : {:.4f}, 재현율 : {:.4f}, F1 : {:.4f}, auc : {:.4f}"
          .format(accuracy, precision, recall, f1, auc) )

# 임계값 변경 
def get_eval_by_threshold(y_test, pred_proba_c1, threshold):

    # threshold list 객체 내의 값을 차례로 iteration 하면서 Evaluation 수행
    for custom_th in threshold: 
        binarizer = Binarizer(threshold = custom_th).fit(pred_proba_c1)
        custom_pred = binarizer.transform(pred_proba_c1)
        
        
        print('임계값 :', custom_th)
        get_clf_eval(y_test, custom_pred)
        
# 정밀도와 재현율의 임계값에 따른 값의 변화 그래프 
import matplotlib.pyplot as plt 
import numpy as np 
from sklearn.metrics import precision_recall_curve

def precision_recall_curve_plot(y_test, pred_proba_c1):
    
    precision, recalls , thresholds = precision_recall_curve(y_test, pred_proba_c1)
    
    plt.figure(figsize = (8,6))
    threshold_boundary = thresholds.shape[0]
    plt.plot(thresholds, precision[0:threshold_boundary], linestyle = '--', label = 'precision')
    plt.plot(thresholds, recalls[0:threshold_boundary], label = 'recall')
    
    start, end = plt.xlim()
    
    plt.xticks(np.round(np.arange(start, end, 0.1), 2))
    
    plt.xlabel('Threshold value'); plt.ylabel('Precision and Recall value')
    plt.legend(); plt.grid()
    plt.show()
    

from sklearn.metrics import roc_curve

def roc_curve_plot(y_test, pred_proba_c1):
    
    fprs, tprs, thresholds = roc_curve(y_test, pred_proba_c1)
    
    plt.plot(fprs, tprs, label = 'ROC')
    plt.plot([0,1], [0,1], 'k--', label ='Random')
    
    start, end = plt.xlim()
    plt.xticks(np.round(np.arange(start, end, 0.1),2))
    plt.xlim(0,1) ; plt.ylim(0,1)
    plt.xlabel('FPR (1- Sensitivity'); plt.ylabel('TPR ( Recall )')
    plt.legend()
    plt.show()

    
    