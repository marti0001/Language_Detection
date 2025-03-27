# 🌍 Language Detection Project – NLP with Multinomial Naive Bayes  

This project focuses on **automatic text language detection** using **Multinomial Naive Bayes** and **TF-IDF Vectorization**. The model is trained on a **custom dataset** with 14 languages, including **English, Spanish, French, Polish**, and more.  

<p align="center">
  <img src="https://img.shields.io/badge/Naive--Bayes-228B22?style=for-the-badge&logo=scikitlearn&logoColor=white" alt="Naive Bayes"/>
  <img src="https://img.shields.io/badge/Web%20Scraping-FF4500?style=for-the-badge&logo=web&logoColor=white" alt="Web Scraping"/>
  <img src="https://img.shields.io/badge/BeautifulSoup-4B275F?style=for-the-badge&logo=beautifulsoup&logoColor=white" alt="BeautifulSoup"/>
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas"/>
  <img src="https://img.shields.io/badge/Numpy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy"/>
  <img src="https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=plotly&logoColor=white" alt="Matplotlib"/>
    <img src="https://img.shields.io/badge/Docker-11557C?style=for-the-badge&logo=plotly&logoColor=white" alt="Docker"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI"/>
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker"/>
  <img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white" alt="Scikit-learn"/>
</p>

---


## 🔍 **Project Description**  

The primary goal of this project is to **automatically detect the language** of short text samples using **Natural Language Processing (NLP)** techniques. The dataset was created by **web scraping** multilingual text from **Wikipedia**, followed by **TF-IDF Vectorization** and **Multinomial Naive Bayes** for classification.  


✅ **API Ready** – Built with **FastAPI** for real-time language detection.  
✅ **Dockerized** – Fully containerized for seamless deployment.  
✅ **Custom Dataset** – Web scraped text data from Wikipedia for multilingual training. 

---

## 🏗️ **Project Structure**  

### 📥 **1. Custom Dataset Creation**  
✔ **Web scraping** text data from Wikipedia in **14 languages**.  
✔ Topics include **Wikipedia**, **Pi**, **Microsoft**, **Adidas**, and others.  

### 🧹 **2. Text Cleaning & Preprocessing**  
✔ Removed **special characters** and **digits** for consistent preprocessing.  
✔ **TF-IDF vectorization** with **unigrams** and **bigrams** for feature extraction.  

### 📊 **3. Data Visualization**  
✔ Showcased **language distribution** in the dataset using **seaborn** and **matplotlib**.  

### 🏃 **4. Model Training**  
✔ Used **Multinomial Naive Bayes** for classification.  
✔ **Hyperparameter tuning** (alpha) via **GridSearchCV**.  

### 📈 **5. Model Evaluation**  
✔ Evaluated performance using:  
- **Confusion matrix**  
- **Classification report**  
- **Accuracy score**  

### 🌐 **6. API Development (FastAPI)**  
✔ Developed a **FastAPI** application for real-time language detection.  
✔ Hosted using **Uvicorn**, with an **interactive web interface** for user input.  

### 🐳 **7. Dockerization**  
✔ **Containerized** the entire project using **Docker**.  
✔ Ensures **portability** and **easy deployment** across different environments.  

---
## 🚀 Project Structure  

```bash
📦 Language_Detection
├── 📁 input
│   ├── Sample_Language.csv                             # My Scrap Dataset 
├── 📁 app
│   ├── 📁 templates
│   │   ├── index.html
│   ├── 📁 model
│   │   ├── Pipeline_and_model_Language_Detection-0.1.0.pkl # Model 
│   ├── 🐍 main.py
├── 📁 notebooks
│   ├── Language_Detection__Web_Scraping.ipynb          # Web_Scraping
│   ├── Language_Detection_TfidfVectorizer.ipynb        # Analysis Preprocessing, Training
├── 📄 README.md
├── 🐳 Dockerfile           # Container configuration
├── 📛 .dockerignore        # Docker exclusion rules
├── 📛 .gitignore           # Git exclusion rules
└── 📜 requirements.txt     # requirements
```
---

## 🛠 **Technologies & Tools**  


## 🛠️ **Technologies & Tools**  

| **Category**           | **Tools & Libraries**                      |
|--------------------------|------------------------------------------|
| **Programming Language** | Python                                   |
| **Web Scraping**          | BeautifulSoup, requests                  |
| **Data Manipulation**     | pandas, numpy                            |
| **Machine Learning**      | scikit-learn (TF-IDF, Naive Bayes)       |
| **API Development**       | FastAPI, Uvicorn                         |
| **Dockerization**         | Docker                                   |
| **Visualization**         | seaborn, matplotlib                      |
---

## 🏗️ Build and Run with Docker:  

```bash
# Clone repository
git clone https://github.com/marti0001/MNIST-Digit-Classification

# Build Docker image
docker build -t language_detection_app .

# Run container
docker run -p 8000:8000 language_detection_app

#Open your browser and go to
http://localhost:8000
```
