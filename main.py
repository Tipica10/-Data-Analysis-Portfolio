import requests
from datetime import datetime as dt, timedelta
from twilio.rest import Client
from dotenv import (load_dotenv)
import os

load_dotenv()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
stocks_api_key = os.environ.get("STOCKS_APIKEY")
news_api_key = os.environ.get("NEW_APIKEY")

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

up_or_down = ""

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
parameters ={
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": stocks_api_key,
}
response = requests.get(url=STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()
# yesterday = dt.now() - timedelta(days=1)
# formatted_date = yesterday.strftime('%Y-%m-%d')
# yesterdays_closing_price = data['Time Series (Daily)'][formatted_date]["4. close"]
#TODO 2. - Get the day before yesterday's closing stock price

# day_before_yesterday = (dt.now() - timedelta(days=2)).date() #didn't work intially because this is a date object and can't just put in a dict calling thing, need to format it as string
# day_before_yesterday_date = day_before_yesterday.strftime('%Y-%m-%d')
#this original methodology does not exclude weekends which would be a bug
# so...
available_dates = sorted(data["Time Series (Daily)"].keys(), reverse=True)
yesterdays_closing_price = float(data["Time Series (Daily)"][available_dates[0]]["4. close"])
day_before_yesterday_closing = float(data["Time Series (Daily)"][available_dates[1]]["4. close"])

# day_before_yesterday_closing = data['Time Series (Daily)'][day_before_yesterday_date]["4. close"]

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
actual_difference = float(yesterdays_closing_price) - float( day_before_yesterday_closing)
difference = abs(actual_difference)

if actual_difference < 0:
    up_or_down = "🔻"
else:
    up_or_down = "🔺"

# #TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage_difference = (difference/float(yesterdays_closing_price) ) * 100
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

if percentage_difference > 5:
    parameters = {
        "apiKey": news_api_key,
        "q": "Tesla"

    }
    news_response = requests.get(url=NEWS_ENDPOINT,params=parameters)
    news_response.raise_for_status()
    news_data = news_response.json()
    list_news = news_data['articles']
    first_three = list_news[:3]

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    first_three_formatted = [
                        f"Headline: {article['title']}\nBrief: {article['description']}" #used join() method
                        for article in first_three
                            ]
# TODO 9. - Send each article as a separate message via Twilio.
    account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
    auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

    client = Client(account_sid, auth_token)
    for article in first_three_formatted:
        message = client.messages.create(
        from_="whatsapp:+14155238886",
        body=
        f"{STOCK_NAME}: {up_or_down}{percentage_difference}%"
        f"{article}",
        to="whatsapp:+447405101447"
        )
        print(message.sid)



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

