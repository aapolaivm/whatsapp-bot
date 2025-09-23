import os
from flask import Flask, request
from serpapi import GoogleSearch
import requests
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv

# load .env file
load_dotenv()


app = Flask(__name__)

@app.route("/", methods=["POST"])

# chatbot logic
def bot():

    # user input
    user_msg = request.values.get('Body', '').lower()

    # creating object of MessageResponsse
    response = MessagingResponse()

    # User Query 
    q = user_msg + " geegsforgeegs.org"

    # query paramters
    params = {
        "q": q,  
        "api_key": os.getenv("SERPAPI_KEY"),
        "num": 3
    }

    # searching storing responce from Google
    search = GoogleSearch(params)
    results = search.get_dict()

    organic_results = results.get("organic_results", [])
    
    # displaying urls
    if organic_results:
        message_text = f"--- Results for '{user_msg}' ---\n\n"
        for r in organic_results:
            title = r.get("title", "No title")
            link = r.get("link", "No link")
            message_text += f"{title}\n{link}\n\n"
    else:
        message_text = f"No results found for '{user_msg}'"
    
    response.message(message_text)
    return str(response)

if __name__ == "__main__":
    app.run()

