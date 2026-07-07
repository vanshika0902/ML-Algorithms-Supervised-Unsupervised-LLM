import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, roc_auc_score, roc_curve
import pandas as pd
import numpy as np


df_train = pd.read_csv('/path/to/train.csv')
df_test = pd.read_csv('/path/to/test.csv')

# EDA

# categorical encoding

print(df_train.info())
print(df_test.info())

# check for number of unique values in the data 
# if LESS i.e. - LOW CARDINALITY - use ONE HOT ENCODING

print(df_train.nunique())
print(df_test.nunique())

# null imputations

print(df_train.isnull().sum())
print(df_test.isnull().sum())

y = df_train['target']
X = df_train.drop('target', axis=1)

y_test = df_test['target']
X_test = df_test.drop('target', axis=1)
                       
X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.2, random_state=42)

# perform HPT to get best HPs

# can add HPs too like num boost rounds, eta, min child weight
model = xgb.XGBClassifier()

model.fit(X_train, y_train)

y_pred = model.predict(X_valid)

print(accuracy_score(y_valid,y_pred))
print(precision_score(y_valid,y_pred))
print(roc_auc_score(y_valid,y_pred))

## can change things and re-test with validation dataset and accordingly proceed with test dataset


