# Stock Market Anomaly Detection

This project implements a complete anomaly detection pipeline for financial time-series data using Microsoft (MSFT) stock between 2022–2025. It identifies both statistically rare events and machine-learning-based anomalies and presents the results through an interactive dashboard built with FastAPI and Plotly.

The system is modular, reproducible, and designed with production-oriented structure to demonstrate strong software engineering and data science practices.

---

## Project Objectives

- Detect abnormal movements in stock price, volatility, and volume
- Compare statistical anomaly detection with ML-based detection
- Engineer financial features for time-series analysis
- Build a backend service that responds with anomaly results
- Visualize insights through an interactive web dashboard

---

## Techniques Used

### Feature Engineering
- Daily returns
- 20-day rolling volatility
- Percentage volume change
- Feature matrix for ML models

### Statistical Method
- Z-score based anomaly detection (values > ±3 standard deviations)

### Machine Learning Method
- Isolation Forest model trained on engineered features

---

## System Architecture
Yahoo Finance → Data Loader → Feature Engineering →
Statistical Anomalies + Isolation Forest →
FastAPI Backend → Frontend Dashboard (Plotly)

---

## Tech Stack

**Backend**
- Python
- FastAPI
- Pandas
- Scikit-learn
- yfinance

**Frontend**
- HTML, CSS, JavaScript
- Plotly.js for visualization

---

## How Anomalies Are Determined

### Statistical Anomalies
A data point is flagged if:

```py
abs(return - mean) > 3 * standard deviation
```

### ML-Based Anomalies
Isolation Forest detects points that are isolated earlier in random partitions. 
Features used:

- daily_return  
- volatility_20  
- volume_change  

---

## Results Delivered by API

The API returns:

- dates  
- closing price values  
- daily returns  
- rolling volatility  
- list of statistical anomaly dates  
- list of ML anomaly dates  

These values are then visualized in the dashboard.
<img width="900" height="450" alt="newplot" src="https://github.com/user-attachments/assets/3d5c814d-1860-473d-8696-cbdccc272bd4" />

<img width="900" height="450" alt="newplot (1)" src="https://github.com/user-attachments/assets/8383eaab-38df-47c3-a589-9a3dcd31bb75" />

<img width="900" height="450" alt="newplot (2)" src="https://github.com/user-attachments/assets/0659758c-b413-4550-94d6-990c1a4e847b" />

---

## Running the Project

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Start the backend
```bash
uvicorn app.main:app --reload
```

### 3. Open the dashboard

Open with browser: app/static/index.html
<img width="1577" height="902" alt="output" src="https://github.com/user-attachments/assets/d5d2217a-a5c4-4ae6-a45a-42fae5d156c1" />

---

## Reproducibility

All data is fetched directly from Yahoo Finance using:

```py
yf.download("MSFT", start="2022-01-01", end="2025-12-31")
```
No synthetic or manually created data is used.

---

## Future Extensions

- Add multi-ticker comparison
- Integrate LSTM or Transformer models for predictive anomalies
- Add automated alerting or reporting
- Deploy backend and frontend to cloud

---

## Summary

This project demonstrates end-to-end capability in:

- financial feature engineering
- anomaly detection using both statistics and machine learning
- API development and integration
- frontend data visualization
- production-style project structuring

[def]: newplot.png
