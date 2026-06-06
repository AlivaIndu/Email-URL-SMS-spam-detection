# Email-URL-SMS-spam-detection
An AI-powered cybersecurity platform designed to detect and prevent phishing attacks using Machine Learning, NLP, URL analysis, screenshot inspection, and browser extension-based real-time protection.

## 🚀 Overview

PhishShield-AI is a smart phishing detection system that helps users identify malicious URLs, phishing emails, suspicious SMS messages, and fake websites before they become victims of cyber attacks.

The platform combines **Machine Learning**, **Natural Language Processing (NLP)**, and **real-time threat analysis** to improve phishing detection accuracy.

---

## ✨ Features

### 🔗 URL Phishing Detection
- Detects malicious and phishing URLs
- Feature extraction based URL analysis
- Checks:
  - HTTPS usage
  - Suspicious keywords
  - URL length
  - Special characters
  - IP-based domains
  - Domain trust patterns
- Machine Learning prediction for phishing probability

### 📧 Email Phishing Detection
- Detects phishing emails using NLP
- Classifies email text as:
  - Legitimate
  - Suspicious
  - Phishing
- Uses text preprocessing and ML classification

### 📱 SMS Phishing Detection
- Detects fraudulent SMS messages
- NLP-based spam/phishing text analysis
- Highlights suspicious patterns and urgency-based manipulation

### 🖼️ Screenshot Analysis
- Upload screenshots of suspicious websites/emails
- Detects phishing indicators from screenshots
- Helps identify fake login pages or scam interfaces

### 🌐 Browser Extension Protection
- Real-time website monitoring
- Automatically scans URLs while browsing
- Warns users about phishing websites
- Provides instant risk score

### 📊 Risk Score System
- Generates phishing probability score
- Displays:
  - Low Risk
  - Medium Risk
  - High Risk

---

## 🧠 Machine Learning Models Used

| Module | Model |
|--------|------|
| URL Detection | Logistic Regression |
| Email Detection | Multinomial Naive Bayes |
| SMS Detection | Multinomial Naive Bayes |

## 📊 Model Performance

| Module | Accuracy |
|----------|----------|
| URL Detection | 96% |
| Email Detection | 92% |
| SMS Detection | 97% |

### NLP Techniques Used
- Tokenization
- Stopword removal
- Text preprocessing
- TF-IDF Vectorization
- Text Classification

---

## 🏗️ System Architecture

```text
User Input
    │
    ├── URL Analysis
    ├── Email Analysis
    ├── SMS Analysis
    ├── Screenshot Analysis
    │
Backend Processing
    │
    ├── Feature Extraction
    ├── NLP Preprocessing
    ├── ML Prediction
    │
Risk Scoring Engine
    │
Final Result
    ├── Safe
    ├── Suspicious
    └── Phishing
```

---

## 🛠️ Tech Stack

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- Flask

### Machine Learning & NLP
- Scikit-learn
- NLTK
- Pandas
- NumPy

### Browser Extension
- JavaScript
- Manifest JSON

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/AlivaIndu/PhishShield-AI.git
```

### 2. Navigate to project folder

```bash
cd PhishShield-AI
```

### 3. Create virtual environment

```bash
python -m venv venv
```

### 4. Activate virtual environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run Flask server

```bash
python app.py
```

---

## 📈 Workflow

### URL Detection Flow

```text
User URL
   ↓
Feature Extraction
   ↓
Logistic Regression Model
   ↓
Risk Score
   ↓
Final Prediction
```

### Email/SMS Detection Flow

```text
Input Text
   ↓
NLP Preprocessing
   ↓
TF-IDF Vectorization
   ↓
Multinomial Naive Bayes
   ↓
Prediction
```

---

## 🔍 Example Use Cases

### URL Analysis

Input:

```text
https://secure-paytm-login.verify-account.com
```

Output:

```text
⚠️ High Risk – Possible Phishing Website
Risk Score: 92%
```

### Email Analysis

Input:

```text
URGENT! Your bank account will be suspended.
Click below immediately to verify.
```

Output:

```text
⚠️ Suspicious Email Detected
```

---

## 🎯 Future Improvements

- Deep Learning based phishing detection
- Real-time threat intelligence API integration
- Multi-language phishing detection
- Dashboard for analytics
- User authentication and history tracking
- Cloud deployment

---

## 📸 Project Screenshots

### Home Page 

<img width="1156" height="598" alt="image" src="https://github.com/user-attachments/assets/b01495d5-8940-418b-96d1-c1bc8bf6d006" />

## Scanning page

<img width="1155" height="670" alt="image" src="https://github.com/user-attachments/assets/7a0ab95b-2512-4da2-a938-bedb0da9df08" />

### URL Analysis

<img width="415" height="754" alt="image" src="https://github.com/user-attachments/assets/48fff227-ca63-4293-9311-321b7d0a4783" /> <img width="1279" height="767" alt="image" src="https://github.com/user-attachments/assets/ecaa010a-07a2-434a-b0e2-923d982615a3" />

## Chrome Browser Extension

<img width="940" height="366" alt="image" src="https://github.com/user-attachments/assets/709c152a-0bbf-4433-a861-6900e8d65f25" />


---

## 🤝 Contributors

- [Aliva Indu](https://github.com/AlivaIndu)
- [Aashutosh Kumar Singh](https://github.com/aashutoshkumarsingh)
- [Ananya Shreya](https://github.com/ananyashreya21)
- [Raj Kamal](https://github.com/Rajkamal007264)
- [Akshay Kashyap](https://github.com/akshaykashyap3010)

---

## 📜 License

This project is for educational and research purposes.

---

## ⭐ Support

If you like this project, consider giving it a **star ⭐** on GitHub.


