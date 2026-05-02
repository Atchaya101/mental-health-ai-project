from flask import Flask, request, jsonify

app = Flask(__name__)


# 🧠 Simple sentiment detection
def detect_sentiment(text):
    text = text.lower()
    if any(word in text for word in ["sad", "depressed", "tired", "upset", "stress"]):
        return "Negative"
    elif any(word in text for word in ["happy", "good", "great", "excited"]):
        return "Positive"
    else:
        return "Neutral"


def generate_response(text, sentiment):
    try:
        if sentiment == "Negative":
            return "I'm really sorry you're feeling this way. It's okay to feel stressed sometimes. Try to take a deep breath and focus on small steps. You're not alone 💙"

        elif sentiment == "Positive":
            return "That's wonderful to hear! Keep holding onto that positivity and continue doing what makes you happy 😊"

        else:
            return "I understand how you're feeling. Would you like to talk more about what's on your mind?"

    except Exception as e:
        return f"Error generating response: {str(e)}"


# 💬 Chat API endpoint
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("text")

    sentiment = detect_sentiment(user_input)
    response = generate_response(user_input, sentiment)

    return jsonify({
        "input": user_input,
        "sentiment": sentiment,
        "response": response
    })


# 🌐 Home route
@app.route("/")
def home():
    return "Mental Health AI API is running 🚀"


# ▶️ Run server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)