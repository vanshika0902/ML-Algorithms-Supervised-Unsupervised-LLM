Why categorical encoding is required?

Categorical variables contain information, but their values don't inherently have the numerical structure that ML algorithms expect.
So we need to decide how to represent that categorical information without introducing misleading relationships or excessive dimensionality.
That's why we have techniques such as:

One-hot encoding → Ordinal encoding → Target encoding → Frequency encoding → Binary encoding → Native categorical handling



**One-Hot Encoding**


- Using : pd.get_dummies(df, columns=['','']

- from sklearn.preprocessing import OneHotEncoder
  encoder = OneHotEncoder(handle_unknown="ignore")
  X_encoded = encoder.fit_transform(X[["City"]])


- 2nd code execution is better
- When we dont have many categories in the column - best, because it does not introduce any relationship

- 
**Label Encoding**

- Simply converting the discrete values to random numbers.
- To be used when there is natural ordering (ex: High School < Bachelor's < Master's < PhD).
- Some machine learning algorithms will treat these numbers as if they mean something and that can cause problems.
- Code
  from sklearn.preprocessing import OrdinalEncoder

   encoder = OrdinalEncoder(categories = [ ["High School", "Bachelor's", "Master's", "PhD"]])
   X_encoded = encoder.fit_transform(X[['Education]])

**Target Encoding**

- Replace category with the mean of the targets.
- Leads to leakage. 
- Thats when K-Fold Encoding comes in picture.



**K-Fold Encoding**

- Fold 1 ────────→ encode using Folds 2-5
- Fold 2 ────────→ encode using Folds 1,3,4,5
- Fold 3 ────────→ encode using Folds 1,2,4,5
- Fold 4 ────────→ encode using Folds 1,2,3,5
- Fold 5 ────────→ encode using Folds 1-4







**Target Encoding**




