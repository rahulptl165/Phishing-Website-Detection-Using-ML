# 🛡️ Phishing Website Detection Using Machine Learning

A machine learning-powered web application that detects whether a given website URL is **phishing** or **legitimate** using multiple feature types — including URL structure, domain metadata, and HTML/JavaScript behavior.

> ⚠️ Over 90% of cyber attacks start with phishing. This tool helps users identify potentially harmful URLs **before they click**.

---

## 🔍 Features

- ✅ **URL-based features**: Length, depth, special characters, HTTPS usage, etc.
- ✅ **Domain-based features**: WHOIS registration check, domain age, DNS availability
- ✅ **HTML/JS-based features**: Presence of `<iframe>`, `alert()` scripts, and suspicious JS functions
- ✅ **Binary classification model** (Phishing vs Legitimate)
- ✅ **Flask-based GUI** with modern dark theme
- ✅ **Real-time prediction** on user input

---

## 🧠 Models

- **Algorithm**: `RandomForestClassifier`
- **Training**:
  - 10,000 phishing URLs
  - 10,000 legitimate URLs
- **Evaluation**:
  - Accuracy: ~`91%`
  - Precision: ~`92%`
  - Recall: ~`88%`

- **Algorithm**: `Logistic Regression`
- **Training**:
  - 10,000 phishing URLs
  - 10,000 legitimate URLs
- **Evaluation**:
  - Accuracy: ~`82.1%`
  - Precision: ~`87%`
  - Recall: ~`82%`

- **Algorithm**: `XGBoost`
- **Training**:
  - 10,000 phishing URLs
  - 10,000 legitimate URLs
- **Evaluation**:
  - Accuracy: ~`82.03%`
  - Precision: ~`87%`
  - Recall: ~`82%`

- **Algorithm**: `MLP Classifier`
- **Training**:
  - 10,000 phishing URLs
  - 10,000 legitimate URLs
- **Evaluation**:
  - Accuracy: ~`96%`
  - Precision: ~`96%`
  - Recall: ~`96%`

---

## 🌐 Live Demo

---

## ⚙️ Tech Stack
Python

Flask

Scikit-learn

BeautifulSoup

WHOIS

## 💻 Run Locally

### 🔧 1. Clone the Repository
```bash
git clone https://github.com/rahulptl165/Phishing-Website-Detection-Using-ML.git
cd Phishing-Website-Detection-Using-ML
```

```bash
pip install -r requirements.txt
```

```bash
cd app
```

```bash
python app.py
```

## ✍️ Authors
Rahul Kumar   &nbsp; &nbsp; &nbsp; &nbsp;  &nbsp; &nbsp; &nbsp; &nbsp;     Ayushmaan

[💼 LinkedIn](https://www.linkedin.com/in/rahul-kumar-39051a351)   &nbsp; &nbsp; &nbsp; &nbsp;  &nbsp; &nbsp; &nbsp; &nbsp;     [💼 LinkedIn]()

[💻 GitHub](https://github.com/rahulptl165)     &nbsp; &nbsp; &nbsp; &nbsp;  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;    [💻 GitHub](https://github.com/ayushmaan100)