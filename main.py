import json
import yfinance as yf

import openai

from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

client = openai.Client()

ticker = "ABEV3"
period = "5d" #1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max

ticker_obj = yf.Ticker(f"{ticker}.SA")

ticker_obj.history()