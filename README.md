\# Recognizing Misinformation

This project aims to analyze current models and technologies for recognizing and flagging misinformation on the internet, and hopes to improve these models and find patterns that people could use to make more informed decisions while reading news that could potentially be misinformation.

![](images/touchpoint1.png)


## Introduction

While the spread of misinformation is not a new concept,the topic has recently garnered attention due to its relevancy in the age of the Internet and social media. The increasingly concerning issue has been the subject of studies, especially in relation to vaccination, the Zika virus, as well as Ebola (Wang et al., 2019). More recently, most people in the world have been exposed to misleading news articles about COVID-19 in the past few months. This causes fear, uncertainty, and doubt that has had negative effects such as loss of life, economic instability, and political turmoil. To address this problem, we are designing a machine mearning model that can identify misinformation and warn the reader when they encounter a headline or article that may contain misinformation. While we are categorically focusing on coronavirus news right now, this model may be generalized to detect misleading and false news about other topics as well.

False or misleading news headlines can sometimes be characterized by errors in punctuation and spelling, use of exclamation marks, or use of all caps text. The credibility of verious news sources, tweets, whatsapp forwards, facebook posts, and online news websites can also be used as factors in determinging the presence of misinformation. We will train our models to identify these patterns that may correlate with misleading headlines or text.

## Methods
We will combine multiple pre-labelled datasets in order to create a substantial dataset that covers a balance of both misleading and factual information. Here are links to two of our datasets. 

