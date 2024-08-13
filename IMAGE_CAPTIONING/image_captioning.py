import google.generativeai as genai
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

import os
import dotenv
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

def main():

    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=GOOGLE_API_KEY)

    mess = input("How can I help you?")

    message = HumanMessage(
        content=[
            {"type": "text", "text": mess},
            {"type" : "image_url", "image_url" : 'img2.jpg'}
        ]
    )

    result = llm.invoke([message])

    print(result.content)

if __name__ == "__main__":
    main()