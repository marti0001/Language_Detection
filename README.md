# Language Detection Project 🌍

A text language detection project using **Multinomial Naive Bayes** and **TF-IDF**. The model recognizes 17 languages, including English, Spanish, French, and others.


## 🔎Project Description  
The goal of this project is to automatically detect the language of a text based on short samples. The model is trained on a dataset containing texts in 17 languages, using NLP techniques (TF-IDF) and a classification algorithm.

## 🎯 Features  
- **Text Cleaning**: Removes special characters and digits.  
- **Data Visualization**: Displays the distribution of languages in the dataset.  
- **TF-IDF Vectorization**: Feature extraction with unigrams and bigrams.  
- **Model Tuning**: Hyperparameter optimization for `alpha` using `GridSearchCV`.  
- **Evaluation**: Confusion matrix, classification report, and accuracy score.  
- **Pipeline**: Saved model as a `.pkl` file for deployment.  
---

## 🛠️ Technologies & Tools

| Category          | Tools & Libraries |
|------------------|------------------|
| **Programming Language** | Python |
| **Data Manipulation** | `pandas`, `numpy` |
| **Machine Learning** | `scikit-learn` (TF-IDF, Cosine Similarity) |
| **Visualization** | `seaborn`, `matplotlib`   |

---
