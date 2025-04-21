# 📧 Spam Classifier

A simple yet powerful machine learning-based **Spam Email Classifier** 🔍 built with Python and a web interface using HTML/CSS/JavaScript. It analyzes email text and classifies it as **Spam** or **Not Spam** using a trained model and TF-IDF vectorizer.

---

## 🚀 Features

- ✉️ Classifies emails into Spam or Not Spam
- 🧠 Uses Machine Learning (Scikit-learn)
- 📊 TF-IDF Vectorization of text
- 🔍 Real-time predictions via web interface
- 🌐 Simple frontend with HTML, CSS, and JS
- 🧪 Backend powered by Flask (app.py)

---

## 🛠️ Tech Stack

**Frontend:**
- HTML5
- CSS3
- JavaScript

**Backend:**
- Python
- Flask

**Machine Learning:**
- Scikit-learn
- Pickle (for model storage)
- TF-IDF Vectorizer
- LabelEncoder

---

## 🗂️ Project Structure

```bash
├── app.py                    # Flask backend app
├── emailclassification.py    # Spam classification logic
├── home.html                 # Frontend HTML page
├── home.css                  # Styling
├── home.js                   # Frontend interaction
├── requirements.txt          # Project dependencies
└── .gitattributes
```

---

## ⚙️ How to Run Locally

1. **Clone the repo:**

```bash
git clone https://github.com/your-username/Spam_Classifier.git
cd Spam_Classifier
```

2. **Create a virtual environment and install dependencies:**

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate (Windows)
pip install -r requirements.txt
```

3. **Run the app:**

```bash
python app.py
```

4. **Go to** `http://localhost:5000` in your browser and try it out!

---

## 🧠 ML Model Info

- **Algorithm Used:** (e.g., Naive Bayes / Logistic Regression / etc.)
- **Accuracy:** ~XX% on test data
- **Preprocessing:** Stopwords removal, lowercasing, vectorization using TF-IDF
