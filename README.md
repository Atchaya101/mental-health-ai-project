# 💬 Mental Health Support Chatbot

A simple AI-powered chatbot that provides emotional support by analyzing user input and generating empathetic responses.

---

## 📌 Project Overview

This project is a **Mental Health Support Chatbot** developed using **Python, Flask, and Streamlit**.
It allows users to express their feelings and receive supportive responses in real-time.

The system uses **basic sentiment analysis** to understand user emotions and respond accordingly.

---

## 🎯 Features

* 💬 Interactive chat interface (Streamlit)
* 🧠 Sentiment analysis (Positive / Negative / Neutral)
* 🤖 AI-style response generation
* ⚡ Real-time response using Flask API
* 🐳 Docker support for containerization
* 🌐 Lightweight and easy to run

---

## 🏗️ System Architecture

User → Streamlit UI → Flask API → Sentiment Analysis → Response Generation → Output

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **Backend:** Flask
* **Language:** Python
* **Libraries:** flask, streamlit, torch (optional)

---

## 📂 Project Structure

mental-health-ai-project/
│── app.py            # Streamlit UI
│── api.py            # Flask backend API
│── requirements.txt  # Dependencies
│── Dockerfile        # Containerization
│── README.md

---

## 🚀 How to Run the Project

### 🔹 Step 1: Clone the repository

git clone https://github.com/Atchaya101/mental-health-ai-project.git

cd mental-health-ai-project

### 🔹 Step 2: Install dependencies

pip install -r requirements.txt

### 🔹 Step 3: Run backend API

python api.py

### 🔹 Step 4: Run frontend

streamlit run app.py

---

## 🐳 Docker Usage (Optional)

### Build Docker Image

docker build -t mental-health-ai .

### Run Container

docker run -p 8501:8501 mental-health-ai

---

## 🧪 Example Usage

Input:
I feel stressed

Output:
I'm really sorry you're feeling this way. It's okay to feel stressed sometimes. You're not alone 💙

---

## 🌍 SDG Alignment

This project supports:

👉 **SDG 3: Good Health and Well-being**

By providing accessible emotional support through technology.

---

## 🚧 Limitations

* Uses simple keyword-based sentiment analysis
* Responses are rule-based
* Not a replacement for professional mental health support

---

## 🔮 Future Improvements

* Integration with advanced LLMs (GPT, etc.)
* Multi-language support
* Voice-based chatbot
* Emotion tracking dashboard

---

## ⚠️ Disclaimer

This chatbot is for **educational purposes only** and should not replace professional mental health services.

---

## 👩‍💻 Author

**Atchaya Parthipan**

---

## 📜 License

This project is licensed under the MIT License.
