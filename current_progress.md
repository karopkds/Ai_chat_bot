# AI_CHAT_BOT 🚀

## Project Overview

AI_CHAT_BOT is a Hybrid NLP + Machine Learning Chatbot built using Python.

The project demonstrates:

* Natural Language Processing (NLP)
* Machine Learning
* Intent Classification
* TF-IDF Vectorization
* Naive Bayes Classification
* Confidence Scoring
* Response Generation

Future enhancements include:

* OpenAI/Gemini Integration
* SQLite Database
* Docker Containerization
* Jenkins CI/CD
* AWS ECS Deployment

---

# Project Architecture

```text
User
 ↓
Input
 ↓
NLP Pipeline
 ├─ Lowercase
 ├─ Tokenization
 ├─ Stopword Removal
 └─ Lemmatization
 ↓
TF-IDF
 ↓
Naive Bayes
 ↓
Confidence Score
 ↓
Intent Detection
 ↓
Response Engine
 ↓
Bot Response
```

---

# Project Structure

```text
AI_CHAT_BOT/
│
├── data/
│   ├── intents.csv
│   └── sentences.txt
│
├── docs/
│
├── models/
│   ├── model.pkl
│   ├── tfidf.pkl
│   └── label_encoder.pkl
│
├── src/
│   ├── chatbot.py
│   ├── train.py
│   ├── predict.py
│   ├── preprocessing.py
│   ├── stop_words_removal.py
│   ├── lemmatizer.py
│   ├── vectorizer.py
│   └── response_engine.py
│
├── README.md
├── requirements.txt
└── Architecture_diagram.png
```

---

# Technologies Used

## Programming Language

* Python

## NLP Libraries

* NLTK

## Machine Learning

* Scikit-Learn

## Data Handling

* Pandas
* NumPy

## Model Persistence

* Joblib

---

# Development Phases

---

## Phase 1 - Project Setup ✅

Completed:

* Git Repository Setup
* VS Code Setup
* Python Virtual Environment
* Project Folder Structure

---

## Phase 2 - Basic Terminal Chatbot ✅

Created:

```python
while True:
    user_input = input("YOU: ")
```

Allows continuous user interaction.

---

## Phase 3 - NLP Preprocessing ✅

### Lowercasing

Example:

```text
AWS
```

↓

```text
aws
```

---

### Tokenization

Using:

```python
word_tokenize()
```

Example:

```text
I am learning NLP
```

↓

```python
['i', 'am', 'learning', 'nlp']
```

---

### Stopword Removal

Example:

```python
['i', 'am', 'learning', 'nlp']
```

↓

```python
['learning', 'nlp']
```

---

### Lemmatization

Example:

```python
['cars', 'running', 'roads']
```

↓

```python
['car', 'run', 'road']
```

---

# NLP Pipeline

```text
User Input
 ↓
Lowercase
 ↓
Tokenization
 ↓
Stopword Removal
 ↓
Lemmatization
```

---

## Phase 4 - TF-IDF Vectorization ✅

Implemented:

```python
TfidfVectorizer()
```

Purpose:

Convert text into numerical vectors that Machine Learning algorithms can understand.

---

## Phase 5 - Intent Dataset Creation ✅

Created:

```text
data/intents.csv
```

Current intents:

* greeting
* goodbye
* aws
* devops
* sports
* thanks

Dataset contains 70+ training examples.

Example:

```csv
sentence,intent

Hello,greeting
What is AWS?,aws
Explain Docker,devops
What is cricket?,sports
Thank you,thanks
```

---

## Phase 6 - Model Training ✅

Created:

```text
src/train.py
```

Training Pipeline:

```text
CSV Dataset
 ↓
Preprocessing
 ↓
TF-IDF
 ↓
Label Encoding
 ↓
Naive Bayes
 ↓
Model Training
 ↓
Save Model
```

Used:

```python
MultinomialNB()
```

Generated Models:

```text
models/
│
├── model.pkl
├── tfidf.pkl
└── label_encoder.pkl
```

---

## Phase 7 - Intent Prediction ✅

Created:

```text
src/predict.py
```

Workflow:

```text
User Input
 ↓
Load Model
 ↓
Predict Intent
```

Example:

```text
Hello
```

↓

```text
greeting
```

---

## Phase 8 - Response Engine ✅

Created:

```text
src/response_engine.py
```

Maps predicted intents to predefined responses.

Example:

```python
{
    "greeting": "Hello! How Can I Help You?",
    "aws": "AWS is Amazon Web Services."
}
```

---

## Phase 9 - NLP Integration into Prediction ✅

Integrated preprocessing modules into prediction pipeline.

Workflow:

```text
Input
 ↓
Lowercase
 ↓
Tokenization
 ↓
Stopword Removal
 ↓
Lemmatization
 ↓
TF-IDF
 ↓
Prediction
```

---

## Phase 10 - Confidence Score ✅

Implemented:

```python
model.predict_proba()
```

Example Output:

```text
Intent: aws
Confidence: 86%
```

Purpose:

Determine how confident the model is before responding.

---

## Phase 11 - Unknown Intent Handling ✅

Implemented threshold-based rejection.

Example:

```text
Confidence < Threshold
```

↓

```text
Sorry, I didn't understand that.
```

Prevents random incorrect responses.

---

# Current Features

✅ NLP Pipeline

✅ TF-IDF Vectorization

✅ Naive Bayes Intent Classification

✅ Confidence Scoring

✅ Unknown Intent Handling

✅ Response Engine

✅ Model Persistence

---

# Current Project Completion

```text
Project Completion ≈ 70%
```

---

# Upcoming Development

## Phase 12 - Unknown Intent Class

Add:

```csv
I love pizza,unknown
Banana cloud monkey,unknown
Tell me a joke,unknown
Random text,unknown
```

Purpose:

Improve handling of out-of-domain questions.

---

## Phase 13 - OpenAI / Gemini Integration

Future Architecture:

```text
User
 ↓
NLP
 ↓
TF-IDF
 ↓
Naive Bayes
 ↓
Intent Detection
 ↓
Known Intent?
     |
 ┌───┴────┐
 │        │
Yes       No
 │        │
 ▼        ▼
Response  OpenAI/Gemini
Engine    API
 │        │
 └───┬────┘
     ▼
Final Response
```

This transforms the project into a Hybrid AI Chatbot.

---

# Future Enhancements

## Database

* SQLite
* Conversation History
* User Sessions
* Chat Memory

---

## DevOps

### Docker

Containerize the chatbot.

### Jenkins

Automate CI/CD pipeline.

### AWS ECR

Store Docker images.

### AWS ECS

Deploy chatbot containers.

### CloudWatch

Centralized logging and monitoring.

---

# Final Goal

Build a production-style Hybrid AI Chatbot demonstrating:

* NLP
* Machine Learning
* Intent Classification
* AI Integration
* Database Management
* CI/CD
* Cloud Deployment

---

# Author

Karop Dezosa S

Cloud & DevOps Engineer | NLP & AI Enthusiast
