import streamlit as st
import openai
from textblob import TextBlob
import pandas as pd
import requests
import random

# Change it to your open ai api key
openai.api_key = 'your_openai_api_key'


# Function to generate a response from GPT-3
def generate_response(text, sentiment):
    text = text.lower()

    negative_responses = [
        "I'm really sorry you're feeling this way. Want to share what happened? 💙",
        "That sounds really tough. I'm here to listen if you'd like to talk.",
        "It’s okay to have bad days. You're not alone in this.",
        "I'm sorry you're going through this. Take a deep breath—we can talk it through.",
    ]

    stress_responses = [
        "It sounds like you're stressed. Maybe try taking a short break or deep breathing.",
        "Stress can be overwhelming. Want to talk about what's causing it?",
    ]

    sad_responses = [
        "I'm really sorry you're feeling sad. Do you want to share more?",
        "Sadness can feel heavy. I'm here with you 💙",
    ]

    positive_responses = [
        "That's great to hear! Keep that positive energy going 😊",
        "I'm glad you're feeling good! What made your day better?",
    ]

    neutral_responses = [
        "I understand how you're feeling. Would you like to talk more?",
        "I'm here for you. Tell me what's on your mind.",
    ]

    try:
        # keyword-based smarter replies
        if "stress" in text:
            return random.choice(stress_responses)

        elif "sad" in text or "bad day" in text or "terrible" in text:
            return random.choice(sad_responses)

        elif sentiment == "Negative":
            return random.choice(negative_responses)

        elif sentiment == "Positive":
            return random.choice(positive_responses)

        else:
            return random.choice(neutral_responses)

    except Exception as e:
        return f"Error generating response: {str(e)}"

# Analyze sentiment
def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0.5:
        return "Very Positive", polarity
    elif 0.1 < polarity <= 0.5:
        return "Positive", polarity
    elif -0.1 <= polarity <= 0.1:
        return "Neutral", polarity
    elif -0.5 < polarity < -0.1:
        return "Negative", polarity
    else:
        return "Very Negative", polarity


# Provide coping strategies
def provide_coping_strategy(sentiment):
    strategies = {
        "Very Positive": "Keep up the positive vibes! Consider sharing your good mood with others.",
        "Positive": "It's great to see you're feeling positive. Keep doing what you're doing!",
        "Neutral": "Feeling neutral is okay. Consider engaging in activities you enjoy.",
        "Negative": "It seems you're feeling down. Try to take a break and do something relaxing.",
        "Very Negative": "I'm sorry to hear that you're feeling very negative. Consider talking to a friend or seeking professional help."
    }
    return strategies.get(sentiment, "Keep going, you're doing great!")


# Disclaimer regarding data privacy
def display_disclaimer():
    st.sidebar.markdown(
        "<h2 style='color: #FF5733;'>Data Privacy Disclaimer</h2>",
        unsafe_allow_html=True
    )
    st.sidebar.markdown(
        "<span style='color: #FF5733;'>This application stores your session data, including your messages and "
        "sentiment analysis results, in temporary storage during your session. "
        "This data is not stored permanently and is used solely to improve your interaction with the chatbot. "
        "Please avoid sharing personal or sensitive information during your conversation.</span>",
        unsafe_allow_html=True
    )

st.title("Mental Health Support Chatbot")

if 'messages' not in st.session_state:
    st.session_state['messages'] = []
if 'mood_tracker' not in st.session_state:
    st.session_state['mood_tracker'] = []

with st.form(key='chat_form'):
    user_message = st.text_input("You:")
    submit_button = st.form_submit_button(label='Send')

if submit_button and user_message:
    st.session_state['messages'].append(("You", user_message))

    sentiment, polarity = analyze_sentiment(user_message)
    coping_strategy = provide_coping_strategy(sentiment)

    response = generate_response(user_message)

    st.session_state['messages'].append(("Bot", response))
    st.session_state['mood_tracker'].append((user_message, sentiment, polarity))

for sender, message in st.session_state['messages']:
    if sender == "You":
        st.text(f"You: {message}")
    else:
        st.text(f"Bot: {message}")

# Display mood tracking chart
if st.session_state['mood_tracker']:
    mood_data = pd.DataFrame(st.session_state['mood_tracker'], columns=["Message", "Sentiment", "Polarity"])
    st.line_chart(mood_data['Polarity'])

# Display coping strategies
if user_message:
    st.write(f"Suggested Coping Strategy: {coping_strategy}")

# Display resources
st.sidebar.title("Resources")
st.sidebar.write("If you need immediate help, please contact one of the following resources:")
st.sidebar.write("1. National Suicide Prevention Lifeline: 1-800-273-8255")
st.sidebar.write("2. Crisis Text Line: Text 'HELLO' to 741741")
st.sidebar.write("[More Resources](https://www.mentalhealth.gov/get-help/immediate-help)")

# Display session summary
if st.sidebar.button("Show Session Summary"):
    st.sidebar.write("### Session Summary")
    for i, (message, sentiment, polarity) in enumerate(st.session_state['mood_tracker']):
        st.sidebar.write(f"{i + 1}. {message} - Sentiment: {sentiment} (Polarity: {polarity})")


display_disclaimer()