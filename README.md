# 📩 SMS Spam Classifier

An end-to-end **Machine Learning + NLP project** that classifies SMS messages as **Spam 🚨** or **Ham ✅** using a trained ML model and an interactive **Streamlit web application**.

---

# 🚀 Project Overview

Spam messages are a common problem in digital communication.  
This project uses **Natural Language Processing (NLP)** and **Machine Learning** to automatically detect spam SMS messages.

Users can enter any SMS message in the Streamlit app and instantly receive a prediction.

---

# 🧠 Problem Statement

The objective of this project is to build a machine learning model that can classify SMS messages into:

- **Spam 🚨**
- **Ham (Not Spam) ✅**

This helps automate spam filtering and improve communication systems.

---

# 📂 Project Structure

```
sms-spam-classifier
│
├── model
│   └── model.pkl
│
├── notebook
│   └── spam_classifier.ipynb
│
├── src
│   ├── predict_pipeline.py
│   └── utils.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

### Folder Explanation

| Folder/File | Description |
|-------------|-------------|
| `model/` | Contains the trained machine learning model |
| `notebook/` | Jupyter notebook used for training and experimentation |
| `src/` | Contains the prediction pipeline and helper utilities |
| `app.py` | Streamlit web application |
| `requirements.txt` | Python dependencies |
| `README.md` | Project documentation |

---

# ⚙️ Tech Stack

| Category | Tools Used |
|--------|-------------|
| Programming Language | Python |
| NLP Library | NLTK |
| Machine Learning | Scikit-learn |
| Model | Support Vector Classifier (SVC) |
| Feature Extraction | TF-IDF Vectorization |
| Web App | Streamlit |

---

# 📊 Model Performance

The model was trained using the **SMS Spam Collection Dataset**.

| Metric | Score |
|------|------|
| Accuracy | ~98% |
| Precision | ~97% |
| Recall | ~90% |
| F1 Score | ~94% |

Confusion Matrix:

```
[[885   4]
 [ 14 131]]
```

This indicates the model performs well in identifying spam messages while keeping false positives low.

---

# 📈 Machine Learning Pipeline

The prediction pipeline works as follows:

```
Raw SMS Message
        ↓
Text Preprocessing
(lowercase, punctuation removal, stopword removal, stemming)
        ↓
TF-IDF Vectorization
        ↓
Support Vector Machine (SVC)
        ↓
Prediction (Spam / Ham)
```

---

# 📚 Dataset

Dataset used in this project:

**SMS Spam Collection Dataset**

It contains **5572 SMS messages** labeled as spam or ham.

Example records:

| Label | Message |
|------|------|
| ham | Go until jurong point, crazy.. |
| spam | Free entry in a weekly competition to win FA Cup tickets |

---

# ✨ Features

- NLP text preprocessing using **NLTK**
- TF-IDF feature extraction
- Machine learning classification using **SVC**
- Hyperparameter tuning with **GridSearchCV**
- Interactive **Streamlit UI**
- Modular project structure

---

# 🔮 Future Improvements

Possible improvements for the project:

- Spam probability score
- Spam keyword highlighting
- Message history tracking
- Model comparison dashboard
- Deep learning NLP models (LSTM / BERT)
- Deployment

---

# 👨‍💻 Author

**Ashish**

BCA Student | Aspiring Data Scientist

---

# ⭐ If you like this project

Consider giving it a **star ⭐ on GitHub**.
