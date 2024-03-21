from flask import Flask, render_template, request, jsonify

import os
from openai import OpenAI
from dotenv import load_dotenv  

# Load environment variables from .env file
load_dotenv()

# Load your OpenAI API key
api_key = os.getenv('OPENAI_API_KEY')


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('chat.html')


@app.route("/get", methods=["POST"])
def chat():
    data = request.json  # Use request.json to access the JSON data sent by AJAX
    msg = data["msg"]
    chat_messages = [{'role': 'system', 'content': 'You are a diabetes management expert.'}, {'role': 'user', 'content': msg}]
    return get_openai_response(chat_messages)

def get_openai_response(messages):
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=100,
        )
        print("Response received from OpenAI:", response)  # For debugging; remove or secure properly for production
        return jsonify({"response": response.choices[0].message.content})
    except Exception as e:
        print("Error:", e)  # For debugging; remove or secure properly for production
        return jsonify({"response": "Sorry, there was an error processing your request."})

if __name__ == '__main__':
    app.run(debug=True)