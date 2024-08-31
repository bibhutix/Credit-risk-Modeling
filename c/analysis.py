#Importing the libraries that required
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from scipy.stats import chi2_contingency
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report,precision_recall_fscore_support
import warnings
import os

#Loading the dataset
a1=pd.read_excel("X:\APersonal Project\Credit risk Modeling\c\case_study1.xlsx")

a1.head(2)