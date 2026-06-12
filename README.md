# 🛡️ Network Intrusion Detection using Random Forest

## 📌 Project Overview
Welcome to the repository for **Team 6**'s final project in the Artificial Intelligence Programming course. This project implements a machine learning model designed to detect and classify various network cyber attacks by analyzing network packet flows and payloads.

## 🚀 Getting Started

## Prerequisites
Install the required dependencies to run the model:
```bash
pip install pandas numpy scikit-learn datasets
```

## 🗄️ Dataset
* We loaded the `rdpahalavan/network-packet-flow-header-payload` dataset directly using the Hugging Face `datasets` library.
* The target variable predicted by our model is `attack_cat`.

## 🛠️ Tech Stack & Data Processing
* **Libraries:** Python, `pandas`, `numpy`, `scikit-learn`, and `datasets`.
* **Data Preprocessing:** We applied `TfidfVectorizer` to extract 100 numerical features from the raw string data in the `packet_dat` column. The resulting TF-IDF matrix is maintained as a sparse matrix to optimize memory usage during training.
* **Classification Model:** The core algorithm is a `RandomForestClassifier` built with 100 estimators (`n_estimators=100`).

## 📊 Model Performance & Results
Our Random Forest model was evaluated across 24 different attack categories and normal traffic, achieving an overall accuracy of **97%**. 

Below is the detailed classification report:

| Category (공격 유형) | Precision (정밀도) | Recall (재현율) | F1-Score | Support (데이터 수) |
| :--- | :---: | :---: | :---: | :---: |
| Analysis | 0.95 | 0.97 | 0.96 | 377 |
| Backdoor | 0.95 | 0.89 | 0.92 | 252 |
| Bot | 1.00 | 0.92 | 0.96 | 736 |
| DDoS | 1.00 | 1.00 | 1.00 | 25,601 |
| DoS | 0.94 | 0.87 | 0.91 | 9,854 |
| DoS GoldenEye | 1.00 | 1.00 | 1.00 | 4,675 |
| DoS Hulk | 1.00 | 1.00 | 1.00 | 83,692 |
| DoS SlowHTTPTest | 1.00 | 1.00 | 1.00 | 1,143 |
| DoS Slowloris | 1.00 | 1.00 | 1.00 | 947 |
| Exploits | 0.94 | 0.93 | 0.94 | 9,114 |
| FTP Patator | 1.00 | 1.00 | 1.00 | 6,413 |
| Fuzzers | 0.96 | 0.90 | 0.93 | 4,970 |
| Generic | 0.93 | 0.74 | 0.82 | 6,853 |
| Heartbleed | 0.96 | 0.99 | 0.98 | 23,247 |
| Infiltration | 1.00 | 1.00 | 1.00 | 1,520 |
| Normal | 0.94 | 0.97 | 0.95 | 36,287 |
| Port Scan | 0.98 | 0.40 | 0.57 | 123 |
| Reconnaissance | 0.88 | 0.95 | 0.91 | 4,870 |
| SSH Patator | 0.98 | 0.99 | 0.98 | 12,031 |
| Shellcode | 1.00 | 1.00 | 1.00 | 222 |
| Web Attack - Brute Force | 1.00 | 1.00 | 1.00 | 2,601 |
| Web Attack - SQL Injection | 0.88 | 0.78 | 0.82 | 9 |
| Web Attack - XSS | 0.99 | 0.99 | 0.99 | 728 |
| Worms | 0.98 | 0.97 | 0.98 | 1,292 |
| | | | | |
| **accuracy** | | | **0.97** | **237,557** |
| **macro avg** | **0.97** | **0.93** | **0.94** | **237,557** |
| **weighted avg** | **0.97** | **0.97** | **0.97** | **237,557** |

