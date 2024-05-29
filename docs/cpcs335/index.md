---
sidebar_position: 0
title: CPCS-335 Fundamentals of artificial intelligence
---

| Supervised learning | Unsupervised learning |
| --- | --- |
| Linear Regression<br />Naive Bayes<br />Support vector machines<br />K-nearest neighbour<br />Neural networks | Clustering<br />Dimensionality reduction |

| Approach | Characteristics | Drawbacks |
| --- | --- | --- |
| Supervised learning | <ul><li>Learns from labeled data (input-output pairs) </li><li>Goal is to learn a mapping from inputs to outputs </li><li>Used for tasks like classification and regression </li></ul> | <ul><li>Requires labeled data, which can be time-consuming and expensive to obtain </li><li>Performance is limited by the quality and quantity of labeled data </li></ul> |
| Unsupervised learning | <ul><li>Learns from unlabeled data </li><li>Goal is to discover patterns, structures, or relationships within the data </li><li>Used for tasks like clustering, dimensionality reduction, and association rule mining </li></ul> | <ul><li>Lack of labeled data can lead to less accurate results compared to supervised learning </li><li>Interpretation of results may require human intervention </li></ul> |
| Reinforcement learning | <ul><li>Learns through interactions with an environment </li><li>Goal is to learn a policy that maximizes cumulative rewards over time </li><li>Used in scenarios where an agent must learn to navigate and make decisions in dynamic environments </li></ul> | <ul><li>Can be computationally expensive and require a large number of iterations to converge </li><li>Designing an appropriate reward function can be challenging </li></ul> |

classification
+ Medical diagnosis
+ Credit scoring
+ Image classification
+ Sentiment analysis
+ Handwriting recognition
+ Fraud detection

regression
+ House price prediction
+ Temperature forecasting
+ Stock price prediction
+ Healthcare cost prediction
+ Energy consumption forecasting
+ GPA prediction

clustering
+ Customer segmentation
+ Image segmentation
+ Social network analysis
+ Document clustering
+ Genomic data analysis
+ Market basket analysis

---

| Approach | Characteristics | Advantages | Drawbacks |
| --- | --- | --- | --- |
| Supervised learning | <ul><li>Learns from labeled data (input-output pairs)</li><li>Goal is to learn a mapping from inputs to outputs</li><li>Used for tasks like classification and regression</li></ul> | <ul><li>Produces accurate and reliable results when sufficient labeled data is available</li><li>Well-established algorithms and techniques</li><li>Suitable for a wide range of applications</li></ul> | <ul><li>Requires labeled data, which can be time-consuming and expensive to obtain</li><li>Performance is limited by the quality and quantity of labeled data</li></ul> |
| Unsupervised learning | <ul><li>Learns from unlabeled data</li><li>Goal is to discover patterns, structures, or relationships within the data</li><li>Used for tasks like clustering, dimensionality reduction, and association rule mining</li></ul> | <ul><li>Can work with large amounts of unlabeled data</li><li>Useful for exploratory data analysis and finding hidden patterns</li><li>Can be used as a preprocessing step for supervised learning</li></ul> | <ul><li>Lack of labeled data can lead to less accurate results compared to supervised learning</li><li>Interpretation of results may require human intervention</li></ul> |
| Reinforcement learning | <ul><li>Learns through interactions with an environment</li><li>Goal is to learn a policy that maximizes cumulative rewards over time</li><li>Used in scenarios where an agent must learn to navigate and make decisions in dynamic environments</li></ul> | <ul><li>Suitable for complex decision-making problems</li><li>Can learn from experience and adapt to changing environments</li><li>Useful for applications like robotics, gaming, and control systems</li></ul> | <ul><li>Can be computationally expensive and require a large number of iterations to converge</li><li>Designing an appropriate reward function can be challenging</li></ul> |
| Artificial Neural Networks | <ul><li>Inspired by the biological neural networks in the human brain</li><li>Consist of interconnected nodes (neurons) that process and transmit information</li><li>Can be used for both supervised and unsupervised learning tasks</li></ul> | <ul><li>Capable of learning complex non-linear relationships</li><li>Can be applied to a wide range of problems</li><li>Highly scalable and parallelizable</li></ul> | <ul><li>Require large amounts of data for training</li><li>Can be computationally expensive, especially for deep neural networks</li><li>Prone to overfitting and can be difficult to interpret</li></ul> |
| Deep learning | <ul><li>A subset of machine learning that uses deep neural networks with multiple layers</li><li>Can automatically learn features from raw data</li><li>Used for tasks like image recognition, natural language processing, and speech recognition</li></ul> | <ul><li>Achieves state-of-the-art performance in many domains</li><li>Can learn complex representations from raw data</li><li>Highly scalable and adaptable to different tasks</li></ul> | <ul><li>Requires large amounts of data and computational resources</li><li>Can be difficult to interpret and explain the decision-making process</li><li>Susceptible to adversarial attacks and biases in the training data</li></ul> |
