# Hybrid NLP Chatbot with MLOps Pipeline 🚀

![Architecture](architech.png)

---

# Project Overview

This project is a Hybrid NLP Chatbot built using:

- Natural Language Processing (NLP)
- Machine Learning (ML)
- Large Language Models (LLMs)
- MLOps Principles

The chatbot can:

- Understand user input using NLP techniques
- Classify user intent using Machine Learning
- Respond using predefined responses for known intents
- Use Llama 3.1 (Groq) for unknown queries
- Store conversation history
- Track model performance
- Support model versioning and retraining
- Deploy using Docker and AWS

---

# Project Objective

Build a production-ready Hybrid AI Chatbot that demonstrates:

### NLP

- Lowercasing
- Tokenization
- Stopword Removal
- Lemmatization

### Machine Learning

- TF-IDF Vectorization
- Naive Bayes Classification
- Intent Detection
- Confidence Scoring

### Generative AI

- Llama 3.1 (Groq API)

### MLOps

- Chat History Logging
- Session Memory
- Model Evaluation
- Model Versioning
- Automated Retraining
- Docker Deployment
- AWS Deployment
- Monitoring

---

# Technologies Used

## Programming Language

- Python 3.x

## NLP

- NLTK

## Machine Learning

- Scikit-Learn
- Multinomial Naive Bayes
- TF-IDF Vectorizer

## Data Processing

- Pandas
- NumPy

## Model Persistence

- Joblib

## LLM

- Llama 3.1 8B Instant
- Groq API

## MLOps

- Docker
- AWS ECR
- AWS ECS
- CloudWatch

---

# Current Architecture

```text
                   User
                     │
                     ▼
              NLP Pipeline
     (Tokenize → Stopword → Lemmatize)
                     │
                     ▼
                  TF-IDF
                     │
                     ▼
               Naive Bayes
                     │
                     ▼
            Intent Detection
                     │
         ┌───────────┴───────────┐
         │                       │
         ▼                       ▼
    Known Intent          Unknown Intent
         │                       │
         ▼                       ▼
 Response Engine          Llama 3.1 (Groq)
         │                       │
         └───────────┬───────────┘
                     ▼
                Final Response
```

---

# Project Structure

```text
AI_CHAT_BOT/
│
├── data/
│   ├── intents.csv
│   ├── sentences.txt
│   └── chat_history.csv
│
├── docs/
│
├── models/
│   ├── model.pkl
│   ├── tfidf.pkl
│   ├── label_encoder.pkl
│
├── src/
│   ├── chatbot.py
│   ├── train.py
│   ├── predict.py
│   ├── llm_service.py
│   ├── response_engine.py
│   ├── preprocessing.py
│   ├── stop_words_removal.py
│   ├── lemmatizer.py
│   ├── vectorizer.py
│   ├── evaluate.py
│   └── retrain.py
│
├── Dockerfile
├── requirements.txt
└── README.md
```

---

# Development Journey

## Phase 1 – Project Setup ✅

### Tasks

- Create GitHub Repository
- Clone Repository
- Configure Python Virtual Environment
- Install Dependencies

### Commands

```bash
python -m venv venv

venv\Scripts\activate

pip install nltk
pip install pandas
pip install numpy
pip install scikit-learn
pip install joblib
pip install groq
```

---

## Phase 2 – Basic Chatbot ✅

### Objective

Create a terminal chatbot.

### Flow

```text
User
 ↓
Input
 ↓
Response
```

### Example

```text
YOU: Hello

BOT: Hello
```

---

## Phase 3 – NLP Preprocessing ✅

### Lowercasing

Input:

```text
AWS
```

Output:

```text
aws
```

---

### Tokenization

Library:

```python
word_tokenize()
```

Input:

```text
I am learning NLP
```

Output:

```python
['i', 'am', 'learning', 'nlp']
```

---

### Stopword Removal

Input:

```python
['i', 'am', 'learning', 'nlp']
```

Output:

```python
['learning', 'nlp']
```

---

### Lemmatization

Input:

```python
['cars', 'running', 'roads']
```

Output:

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

## Phase 4 – Feature Engineering ✅

### TF-IDF

TF-IDF converts words into numerical vectors.

### Workflow

```text
Words
 ↓
TF-IDF
 ↓
Vectors
```

Example:

```text
car run road
```

becomes

```python
[0.44, 0.62, 0.18]
```

### Why TF-IDF?

Because Machine Learning algorithms cannot understand text directly.

