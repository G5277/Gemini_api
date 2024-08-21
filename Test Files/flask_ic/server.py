from flask import Flask, request, jsonify
import google.generativeai as genai
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

import os
import dotenv
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY environment variable is not set")

app = Flask(__name__)


@app.route('/caption', methods=['POST'])
def caption_image():
    try:
        llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash", google_api_key=GOOGLE_API_KEY)

        image_data = request.files['image'].read()
        message = HumanMessage(
            content=[
                {"type": "text", "text": "Caption this image"},
                {"type": "image_url", "image_url": "data:image/jpg;base64," +
                    image_data.decode('base64')}
            ]
        )

        result = llm.invoke([message])
        print(result.content)

        return jsonify({'caption': result.content})
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run()
