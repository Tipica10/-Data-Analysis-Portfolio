Stock Trading News Alert Bot
Problem / Objective

Manually tracking significant daily price swings on a watched stock — and finding the news that might explain them — is slow and easy to miss. The goal was to automate this end to end: detect a meaningful price move and immediately surface relevant news, delivered straight to a phone.

Approach
Tools: Python, Alpha Vantage API, NewsAPI, Twilio
Pulled daily open/close stock prices from the Alpha Vantage API
Calculated the day-over-day percentage change
If the change crossed a set threshold (e.g. ±5%), queried NewsAPI for the top related headlines
Sent an SMS containing the price move and relevant headlines via Twilio
Chained three separate third-party APIs into a single automated pipeline, with response parsing and key-safety handling (.get() over direct key access) throughout
