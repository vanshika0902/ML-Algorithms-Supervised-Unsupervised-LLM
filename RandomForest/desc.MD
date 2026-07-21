**Decision Trees** are 

- easy to build
- easy to use 
- easy to intepret
- low bias, high variance
- but they suffer from inaccuracy (work well on data used to create them but not good on new data)
- Reason : The algo creates very deep trees, which captures random noise of the training data - causing low bias but high variance.
- Solution: 
    - Pre-pruning (Stop growth early using **HPs** - **max_depth**, **min_samples_split**, **min_samples_leaf**, **max_leaf_nodes**)
    - Post-pruning (Grow the full tree, then remove branches that do not improve validation performance (cost-complexity pruning))
    - Use ensemble (Random Forest, Gradient Boosting)

---------------------------------------------------------------------------------------------------------------------------------
**Random Forest (Bagging Algo - Bootstrapping the data + aggregating it)**

Steps to build 
 
- Step 1 : Create Bootstrapped dataset: random sampling from original dataset with replacement.
- Step 2 : Create a decision tree using the bootstrapped dataset, but only use a random subset of variables (or columns) at each step.
- Step 3 : Repeat Step 1 & Step 2.

---------------------------------------------------------------------------------------------------------------------------------
Reason why **Random Forest** is better than **Decision Tree**

Each tree:

- sees a different bootstrap sample of the data
- considers only a random subset of features at each split
- If one tree makes a mistake because it overfit, the other trees usually correct it.
- slightly higher bias, but low variance

-------------------------------------------------------------------------------------------------------------------------------------
Final Prediction 

- Majority Votes (in case of Classification)
- Averaging (in case of Regression)

-------------------------------------------------------------------------------------------------------------------------------------
Test its working 

- Using - OOB (Out of Bag) dataset - data that was not included in the bootstrap dataset.
- OOB Error : Proportion of samples that were incorrectly classified
- We can use OOB Error/Accuracy to see how many variables we should select at Step 2. (Usually we start we use square of variables and then do & less)

-------------------------------------------------------------------------------------------------------------------------------------
Fun Facts

- Random Forest natively supports **multiclass classification**
- from sklearn.ensemble import RandomForestClassifier
- **Encoding** : Though in theory categorical variables are okay to use in algo, sklearn does not support it, encoding needs to be done.
- **Feature Scaling** : Not required, algo creates splits basis comparision condition.
- While building a decision tree, the algorithm evaluates all possible splits and computes an impurity metric such as Gini impurity or entropy. It selects the split that produces the largest reduction in impurity, creating child nodes that are as pure as possible. This process is repeated recursively until the stopping criteria are met.
-------------------------------------------------------------------------------------------------------------------------------------

How do handle missing data?

**Step 1** : check type of missingness (MCAR, MAR, MNCAR) 
- MCAR : Missing Completely At Random - use **simple imputation**
- MAR : Missing At Random - Missingness depends on another feature.
- MNAR : Missing Not At Random - Requires domain knowledege

**Step 2**: Check how much data is missing

| Missing Percentage | Recommended Approach |
|--------------------|----------------------|
| **< 5%** | Simple imputation (e.g., mean, median, or mode) |
| **5–30%** | More advanced imputation (e.g., KNN, MICE) |
| **> 40–50%** | Consider dropping the feature if it is not important |

**Step 3** : Choose Imputation type

- Mean Imputation
- Median Imputation
- KNN Imputation
- MICE (Multiple Imputation by Chained Equations)
- For Categorical Variables : Mode Imputation
