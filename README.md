## 📌 Project Overview
This project focuses on Categorical Sentiment Analysis using Natural Language Processing (NLP). Unlike standard binary classification (Good/Bad), this model handles the complexity of neutral sentiments often found in social media text.

After extensive experimentation with Logistic Regression, SVM, and Naive Bayes, the **Decision Tree Classifier** using **Bag of Words (BoW)** emerged as the best performing model for this specific dataset.

## 🚀 Features
- **Real-time Prediction:** User-friendly web interface via Streamlit.
- **Categorical Output:** Predicts `Positive`, `Negative`, or `Neutral`.
- **Interpretability:** Uses a Decision Tree model, allowing for clear logic visualization.
- **Robustness:** Achieved **74% Accuracy** on the test dataset, outperforming standard benchmarks for this specific data size.

## 🛠️ Tech Stack
- **Language:** Python
- **Frontend:** Streamlit
- **Machine Learning:** Scikit-Learn (Decision Tree Classifier)
- **Feature Extraction:** CountVectorizer (Bag of Words)
- **Data Manipulation:** Pandas, NumPy
- **Dataset Source:** [Kaggle - Categorical Sentiment Analysis](https://www.kaggle.com/)
