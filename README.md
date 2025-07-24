# Network Traffic Classification using Machine Learning

This project represents my Bachelor's thesis, focusing on the comparative analysis of machine learning models for network traffic classification. The models were trained and tested using the CICIDS2017 dataset.

## 📌 Project Overview

The main goal of this project is to evaluate and compare the performance of three machine learning algorithms in classifying network traffic as benign or malicious:

- XGBoost
- Random Forest
- Neural Network (using Keras/TensorFlow)

The dataset used is **CICIDS2017**, a comprehensive dataset for intrusion detection systems research.

## 🛠️ Features

- Data preprocessing and feature selection
- Model training, optimization, and evaluation
- Saving extracted features and trained models
- Web interface built with **Flask** for interactive performance testing
- Upload and evaluate new data samples (20% test split) via the web app
- Real-time comparison between models using metrics such as:
  - Accuracy
  - Precision
  - Recall
  - F1-score

## 🧪 Technologies Used

- Python
- scikit-learn
- XGBoost
- TensorFlow / Keras
- Flask
- Pandas, NumPy, Matplotlib
- CICIDS2017 Dataset

## 🖥️ Web Interface

A simple **Flask-based web app** is included to allow users to:

- Upload a subset of the dataset (20% reserved for testing)
- Choose a trained model
- View performance metrics and compare models
- Display prediction statistics in real time

## 📁 Project Structure

