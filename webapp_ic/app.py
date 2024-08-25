from flask import Flask, render_template, request, redirect, url_for
import os
from dotenv import load_dotenv
import google.generativeai as genai
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

# Load the Google API key from the .env file
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

def generate_caption(image_path, message_text):
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=GOOGLE_API_KEY)

    message = HumanMessage(
        content=[
            {"type": "text", "text": message_text},
            {"type": "image_url", "image_url": image_path}
        ]
    )

    result = llm.invoke([message])

    return result.content

@app.route('/', methods=['GET', 'POST'])
def home():
    caption = None
    if request.method == 'POST':
        # Get the image from the form
        image = request.files['image']
        message_text = request.form['message']

        # Save the image to the uploads folder
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
        image.save(image_path)

        # Generate the caption
        caption = generate_caption(image_path, message_text)

    return render_template('index.html', caption=caption)

if __name__ == '__main__':
    app.run(debug=True)