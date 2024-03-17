import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# import csv file
df = pd.read_csv('WA_Fn-UseC_-HR-Employee-Attrition.csv')

print(df)

