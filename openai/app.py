#--- References:
# https://learnwithhasan.com/advanced-chatgpt-prompt-engineering-course/
# https://www.youtube.com/watch?v=-C4FCxP-QqE

import openai
import json
import requests
import streamlit as st

from decouple import config

# Set Authentication Key
openai.api_key = config('OPENAI_API_KEY')
# print(openai.Model.list())

def basic_generation(prompt):
    completion = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {
                'role': 'user',
                'content': prompt
            }
        ]
    )

    return completion.choices[0].message.content

# prompt = 'Analyze the last 7 days bitcoin prices'
# response = BasicGeneration(prompt)
# print(response)


def get_bit_coin_prices():
    # Define the API endpoint and query parameters
    url = "https://coinranking1.p.rapidapi.com/coin/Qwsogvtv82FCd/history"
    querystring = {
        "referenceCurrencyUuid": "yhjMzLPhuIDl",
        "timePeriod": "7d"
    }
    # Define the request headers with API key and host
    headers = {
        "X-RapidAPI-Key": config('X_RapidAPI_Key'),
        "X-RapidAPI-Host": "coinranking1.p.rapidapi.com"
    }
    # Send a GET request to the API endpoint with query parameters and headers
    response = requests.request(
        "GET", url, headers=headers, params=querystring)
    # Parse the response data as a JSON object
    JSONResult = json.loads(response.text)
    # Extract the "history" field from the JSON response
    history = JSONResult["data"]["history"]
    # Extract the "price" field from each element in the "history" array and add to a list
    prices = []
    for change in history:
        prices.append(change["price"])
    # Join the list of prices into a comma-separated string
    prices_list = ','.join(prices)
    # Return the comma-separated string of prices
    return prices_list


st.title('Bitcoin Analyzer With ChatGPT')
st.subheader('Get Analysis from an expert Trader')

if st.button('Analyze'):
    with st.spinner('Getting Bitcoin Prices...'):
        bit_coin_prices = get_bit_coin_prices()
        st.success('Done!')
    with st.spinner('Analyzing Bitcoin Prices...'):
        chatGPTPrompt = f"""You are an expert crypto trader with more than 10 years of experience, 
                    I will provide you with a list of bitcoin prices for the last 7 days
                    can you provide me with a technical analysis
                    of Bitcoin based on these prices. here is what I want: 
                    Price Overview, 
                    Moving Averages, 
                    Relative Strength Index (RSI),
                    Moving Average Convergence Divergence (MACD),
                    Advice and Suggestion,
                    Do I buy or sell?
                    Please be as detailed as much as you can, and explain in a way any beginner can understand. and make sure to use headings
                    Here is the price list: {bit_coin_prices}"""
    
        analysis = basic_generation(chatGPTPrompt)
        st.text_area("Analysis", analysis,
                     height=500)
        st.success('Done!')