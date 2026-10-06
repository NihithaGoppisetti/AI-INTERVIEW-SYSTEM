# 🎯 AI Interview Preparation System

An AI-powered web application that helps students and job seekers prepare for technical and HR interviews through resume analysis, personalized question generation, mock interviews, AI-powered answer evaluation, and performance tracking.

## 🚀 Live Demo

👉 **[Open AI Interview Preparation System](YOUR_STREAMLIT_APP_LINK_HERE)**

> Replace `YOUR_STREAMLIT_APP_LINK_HERE` with your Streamlit deployment link.

## 📌 Project Overview

The **AI Interview Preparation System** is designed to provide a personalized interview preparation experience. Users can analyze their resumes, generate interview questions based on their job role and experience, practice answering questions, receive AI-based feedback, and review their interview performance.

## ✨ Features

* 📄 **Resume Analysis**

  * Upload and analyze a PDF resume.
  * Extract resume content for interview preparation.

* ❓ **AI Question Generation**

  * Generate interview questions based on:

    * Job role
    * Experience level
    * Question type
    * Number of questions

* 🎤 **Practice Interview**

  * Practice answering generated interview questions.
  * Receive AI-powered evaluation and feedback.

* 📊 **Performance Tracking**

  * View previous interview attempts.
  * Review answers and evaluation results.

* 🤖 **AI-Powered Evaluation**

  * Analyze interview answers.
  * Provide feedback to improve interview performance.

## 🛠️ Technologies Used

* **Python**
* **Streamlit**
* **Google Generative AI**
* **Pandas**
* **PyPDF**
* **SQLite / Database**
* **HTML & CSS**

## 📂 Project Structure

```text
AI-INTERVIEW-SYSTEM/
│
├── app.py
├── requirements.txt
├── README.md
│
├── modules/
│   ├── __init__.py
│   ├── ai_engine.py
│   ├── answer_evaluator.py
│   ├── database.py
│   └── resume_parser.py
│
└── screenshots/
    ├── home.png
    ├── resume_analysis.png
    ├── questions.png
    ├── practice.png
    └── performance.png
```

## 📸 Screenshots

### 🏠 Home Page

![Home Page](screenshots/home.png)

### 📄 Resume Analysis

![Resume Analysis](screenshots/resume_analysis.png)

### ❓ Question Generation

![Question Generation](screenshots/questions.png)

### 🎤 Practice Interview

![Practice Interview](screenshots/practice.png)

### 📊 Performance

![Performance](screenshots/performance.png)

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/NihithaGoppisetti/AI-INTERVIEW-SYSTEM.git
```

### 2. Open the project

```bash
cd AI-INTERVIEW-SYSTEM
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## 🔑 API Configuration

If the project uses an AI API key, configure it using Streamlit secrets rather than directly placing the API key in the source code.

For Streamlit deployment, add the required API key under:

```text
Settings → Secrets
```

Example:

```toml
GOOGLE_API_KEY = "your-api-key"
```

## 🔄 System Workflow

```text
User
  ↓
Upload Resume
  ↓
Resume Analysis
  ↓
Select Job Role & Experience
  ↓
Generate Interview Questions
  ↓
Practice Interview
  ↓
Submit Answer
  ↓
AI Answer Evaluation
  ↓
Performance Tracking
```

## 🎯 Objectives

* Help users prepare for interviews efficiently.
* Provide personalized interview questions.
* Analyze interview answers using AI.
* Identify strengths and areas for improvement.
* Track interview preparation performance.
* Provide an interactive and user-friendly interview preparation platform.

## 🔮 Future Enhancements

* 🎙️ Voice-based mock interviews
* 📹 Video interview analysis
* 😊 Facial expression analysis
* 🗣️ Speech and communication analysis
* 📈 Advanced performance dashboards
* 👥 Multiple user profiles
* 🏆 Interview readiness score
* 💼 Job-specific interview preparation

## 👩‍💻 Author

**Gopisetti Nihitha**

AI Interview Preparation System

## 📄 License

This project is created for educational and project purposes.