They require numerical values.

---

## Phase 5 – Dataset Creation ✅

Dataset:

```text
data/intents.csv
```

Current Intents:

- greeting
- goodbye
- aws
- devops
- sports
- thanks
- unknown

Example:

```csv
sentence,intent

Hello,greeting
Hi,greeting

What is AWS?,aws
Explain ECS,aws

What is Kubernetes?,devops
Explain Docker,devops

Thank you,thanks

Banana cloud monkey,unknown
```

Purpose:

Train the chatbot to identify user intent.

---

---

# Phase 6 – Machine Learning Training ✅

## Algorithm Used

### Multinomial Naive Bayes

Library:

```python
from sklearn.naive_bayes import MultinomialNB
```

Why Naive Bayes?

- Fast training
- Works well with text classification
- Commonly used in NLP tasks
- Efficient for small and medium datasets

---

## Training Workflow

```text
Dataset
 ↓
NLP Preprocessing
 ↓
TF-IDF
 ↓
Label Encoding
 ↓
Naive Bayes
 ↓
Model Training
```

---

## Output Files

Generated Models:

```text
models/

model.pkl

tfidf.pkl

label_encoder.pkl
```

Purpose:

### model.pkl

Stores trained Naive Bayes model.

### tfidf.pkl

Stores trained TF-IDF vectorizer.

### label_encoder.pkl

Stores intent labels.

---

# Phase 7 – Intent Prediction ✅

## Objective

Predict user intent.

---

### Workflow

```text
User Input
 ↓
NLP Pipeline
 ↓
TF-IDF
 ↓
Model
 ↓
Intent Prediction
```

---

### Example

Input:

```text
What is AWS?
```

Output:

```text
Intent = aws
```

---

# Phase 8 – Response Engine ✅

## Objective

Generate responses for known intents.

---

### Example

```python
responses = {

"greeting":"Hello! How Can I Help You?",

"goodbye":"Goodbye! Have a Great Day!",

"aws":"AWS is Amazon Web Services.",

"devops":"DevOps combines Development and Operations."
}
```

---

### Workflow

```text
Intent
 ↓
Response Engine
 ↓
Bot Response
```

---

# Phase 9 – Confidence Scoring ✅

## Objective

Determine prediction confidence.

---

### Method

```python
model.predict_proba()
```

---

### Example

```text
Intent: aws

Confidence: 95%
```

---

### Why Confidence Matters

Without confidence:

```text
banana cloud monkey
```

may become:

```text
aws
```

incorrectly.

Confidence helps identify uncertain predictions.

---

# Phase 10 – Unknown Intent Detection ✅

## Problem

Traditional classifiers always choose a class.

Example:

```text
banana cloud monkey
```

might become:

```text
aws
```

---

## Solution

Added:

```text
unknown
```

intent.

---

### Examples

```csv
I love pizza,unknown

Banana cloud monkey,unknown

Who is Batman?,unknown

Random text,unknown
```

---

### Result

Input:

```text
banana cloud monkey
```

Output:

```text
Intent: unknown
```

---

# Phase 11 – Llama 3.1 Integration ✅

## Objective

Provide AI-generated responses for unknown questions.

---

## Model

```text
Llama 3.1 8B Instant
```

Provider:

```text
Groq
```

---

## Workflow

```text
Unknown Intent
 ↓
Groq API
 ↓
Llama 3.1
 ↓
AI Response
```

---

## Example

Input:

```text
Who is Elon Musk?
```

Output:

```text
Elon Musk is a business entrepreneur...
```

---

# Phase 12 – Hybrid AI Architecture ✅

## Objective

Combine Machine Learning and Generative AI.

---

### Known Intent

```text
What is AWS?
```

↓

```text
Naive Bayes
```

↓

```text
Response Engine
```

---

### Unknown Intent

```text
Who is Elon Musk?
```

↓

```text
Llama 3.1
```

↓

```text
AI Response
```

---

## Hybrid Architecture

```text
User
 ↓
NLP
 ↓
TF-IDF
 ↓
Naive Bayes
 ↓
Intent
      |
 ┌────┴────┐
 │         │
Known   Unknown
 │         │
 ▼         ▼
Response   Llama 3.1
Engine     (Groq)
 │         │
 └────┬────┘
      ▼
Final Response
```

---

# Phase 13 – Chat History Logging 🔄

## Objective

Store chatbot conversations.

---

## File

```text
data/chat_history.csv
```

---

