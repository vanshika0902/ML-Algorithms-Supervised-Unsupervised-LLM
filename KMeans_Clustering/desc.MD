**Algo**

- Select the # of clusters you want identify in your data. This is "K" in K-Means Clustering.
- Ex: We select K as 3. Randomly select 3 distinct data points
- Measure the distance between 1st point & the three initial clusters.
- Simple distance in case of 1-D. In case of 2-D, it is Eucilidian distance.
- Assign the 1st point to the nearest cluster.
- Repeat for the next points.
- Calculate the mean of clusters. 
- Then again calculate distance of each point from mean. 
- Change the initial points and check when we get the least variation.


**How to choose K?**
  - Plot Number of Clusters (K) on x-axis & Reduction in Variation on y-axis.
  - Find elbow point. (post elbow point there is not much reduction in Variation)

**Diff between K-means clustering & Hierarchical clustering**

- K-means Clsutering specifically tries to put the data into the number of clusters you tell it to.
- Heirarchical Clustering just tells you, pairwise, what two things are most similar.

**Application of K-Means Clustering**

- Customer segmentation in market
- Image compression & segmentation
- Anomaly detection in cybersecurity
- Document clustering in Natural Language Processing
- Recommendation system in e-commerce
