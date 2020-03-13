---
title: "Data Science for Business Notes"
date: 2020-03-28 08:00:00
updated: 2020-05-25 10:09:33
tags: ["Notes","Study"]
---

Foster Provost and Tom Fawcett, Data Science for Business: What you need to know about data mining and data-analytic thinking, O'Reilly Media; 1 edition (August 16, 2013)
[Notes](https://www.studeersnel.nl/nl/document/technische-universiteit-eindhoven/business-analytics-decision-support/samenvattingen/summary-data-science-for-business/3274615/view)

1. Introduction: Data-Analytic Thinking
   1. Data science: a set of fundamental principles that guide the extraction of knowledge from data
   2. Churn: customers switching from one company to another
   3. DDD: Data-Driven Decition Making =by> Data science involces principles, processes, and techniques for understanding phenomena via the (automated) analysis of data. [data-driven-decision-making-notes.pdf](0)
      1. Discovery
      2. Accuracy
   4. Big Data: datasets that are too large for traditional data processing systems
   5. Data, Data Science Capability as a Dtrategic Asset: the capability to extract useful knowledge from data
   6. Fundamental concept:
      1. Extracting useful knowledge from data to solve business problemscan be treated systematically by following a process with reasonably well-defined stages
      2. From a large mass of data, information technology can be used tofind  informative  descriptive  attributes of entities of interest
      3. If you look too hard at a set of data, you will find something—butit might not generalize beyond the data you’re looking at
      4. Formulating  data  mining  solutions  and  evaluating  the  resultsinvolves thinking carefully about the context in which they will be used
2. Business Problems and Data Science Solutions
   1. Fundamentally different types of tasks data mining algorithms address:
      1. Classification and class probability estimation
         1. attempts to predict, for each individual in a population, which of a (small) set of classes this individual belongs to (binary target)
         2. scoring model applied to an individual produces a score representing the probability that that individual belongs to each class
      2. Regression (“value estimation”)
         1. attempts to estimate or predict, for each individual, the numerical value of some variable for that individual (numeric target)
      3. Similarity matching
         1. attempts to identify similar individuals based on data known about them
      4. Clustering
         1. attempts to group individuals in a population together by their similarity, but not driven by any specific purpose
      5. Co-occurrence grouping
         1. attempts to find associations between entities based on transactions involving them
      6. Profiling (behaviour description)
         1. attempts to characterize the typical behaviour of an individual, group, or population
      7. Link prediction
         1. attempts to predict connections between data items, usually by suggesting that a link should exist, and possibly also estimating the strength of the link
      8. Data reduction
         1. attempts to take a large set of data and replace it with a smaller set of data that contains much of the important information in the larger set
      9. Casual modelling
         1. attempts to understand what events or actions actually influence others
   2. Unsupervised: data mining problem when there is no clear target
   3. Supervised: data mining problem where a specific target is defined and there must be data on the target
   4. Label: the value for the target variable for an individual
   5. Data mining algorithms:
      1. supervised methods
         1. classification
         2. regression
         3. casual modelling
         4. similarity matching
         5. link prediction
         6. data reduction
      2. unsupervised
         1. clustering
         2. co-occurrence grouping
         3. profiling
         4. similarity matching
         5. link prediction
         6. data reduction
   6. The data mining process given by the Cross Industry Standard Process for Data Mining (CRSIP-DM):
      1. Business Understanding
          * to understand the problem to be solved
          * the design team should think carefully about the problem to be solved and about the use scenario (the analysts’ creativity plays a large role)
      2. Data Understanding
          * to understand the strengths and limitations of the data because there rarely is there an exact match with the problem
          * cost of data may vary (some data may be purchased, free, or doesn’t exist at all)
      3. Data Preparation
          * conversing the data into forms that yield better results (removing or inferring missing values, converting data to different types)
          * leakage must be considered carefully (a situation where a variable collected in historical data gives information on the target variable – information that appears in historical data but is not actually available when the decision has to be made)
      4. Modelling
          * the output of modelling is some sort of model or pattern capturing regularities in the data
      5. Evaluation
          * to assess the data mining results rigorously and to gain confidence that they are valid and reliable before moving on
          * ensure that the model satisfies the original business goals
          * evaluating the results includes both quantitative and qualitative assessments
      6. Deployment
          * the results are put into real use in order to realize some return on investment
   7. Related analytic techniques:
      1. Statistics
      2. Database Querying
      3. Data Warehousing
      4. Regression Analysis
      5. Machine Learning and Data Mining
3. Introduction to Predictive Modelling: From Correlation to Supervised Segmentation
   1. Model: a simplified representation of reality created to serve a purpose
   2. Predictive modelling: the primary purpose of the model is to estimate an unknown value
   3. Descriptive modelling: the primary purpose of the model is to gain insight into the underlying phenomenon or process
   4. Supervised learning: model creation where the model describes a relationship between a set of selected variables (attributes or features) and a predefined variable called the target variable
   5. Instance (feature vector): a set of attributes (fields, columns, variables, or features)
   6. Model induction: the creation of models
   7. Induction algorithm/learner: the procedure that creates the model from the data
   8. Training data/labelled data: the input data for the induction algorithm, used for inducing the model
   9. Supervised Segmentation & Selecting Informative Attributes - Pure: homogeneous with respect to the target variable
   10. Entropy: a measure of disorder that can be applied to a set
   11. Information Gain (IG): measures the change in entropy due to any amount of new information being added
   12. Classification tree are one sort of tree-structured model
   13. probability estimation tree - Y/N
   14. regression tree - numeric
4. Fitting a Model to Data
   1. Parameter learning/parametric modeling: tuning parameters so that the model fits the data as well modelling as possible
   2. Linear discriminant: linear functions (𝑦 = 𝑚𝑥 + 𝑏) that discriminates between the classes, and the function of the decision boundary is a linear combination – a weighted sum – of the attributes
   3. Support vector machine (SVM)
      1. First fit the fattest bar between the classes
      2. the linear discriminant will be the center line through the dashed parallel lines (margin)
      3. has hinge loss - “small” errors
   4. Regression via Mathematical Functions
      1. Loss functions - hinge loss, Zero-one loss
      2. absolute error
   5. Least squares regression: its very sensitive to the date, outlying data points can severely skew the resultant linear function
   6. Logistic regression f(x) is the model’s estimation of the log-odds that x belongs to the positive class
      1. Most important parts logistic regression
      2. Differences between classification trees and linear classifiers
   7. Neural networks: can be seen as a “stack” of models
5. Overfitting and Its Avoidance
   1. Generalization - the property of a model or modelling process, whereby the model applies to data that were not used to build the model
   2. Overfitting - the tendency of data mining procedures to tailor models to the training data, at the expense of generalization to previously unseen data points
      1. There is a fundamental trade-off between model complexity and the possibility of overfitting.
   3. Fitting graph - shows the accuracy of a model as a function of complexity
      1. Estimate generalization performance by comparing the predicted values with the hidden true values.
   4. Holdout data - data not used in building the model, but for which we do know the actual value of the target variable
      1. Generally, there will be more overfitting as one allows the model to be more complex.
      2. One way mathematical functions can become more complex is by adding more variables (more attributes) or changing the function from being truly linear to nonlinear.
      3. Overfitting is bad because as a model gets more complex it is allowed to pick up harmful spurious correlations. The harm occurs when these spurious correlations produce incorrect generalizations in the model.
      4. A holdout set gives us an estimate of generalization performance.
   5. Cross-validation - a more sophisticated holdout training and testing procedure
      1. Cross-validation begins by splitting a labelled dataset into k partitions called folds. The purpose of cross-validation is to use the original labelled data efficiently to estimate the performance of a modelling procedure. The result is k-different accuracy results, which then can be used to compute the average accuracy and its variance.
   6. Learning curve - a plot of the generalization performance against the amount of training data
      1. A learning curve shows the generalization performance – the performance only on testing data, plotted against the amount of training data used. A fitting graph shows the generalization performance as well as the performance on the training data, but plotted against model complexity.
      2. Tree induction uses two techniques to avoid overfitting:
         1. stop growing the tree before it gets too complex
            1. the threshold can be determined using a hypothesis test.
         2. grow the tree until it is too large, then “prune” it back, reducing its size (and thereby its complexity)
      3. The general method for avoiding overfitting is to choose the value for some complexity parameter by using some sort of nested holdout procedure.
   7. Sequential forward selection (SFS) - uses a nested holdout procedure to first pick the best individual feature, by looking at all models built using just one feature
   8. Regularization - a combination of fit to the data and simplicity of the model
6. Similarity, Neighbors, and Clusters
   1. Similarity and Distance (Nearest-Neighbor Reasoning)
      1. nearest-neighbor methods often use weighted  voting or imilarity moderated voting
      2. instance-based learning
      3. Case-Based Reasoning
   2. Geometric Interpretation, Overfitting, and Complexity Control
      1. k-NN e.g. k = n | k = 1
      2. Issues with Nearest-Neighbor Methods
         1. Intelligibility
         2. Dimensionality and domain knowledge
   3. Technical Details - Calculating Scores from Neighbors
      1. Heterogeneous Attributes
      2. Manhattan distance or L1-norm
      3. Jaccard distance
      4. Cosine distance - text classification
      5. edit distance or the Levenshtein metric
      6. Majority vote classification
      7. Majority scoring function
      8. Similarity-moderated classification
      9. Similarity-moderated scoring
      10. Similarity-moderated regression
   4. Clustering
      1. Hierarchical Clustering - e.g. Tree of Life
      2. Clustering Around Centroids - k-means clustering
      3. Using Supervised Learning to Generate Cluster Descriptions
      4. CRISP data mining process
7. Decision Analytic Thinking I: What Is a GoodModel?
   1. Evaluating Classifiers
   2. Classifier accuracy
   3. Confusion Matrix
8. Visualizing Model Performance
9. Evidence and Probabilities
10. c

* Understanding Data and the Data Mining Process
* Exploring and Visualizing Data
* Market Segmentation of Customers
* Working with Unstructured Datasets
* Predictive Modeling
* Overfitting and Evaluating Models
* Data Mining Techniques for Prediction
* Pro-Active Churn Management
* Data Based Decision Making
* Business Strategy for Employing Data Science

Tools:

1. Calculus
2. Linear Algebra - [MIT Math](https://mitmath.github.io/1806/)
3. Probability And Statitics
4. Statistical Inference
5. Applied Linear Regression 4th edition by Weisberg
6. Statistics for Experimenters: Design, Innovation, and Discovery, 2nd Edition
7. Probability and Measure
8. SVD cholesky decomposition matrix differentiation
9. ..