## Structure

```csv
timestamp,user_input,bot_response,intent,confidence
```

---

## Example

```csv
2026-06-15 12:00:00,hello,Hello!,greeting,0.95

2026-06-15 12:01:00,who is elon musk,<llama response>,unknown,0.32
```

---

# Phase 14 – Session Memory 🔄

## Objective

Allow chatbot to remember context.

---

### Example

User:

```text
My name is Dezosa
```

Later:

```text
What is my name?
```

Bot:

```text
Your name is Dezosa
```

---

# Phase 15 – Model Evaluation 🔄

## Objective

Measure model performance.

---

## Metrics

### Accuracy

```python
accuracy_score()
```

---

### Classification Report

```python
classification_report()
```

---

### Confusion Matrix

```python
confusion_matrix()
```

---

## Example Output

```text
Accuracy: 94%
```

---

# Phase 16 – Model Versioning 🔄

## Objective

Track multiple model versions.

---

## Structure

```text
models/

model_v1.pkl

model_v2.pkl

model_v3.pkl
```

---

## Benefits

- Rollback capability
- Performance comparison
- Audit trail

---

# Phase 17 – Experiment Tracking 🔄

## Objective

Track model improvements.

---

## File

```text
models/model_metrics.csv
```

---

## Example

```csv
version,accuracy,date

v1,92.1,2026-06-15

v2,94.5,2026-06-20
```

---

# Phase 18 – Automated Retraining 🔄

## Objective

Automatically retrain model when data changes.

---

## Workflow

```text
New Intent Added
 ↓
intents.csv Updated
 ↓
retrain.py
 ↓
New Model Generated
```

---

# Phase 19 – Docker 🔄

## Objective

Containerize application.

---

## Docker Build

```bash
docker build -t chatbot-mlops .
```

---

## Docker Run

```bash
docker run chatbot-mlops
```

---

# Phase 20 – AWS Deployment 🔄

## Option A (Recommended)

```text
Docker
 ↓
AWS ECR
 ↓
AWS ECS
 ↓
Running Chatbot
```

---

## Option B (Advanced MLOps)

```text
Model
 ↓
AWS S3
 ↓
SageMaker
 ↓
Inference Endpoint
```

---

# Phase 21 – Monitoring 🔄

## Tools

- CloudWatch Logs
- CloudWatch Metrics

---

## Monitor

- Prediction Confidence
- Unknown Intents
- Response Time
- Error Rate
- CPU Usage
- Memory Usage

---

# Final MLOps Architecture

```text
                   User
                     │
                     ▼
              NLP Pipeline
     (Tokenize → Stopword → Lemmatize)
                     │
                     ▼
                  TF-IDF
                     │
                     ▼
               Naive Bayes
                     │
                     ▼
            Intent Detection
                     │
         ┌───────────┴───────────┐
         │                       │
         ▼                       ▼
    Known Intent          Unknown Intent
         │                       │
         ▼                       ▼
 Response Engine          Llama 3.1 (Groq)
         │                       │
         └───────────┬───────────┘
                     ▼
                Response
                     │
                     ▼
             Chat History
                     │
                     ▼
             Model Metrics
                     │
                     ▼
            Model Versioning
                     │
                     ▼
             Automated Retraining
                     │
                     ▼
                 Docker
                     │
                     ▼
                AWS ECS
                     │
                     ▼
               CloudWatch
```

---

# Resume Description

Built a Hybrid NLP Chatbot using NLTK, TF-IDF, Naive Bayes, and Llama 3.1 (Groq). Implemented intent classification, confidence scoring, unknown intent detection, hybrid AI routing, and designed an end-to-end MLOps pipeline including model evaluation, versioning, retraining, containerization, AWS deployment, and monitoring.

---

# Deliverables

## Source Code

```text
src/
```

## Dataset

```text
data/intents.csv
```

## Trained Models

```text
models/
```

## Documentation

```text
README.md
```

## Deployment

```text
Dockerfile
```

---

# Completion Criteria

Project is complete when:

✅ NLP Pipeline works

✅ Intent Classification works

✅ Llama Integration works

✅ Chat History Logging works

✅ Session Memory works

✅ Model Evaluation completed

✅ Model Versioning implemented

✅ Automated Retraining implemented

✅ Docker image runs successfully

✅ AWS deployment works

✅ Monitoring works

---

# Author

Karop Dezosa S

Cloud Engineer | DevOps Engineer | NLP & MLOps Enthusiast