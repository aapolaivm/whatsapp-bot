from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

# chatbot logic
def bot():

    # user input
    user_msg = request.values.get('Body', '').lower

    # creating object of MessageResponce
    response = MessageResponce()

    # User Query
    q = user_msg + "geegsforgeegs.org"

    # List to store urls
    result = []

    # searching and storing urls
    for i in search(q, tld='co.in', num=6, stop=6, pause=2):
        result.append(i)

    # displaying result
    msg = response.message(f"--- Results for '{user_msg}' ---")
    for result in search_results:
        msg = response.message(result)

    return str(response)


