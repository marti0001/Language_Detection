# 🌍 Language Detection Project – NLP with Multinomial Naive Bayes  

This project focuses on **automatic text language detection** using **Multinomial Naive Bayes** and **TF-IDF Vectorization**. The model is trained on a **custom dataset** with 14 languages, including **English, Spanish, French, Polish**, and more.  

<p align="center">
  <img src="https://img.shields.io/badge/Naive--Bayes-228B22?style=for-the-badge&logo=scikitlearn&logoColor=white" alt="Naive Bayes"/>
  <img src="https://img.shields.io/badge/Web%20Scraping-FF4500?style=for-the-badge&logo=web&logoColor=white" alt="Web Scraping"/>
  <img src="https://img.shields.io/badge/BeautifulSoup-4B275F?style=for-the-badge&logo=beautifulsoup&logoColor=white" alt="BeautifulSoup"/>
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas"/>
  <img src="https://img.shields.io/badge/Numpy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy"/>
  <img src="https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=plotly&logoColor=white" alt="Matplotlib"/>
</p>

---

## 🔍 **Project Description**  

The primary goal of this project is to **automatically detect the language** of short text samples using **Natural Language Processing (NLP)** techniques. The dataset was created by **web scraping** multilingual text from **Wikipedia**, followed by **TF-IDF Vectorization** and **Multinomial Naive Bayes** for classification.  

### ✨ **Latest Update**  
- Created a **custom dataset** by scraping Wikipedia pages.  
- Expanded the dataset to **14 languages**, including:  
  > 🇺🇸 English, 🇪🇸 Spanish, 🇫🇷 French, 🇩🇪 German, 🇮🇹 Italian, 🇵🇹 Portuguese, 🇷🇺 Russian, 🇵🇱 Polish, 🇺🇦 Ukrainian, 🇳🇱 Dutch, 🇸🇪 Swedish, 🇫🇮 Finnish, 🇳🇴 Norwegian, 🇩🇰 Danish.  
- Improved dataset **diversity** by scraping a variety of topics (e.g., **Wikipedia**, **Pi**, **Microsoft**, **Adidas**).  

---

## 🎯 **Key Features**  

### 🛠 **1. Web Scraping**  
- Collected **multilingual text data** from **Wikipedia** for **14 languages**.  

### 🧹 **2. Text Cleaning**  
- Removed **special characters**, **digits**, and standardized input text.  

### 📊 **3. Data Visualization**  
- Visualized **language distribution** and dataset balance using **Seaborn** & **Matplotlib**.  

### 🧮 **4. TF-IDF Vectorization**  
- Extracted features using **unigrams** and **bigrams** for better language differentiation.  

### 🔍 **5. Model Training & Optimization**  
- Trained a **Multinomial Naive Bayes** classifier.  
- Tuned the **alpha hyperparameter** using **GridSearchCV**.  

### 📈 **6. Evaluation**  
- Performance metrics include:  
  - **Confusion Matrix** for error analysis.  
  - **Classification Report** for precision, recall, and F1-score.  
  - **Accuracy Score** on the custom dataset.  

### 🏗️ **7. Model Deployment**  
- Exported the final model as a **.pkl file** for future use.  

---
## 🚀 Project Structure  

```bash
📦 Language_Detection
├── 📁 input
│   ├── Sample_Language.csv                                 # My Scrap Dataset 
├── 📁 model
│   ├── Pipeline_and_model_Language_Detection-0.1.0.pkl     # Model 
├── 📁 notebooks
│   ├── Language_Detection__Web_Scraping.ipynb              # Web_Scraping
│   ├── Language_Detection_TfidfVectorizer.ipynb            # Analysis, Preprocessing, Training
├── 📄 README.md
```
---

## 🛠 **Technologies & Tools**  

| **Category**         | **Tools & Libraries**                                 |
|-----------------------|------------------------------------------------------|
| **Programming**       | Python                                               |
| **Web Scraping**      | `BeautifulSoup`, `requests`                          |
| **Data Manipulation** | `pandas`, `numpy`                                    |
| **Machine Learning**  | `scikit-learn` (TF-IDF, Naive Bayes)                 |
| **Visualization**     | `seaborn`, `matplotlib`                              |

---
