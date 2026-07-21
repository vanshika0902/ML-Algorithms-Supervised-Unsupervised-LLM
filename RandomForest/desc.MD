Decision Trees are 

- easy to build
- easy to use 
- easy to intepret
- but they suffer from inaccuracy (work well on data used to create them but not good on new data)
- Reason : The algo creates very deep trees, which captures random noise of the training data - causing low bias but high variance.
- Solution: 
    - Pre-pruning (Stop growth early using HPs - **max_depth**, **min_samples_split**, **min_samples_leaf**, **max_leaf_nodes**)
    - Post-pruning (Grow the full tree, then remove branches that do not improve validation performance (cost-complexity pruning))
    - Use ensemble (Random Forest, Gradient Boosting)

