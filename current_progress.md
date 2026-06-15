# AI ChatBot Project (NLP + Machine Learning + AI + DevOps)

## Project Goal

Build an intelligent chatbot that demonstrates:

* Natural Language Processing (NLP)
* Machine Learning (ML)
* Intent Classification
* AI Integration (OpenAI/Gemini)
* DevOps Deployment (Docker, Jenkins, AWS ECS)

---

# Current Project Structure

```text
AI_CHAT_BOT/
│
├── data/
│   └── sentences.txt
│
├── docs/
│
├── models/
│
├── src/
│   ├── chatbot.py
│   ├── preprocessing.py
│   ├── stop_words_removal.py
│   ├── lemmatizer.py
│   └── vectorizer.py
│
├── README.md
└── requirements.txt
```

---

# Project Phases

## Phase 1: Project Setup

### Completed

* Created GitHub repository
* Cloned repository into VS Code
* Created project folder structure
* Configured Python environment

---

## Phase 2: Basic Terminal Chatbot

### Objective

Create a chatbot that can accept user input continuously.

### Implementation

```python
while True:
    user_input = input("You: ")
```

### Example

```text
You: Hello

KDS: Hello
```

### Status

✅ Completed

---

## Phase 3: Text Preprocessing

### Objective

Normalize text before NLP processing.

### Implementation

```python
text.lower()
```

### Example

Input:

```text
AWS
```

Output:

```text
aws
```

### Status

✅ Completed

---

## Phase 4: Tokenization

### Objective

Convert a sentence into individual tokens (words).

### Library

NLTK

### Implementation

```python
word_tokenize(text)
```

### Example

Input:

```text
I am learning NLP
```

Output:

```python
['i', 'am', 'learning', 'nlp']
```

### Status

✅ Completed

---

## Phase 5: Stop Word Removal

### Objective

Remove common words that do not contribute significant meaning.

### Library

NLTK Stopwords

### Example

Before:

```python
['i', 'am', 'learning', 'nlp']
```

After:

```python
['learning', 'nlp']
```

### Status

✅ Completed

---

## Phase 6: Lemmatization

### Objective

Convert words into their dictionary (root) form.

### Library

WordNetLemmatizer

### Example

Before:

```python
['cars', 'running', 'roads']
```

After:

```python
['car', 'run', 'road']
```

### Status

✅ Completed

---

## Current NLP Pipeline

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

### Example

Input:

```text
The cars are running on roads
```

Output:

```python
['car', 'run', 'road']
```

---

## Phase 7: TF-IDF Vectorization

### Objective

Convert text into numerical vectors for machine learning.

### Library

Scikit-Learn

### Component

```python
TfidfVectorizer()
```

### Example

Input:

```text
car run road
```

Output:

```python
[0.41, 0.72, 0.18]
```

### Why?

Machine learning algorithms cannot understand words directly.

They require numerical features.

### Status

✅ Basic Implementation Completed

---

# Current Project Flow

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
      ↓
TF-IDF
```

---

# Upcoming Phases

## Phase 8: Intent Dataset Creation

### File

```text
data/intents.csv
```

### Example

```csv
sentence,intent

Hi,greeting
Hello,greeting
Good morning,greeting

Bye,goodbye
Goodbye,goodbye

What is AWS?,aws
Explain ECS,aws

What is Kubernetes?,devops
Explain Docker,devops
```

### Purpose

Teach the chatbot different categories (intents).

### Status

⬜ Pending

---

## Phase 9: Model Training

### File

```text
src/train.py
```

### Workflow

```text
Dataset
   ↓
TF-IDF
   ↓
Naive Bayes
   ↓
Train Model
   ↓
Save Model
```

### Output

```text
models/model.pkl
```

### Status

⬜ Pending

---

## Phase 10: Intent Prediction

### Workflow

```text
User Input
      ↓
Preprocessing
      ↓
TF-IDF
      ↓
Trained Model
      ↓
Intent Prediction
```

### Example

Input:

```text
What is ECS?
```

Output:

```text
Intent = AWS
```

### Status

⬜ Pending

---

## Phase 11: AI Integration

### Tools

* OpenAI API
* Gemini API

### Workflow

```text
Intent Detection
      ↓
LLM
      ↓
Generate Response
```

### Status

⬜ Pending

---

## Phase 12: Database Integration

### Database

SQLite

### Store

* User Message
* Bot Response
* Timestamp

### Status

⬜ Pending

---

## Phase 13: DevOps Deployment

### Containerization

Docker

### CI/CD

GitHub → Jenkins

### Deployment

AWS ECS

### Monitoring

CloudWatch

### Status

⬜ Pending

---

# Final Architecture

```text
User
 ↓
Preprocessing
 ↓
Tokenization
 ↓
Stopword Removal
 ↓
Lemmatization
 ↓
TF-IDF
 ↓
Naive Bayes
 ↓
Intent Detection
 ↓
OpenAI/Gemini
 ↓
Response
 ↓
SQLite
 ↓
Docker
 ↓
Jenkins
 ↓
AWS ECS
```

---

# Progress Tracker

| Phase                | Status |
| -------------------- | ------ |
| Project Setup        | ✅      |
| Terminal Chatbot     | ✅      |
| Lowercasing          | ✅      |
| Tokenization         | ✅      |
| Stopword Removal     | ✅      |
| Lemmatization        | ✅      |
| TF-IDF Basics        | ✅      |
| Intent Dataset       | ⬜      |
| Naive Bayes Training | ⬜      |
| Intent Prediction    | ⬜      |
| OpenAI Integration   | ⬜      |
| SQLite               | ⬜      |
| Docker               | ⬜      |
| Jenkins              | ⬜      |
| ECS Deployment       | ⬜      |

---

## Current Completion

Approximately **35% Complete**

Next milestone:

**Create `data/intents.csv` and train the first Naive Bayes intent classification model.**
