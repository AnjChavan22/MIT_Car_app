Markdown
# 🚗 MIT Car Price Prediction App

## 📌 Project Overview
This project is a Machine Learning based web application developed using Streamlit.  
It predicts the estimated price of a used car based on user inputs such as fuel type, ownership, transmission, kilometers driven, seats, and insurance validity.

## 🎯 Features
- Predicts used car price instantly
- Simple and interactive Streamlit dashboard
- Machine Learning model trained using Scikit-learn
- User-friendly interface

## 🛠️ Technologies Used
- Python
- Pandas
- Scikit-learn
- Streamlit
- Pickle

## 📂 Project Files
- `app.py` → Streamlit main application
- `final_model.pkl` → Trained ML model
- `columns.pkl` → Model input columns
- `requirements.txt` → Required libraries

## ▶️ How to Run Project

```bash
pip install -r requirements.txt
python -m streamlit run app.py
📊 Input Parameters
Insurance Validity
Fuel Type
Number of Seats
Kilometers Driven
Ownership
Transmission
📈 Output
Predicted Car Price in Lakhs.
