# Network Traffic Classification using Machine Learning

This project is based on my Bachelor's thesis and focuses on classifying network traffic using machine learning models. The goal is to detect malicious behavior in network connections by training supervised models on labeled traffic data from the CICIDS2017 dataset.

---

## 📌 Project Overview

The project compares the performance of three machine learning models:

- **XGBoost**
- **Random Forest**
- **Neural Network (Keras/TensorFlow)**

Each model was trained on the CICIDS2017 dataset, which includes realistic traffic scenarios such as DDoS, brute-force, botnets, and port scans.

---

## 🧪 Technologies Used

- Python
- scikit-learn
- XGBoost
- Optuna
- TensorFlow / Keras
- Flask
- Pandas, NumPy, Matplotlib, Seaborn

---

## 🔄 Dataset Preprocessing

The original CICIDS2017 dataset is split into multiple CSV files per attack type and day. These files were:

- Preprocessed individually (cleaning, encoding, normalization)
- Merged into a single, unified dataset named `all_data.csv`
- Split into training (80%) and testing (20%) subsets

---

## 🔍 Feature Analysis

For each model, feature importance was calculated using:

- **XGBoost:** Gain-based importance
- **Random Forest:** Gini importance


Then, the models were retrained on subsets of top-N features (e.g., top 5, 10, 15) to evaluate the trade-off between performance and dimensionality.

### 🧪 Feature Selection Based on Recall

To determine the optimal number of features, the models were compared based on **recall**, which is critical in intrusion detection (minimizing false negatives).

---

## ⚙️ Model Optimization

Each model was tuned to achieve the best possible performance:

- **Random Forest:** Optimized using `GridSearchCV` with cross-validation for parameters like `n_estimators`, `max_depth`, `min_samples_split`.
- **XGBoost:** Optimized using `Optuna`, exploring parameters such as `learning_rate`, `max_depth`, `subsample`, and `n_estimators`.
- **Neural Network:** Tuned with dropout, batch normalization, and early stopping to prevent overfitting.

---

## 💾 Model Saving

After training, the final models and their selected feature sets were saved to disk using:

- `joblib` for Random Forest and XGBoost
- `HDF5` for the Keras model

These are loaded in the Flask interface for evaluation.

---

## 🌐 Web Interface (Flask)

An interactive web app allows users to:

- Upload a new dataset or use the reserved 20% test set
- Select which trained model to use
- Evaluate model predictions in real-time
- View and compare metrics such as:
  - Accuracy
  - Precision
  - Recall
  - F1-score

---

### 🧪 Sample Results:

| Model           | Accuracy | F1 Score | Precision | Recall  | Duration |
|----------------|----------|----------|-----------|---------|----------|
| Random Forest  | 0.988    | 0.9184   | 0.9443    | 0.9026  | 18.65s   |
| XGBoost        | 0.979    | 0.9136   | 0.8843    | 0.9655  | 1.6s     |
| Deep Learning  | 0.9909   | 0.9552   | 0.9443    | 0.9697  | 27.84s   |

![Web Interface - Metrics](./screenshots/1.png)

---

### 🔍 Per-Class Evaluation

The interface also displays detailed metrics for each class:

![Web Interface - Per-Class Metrics](./screenshots/2.png)

---

## ✅ Conclusions

- **Deep Learning** achieved the best overall performance (highest accuracy and recall).
- **XGBoost** performed best on specific classes but was slightly lower in accuracy.
- **Random Forest** delivered solid baseline results and was computationally efficient.



