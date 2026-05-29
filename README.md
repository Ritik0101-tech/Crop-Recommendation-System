# 🌱 AI Smart Crop Recommendation System

An AI-powered web application that recommends the most suitable crop based on soil and environmental conditions. The system uses Machine Learning to analyze input parameters and provide accurate crop recommendations along with crop information and guidance.

## 🚀 Features

- User Registration and Login
- Crop Prediction using Machine Learning
- Input Parameters:
  - Nitrogen (N)
  - Phosphorus (P)
  - Potassium (K)
  - Temperature
  - Humidity
  - pH Value
  - Rainfall
- Displays Recommended Crop
- Crop Images
- Farming Advice and Information
- Responsive User Interface
- Password Recovery Feature
- Data Validation for User Inputs

## 🛠️ Technologies Used

### Frontend
- HTML
- CSS
- JavaScript
- Bootstrap

### Backend
- Python
- Flask

### Machine Learning
- Scikit-learn
- Pandas
- NumPy

### Database
- SQLite / MySQL

## 📂 Project Structure
Crop-app/
│
├── app.py
├── train.py
├── requirements.txt
├── database.db
│
├── model/
│   ├── crop_model.pkl
│   ├── label_encoder.pkl
│   └── scaler.pkl
│
├── datasets/
│   ├── Crop_recommendation.csv
│   ├── Indian_Agriculture_Dataset.csv
│   └── Soil_State_District_Data.csv
│
├── templates/
│   ├── index.html
│   ├── dashboard.html
│   ├── login.html
│   ├── register.html
│   ├── forgot_password.html
│   ├── result.html
│   ├── advice.html
│   └── history.html
│
├── static/
│   │
│   ├── css/
│   │   └── style.css
│   │
│   ├── js/
│   │   └── app.js
│   │
│   ├── images/
│   │   ├── logo.png
│   │   │
│   │   └── crops/
│   │       ├── apple.jpg
│   │       ├── banana.jpg
│   │       ├── blackgram.jpg
│   │       ├── chickpea.jpg
│   │       ├── coconut.jpg
│   │       ├── coffee.jpg
│   │       ├── cotton.jpg
│   │       ├── grapes.jpg
│   │       ├── jute.jpg
│   │       ├── kidneybeans.jpg
│   │       ├── lentil.jpg
│   │       ├── maize.jpg
│   │       ├── mango.jpg
│   │       ├── mungbean.jpg
│   │       ├── muskmelon.jpg
│   │       ├── orange.jpg
│   │       ├── papaya.jpg
│   │       ├── pigeonpeas.jpg
│   │       ├── pomegranate.jpg
│   │       ├── rice.jpg
│   │       ├── watermelon.jpg
│   │       └── wheat.jpg
│   │
│   ├── videos/
│   │   └── loading.mp4
│   │
│   └── data/
│       └── india_data.json
│
├── utils/
│   ├── __init__.py
│   ├── weather.py
│   ├── fertilizer.py
│   ├── soil.py
│   ├── tips.py
│   └── database.py
│
└── migrations/
