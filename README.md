# Recognizing Misinformation

This project aims to analyze current models and technologies for recognizing and flagging misinformation on the internet, and hopes to improve these models and find patterns that people could use to make more informed decisions while reading news that could potentially be misinformation.

## Summary
![](images/slide.png)


## Introduction
Most people in the world have been exposed to misleading news articles about COVID-19 in the past few months. This causes fear, uncertainty, and doubt that has had negative effects such as loss of life, economic instability, and political turmoil. To address this problem, we are designing a machine mearning model that can identify misinformation and warn the reader when they encounter a headline or article that may contain misinformation. While we are categorically focusing on coronavirus news right now, this model may be generalized to detect misleading and false news about other topics as well.

False or misleading news headlines can sometimes be characterized by errors in punctuation and spelling, use of exclamation marks, or use of all caps text. The credibility of verious news sources, tweets, whatsapp forwards, facebook posts, and online news websites can also be used as factors in determinging the presence of misinformation. We will train our models to identify these patterns that may correlate with misleading headlines or text.

## Methods
We will combine multiple pre-labelled datasets in order to create a substantial dataset that covers a balance of both misleading and factual information. Here are links to two of our datasets. 

[https://www.kaggle.com/sagunsh/coronavirus-news-headline](https://www.kaggle.com/sagunsh/coronavirus-news-headline)

[https://www.kaggle.com/trtmio/project-coviewed-subreddit-coronavirus-news-corpus](https://www.kaggle.com/trtmio/project-coviewed-subreddit-coronavirus-news-corpus)



A significant step in processing our data will be extracting numerical features we can use in supervised and unsupervised methods. One set of featues we will be using is the term frequency–inverse document frequency, a statistic commonly used for text classification. We will also be generating our own features based on our intuition on potientially related properties of the text such as sentence structure or punctuation usage.

Based on our features, the model will output whether a particular piece of news is trustable or not. Thus, our model is a binary classifier. To acheive this we will use unsupervised learning methods such as k-means clustering or other clustering algorithms and supervised learning methods such as logistic regression, decision trees, or neural networks.
## Results
The results of this project will be a set of supervised and unsupervised models that can determing the presence of misinformation. The degree of accuracy of these models will be analyzed in order to determine the method that was most effective. We will be able to compare our results to the performance of existing implementation of systems that have the same goal.

## Discussion
The ideal outcome of this project is a model that can identify the presence of misinformation in a text with high accuracy. This capability would allow for large platforms to minimize the exposure of misinformation to their users. If high accuracy is not achieved there are still benefits from the automated nature of a machine learning model. This work will still be able to  reduce the workload of manual review. Future work may include improving the accuracy of our models, finding better methods for obtaining data, or changing the focus to augmenting human review instead of replacement. 

## References 
Ko, Youngjoong, and Jungyun Seo. "Automatic text categorization by unsupervised learning." COLING 2000 Volume 1: The 18th International Conference on Computational Linguistics. 2000.

[http://www.tfidf.com/](http://www.tfidf.com/)


---

CS 4641 Group Project by Akanksha Jhunjhunwala, Albert Chen, Ermy Izihirwe and Sudhanshu Agarwal

---