[https://www.kaggle.com/sagunsh/coronavirus-news-headline](https://www.kaggle.com/sagunsh/coronavirus-news-headline)

[https://www.kaggle.com/trtmio/project-coviewed-subreddit-coronavirus-news-corpus](https://www.kaggle.com/trtmio/project-coviewed-subreddit-coronavirus-news-corpus)


A significant step in processing our data will be extracting numerical features we can use in supervised and unsupervised methods. One set of featues we will be using is the term frequency–inverse document frequency, a statistic commonly used for text classification (Peng et al., 2014). We will also be generating our own features based on our intuition on potientially related properties of the text such as sentence structure or punctuation usage. 

Based on our features, the model will output whether a particular piece of news is trustable or not. Thus, our model is a binary classifier. To acheive this we will use unsupervised learning methods such as k-means clustering or other clustering algorithms and supervised learning methods such as logistic regression, decision trees, or neural networks (Ko & Seo, 2000).

## Results
The results of this project will be a set of supervised and unsupervised models that can determing the presence of misinformation. The degree of accuracy of these models will be analyzed in order to determine the method that was most effective. We will be able to compare our results to the performance of existing implementation of systems that have the same goal.

## Discussion
The ideal outcome of this project is a model that can identify the presence of misinformation in a text with high accuracy. This capability would allow for large platforms to minimize the exposure of misinformation to their users. If high accuracy is not achieved there are still benefits from the automated nature of a machine learning model. This work will still be able to  reduce the workload of manual review. Future work may include improving the accuracy of our models, finding better methods for obtaining data, or changing the focus to augmenting human review instead of replacement. 

## References 

Ko, Y., & Seo, J. (2000). Automatic text categorization by unsupervised learning. Proceedings of the 18th Conference on Computational Linguistics, 1, 453–459.

Peng, Tao, Liu, Lu, & Zuo, Wanli. (2014). PU text classification enhanced by term frequency–inverse document frequency‐improved weighting. Concurrency and Computation, 26(3), 728-741.

Wang, Yuxi, McKee, Martin, Torbica, Aleksandra, & Stuckler, David. (2019). Systematic Literature Review on the Spread of Health-related Misinformation on Social Media. Social Science & Medicine (1982), 240, 112552.

# Midterm Report

![](images/touchpoint2.png)

## Data Preprocessing

The columns of our dataset are source, title text, body text, and label.

Some rows had ``NaN`` values for either the title or body. We replaced these with empty strings. We also grouped sources as "Facebook/Twitter/Youtube", "Medical", "Government", "Education", "News" and "Others" in order to understand the sentence construction in context of the sources (and their group of readers) and how it affects our clustering algorithm. We also cleaned the data to convert the labels column into a boolean "true" and "false" one.

Recognizing misinformation is a classification problem (and not regression) and in our dataset of 1164 columns, 584 (or 50.17%) were articles that were true and the rest (49.8%) were false. All of the articles were related to coronavirus, and the link to the dataset is [here](https://raw.githubusercontent.com/susanli2016/NLP-with-Python/master/data/corona_fake.csv).

This dataset is a collections of sentences so it does not contain any outliers and includes a diverse set of sources. Our feature engineering did lead to creation of some outliers when it came to misspellings and TF-IDF (discussed below) values but we normalized all of the values before further analysis and also computed the PCA to highlight the important features.

## Feature Engineering

In order to apply any machine learning methods, we extracted numerical data by engineering features based on existing literature on misinformation in news, as well as our intution on potential signals within the text. These features will be normalized to text length where applicable.

### TF-IDF

Text frequency-inverse document frequency measures the importance of a word to a document within a corpus. We hypothesized that a text with and wihtout misinformation may be characterized by the emphasis of certain words. We chose to limit the minimum docment frequency to .2 in an attempt to filter out words that are too rare to effectively catagorize an article to be misinformation.

### Stylistic and Vocabulary Patterns

Studies have shown fake news may use simpler, repetitive content in the text body. We extracted the following vocabulary and style statistics:
stop-words,
pronouns, 
adjectives,
negations,
capital letters,
type-token ratio,
average word length,
and number of quotes

We also extracted other ad hoc features such as sentiment, polarity, subjectivity, and mispellings

### Source

The reliability of the information within an article may be highly correlated to the source where the article was found. We labled articles by source with one hot encoding into categories like government, social media, academia, mainstream news, or other.

## Clustering

We normalized our features and ran DBScan, K-means and GMM on the all of the features. The graphs are plotted against two features of sentiment analysis.

DBScan clusters data based on their distances, and this distance is calculated using the vectors (of features) that we generated. We normalized all of our features so that none of them dominates over the others. We used this clustering as it clusters based on "closeness" to neighboring vectors and if DBScan returns two clusters with high purity then this means that true and misleading articles are distinct. DBScan returned three clusters instead of two because we couldn't manually choose the number of clusters, but it gave us important insight into the fact that even within the same label, our datapoints have a lot of variety.

![](images/dbscan.png)

K-means clusters data using a randomly (or for sci-kit learn it tries to optimize convergence) and then clusters vectors close to that center into one cluster. We used two number of clusters and the F-score of K-mean was significantly higher than DBScan, and we discuss more about the implications of this in the section below. The results we got showed that it is possible that a misleading article might closely resemble true ones and vice versa.

![](images/kmeans.png)

GMM uses expectation-maximization to cluster data. We used this method as DBScan and K-means showed the weakness in using just distance to cluster our data, and the results we got were better than K-means with a higher F-score (discussed in the section below). This means that distance is not the right way to approach the problem of clustering misinformation, and we should rather focus on algorithms that use EM or other probabilitistic methods.

![](images/gmm.png)

When we looked at how all three of our clustring algorithms were clustering data when it came to sources, we found that it often clustered false news articles and the true articles from government and educational sources together, and this means that false news articles often portray themselves as being official or gain credibility by using a writing style similar to educational sources. 

### F-measure:

After obtaining two labelled clusters from each of the three clustering algorithms, the F1 score metrics from sci-kit learn was ran on these predictive labels and the true labels from our dataset. The results are shown in the bar graph below:

![](images/fmeasure.png)

F1 score, otherwise known as F-measure, is the average between precision and recall, which is why it was chosen as measurement of performance. In this case, precision is the number of correctly identified true news articles, divided by the number of articles classified as true. On the other hand, recall is the number of correctly identified true news articles, divided by the number of true articles. GMM and K-Means both had an F-Measure well above 50% (85% and 65%), and this can serve as an indication that there is some feature(s) in our dataset that can used to differentiate between false and true news articles.

## Conclusion

After running the clustering algorithms as described above, we realized that our data isn't very suitable to unsupervised laerning. Unsupervised learning does not learn from "experience" and that is an important factor in our data because of how subjective the labels can be. Supervised learning is general is known to incraese accuracy, F-scores, etc., and improving the F-score is one of our main goals right now.

## References

Horne, Benjamin D., and Sibel Adali. "This just in: Fake news packs a lot in title, uses simpler, repetitive content in text body, more similar to satire than real news." arXiv preprint arXiv:1703.09398 (2017).

Eldén, Lars. Matrix methods in data mining and pattern recognition. Society for Industrial and Applied Mathematics, 2007

---

CS 4641 Group Project by Akanksha Jhunjhunwala, Albert Chen, Ermy Izihirwe and Sudhanshu Agarwal

---
