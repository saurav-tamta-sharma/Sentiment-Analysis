# **Sentiment Analysis with Sentiment140**

This project implements a machine learning model to classify textual data (e.g., product reviews, social media posts) into two sentiment categories: positive and negative. The model is built using the **Sentiment140** dataset and provides a web interface for real-time sentiment analysis using **Streamlit**.

## **Project Overview**

This project aims to develop a machine learning model that accurately classifies textual data into two sentiment classes: **positive** and **negative**. The model is trained using the Sentiment140 dataset, which contains Twitter data with labeled sentiments. A user-friendly web interface is built using Streamlit, allowing users to input text and view sentiment analysis results in real-time.

## **Technologies Used**

* **Python**: Core language for building the model and processing data.  
* **scikit-learn**: Machine learning library for building and evaluating models.  
* **Streamlit**: Framework for creating the web-based interface.  
* **joblib**: For model and vectorizer serialization.  
* **pandas**: Data manipulation and analysis.  
* **NumPy**: Support for numerical operations.

## **Dataset**

The **Sentiment140** dataset contains 1.6 million labeled tweets, where each tweet is categorized as either **positive** or **negative**. It is used to train the machine learning model.

* Positive: Tweets expressing positive sentiments.  
* Negative: Tweets expressing negative sentiments.

You can access the dataset from [here](https://www.kaggle.com/datasets/kazanova/sentiment140) 

## **Model Workflow**

1. **Data Preprocessing**:  
   * Removing stop words, special characters, and URLs.  
   * Tokenization and lowercasing of text data.  
   * Vectorization using **TF-IDF** to convert text into numerical features.  
2. **Model Training**:  
   * Using **Logistic Regression** to classify sentiments.  
   * Model is trained and tested on the **Sentiment140** dataset.  
3. **Web Interface**:  
   * Built using **Streamlit** to allow users to enter custom text and see sentiment predictions.

