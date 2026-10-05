# Mini Image Classifier

A simple Deep Learning web application that classifies uploaded images using a pre-trained **ResNet-18** model and provides the predicted object along with its confidence score.

## Project Overview

This project demonstrates how a pre-trained Deep Learning model can be integrated with a web application and deployed online.

The application uses:

* **PyTorch** – Deep Learning framework
* **ResNet-18** – Pre-trained image classification model
* **FastAPI** – Backend API
* **HTML, CSS, JavaScript** – Frontend
* **GitHub** – Source code repository
* **Render** – Cloud deployment platform

## Features

* Upload an image through the web interface
* Display the uploaded image
* Classify the image using ResNet-18
* Display the predicted object
* Display prediction confidence
* REST API endpoint for prediction
* Health-check endpoint
* Web-based interface accessible through a browser

## Project Structure

```text
mini-image-classifier/
│
├── app.py
├── index.html
├── requirements.txt
├── .python-version
├── .gitignore
│
├── css/
│   └── style.css
│
└── js/
    └── script.js
```

## How It Works

The application follows this workflow:

```text
User uploads image
        ↓
Frontend sends image to FastAPI
        ↓
Image is preprocessed
        ↓
ResNet-18 processes the image
        ↓
Prediction probabilities are calculated
        ↓
Highest-probability class is selected
        ↓
Prediction + confidence are returned
        ↓
Result displayed on webpage
```

## API Endpoints

### Home Page

```text
GET /
```

Opens the web application.

### Health Check

```text
GET /health
```

Returns:

```json
{
  "status": "ok"
}
```

### Image Prediction

```text
POST /predict
```

Accepts an image file and returns the predicted class and confidence.

Example response:

```json
{
  "prediction": "golden retriever",
  "confidence": 97.38
}
```

## Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/rupamsah0123/mini-image-classifier.git
cd mini-image-classifier
```

### 2. Create a virtual environment

```bash
py -3.13 -m venv venv
```

### 3. Activate the environment

Windows PowerShell:

```bash
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Start the application

```bash
uvicorn app:app --reload
```

Open the application in your browser:

```text
http://127.0.0.1:8000
```

API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

## Deployment

The application is designed to be deployed using **GitHub and Render**.

Deployment process:

```text
Local Project
     ↓
GitHub Repository
     ↓
Render Web Service
     ↓
Build & Deploy
     ↓
Public Web Application
```

### Render Configuration

**Build Command**

```bash
pip install -r requirements.txt
```

**Start Command**

```bash
uvicorn app:app --host 0.0.0.0 --port $PORT
```

## Technologies Used

| Technology | Purpose                 |
| ---------- | ----------------------- |
| Python     | Application development |
| PyTorch    | Deep Learning           |
| ResNet-18  | Image classification    |
| FastAPI    | Backend/API             |
| HTML       | Web structure           |
|            |                         |
