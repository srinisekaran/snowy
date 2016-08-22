# Snowy
# Helpful Telegram bot
# Srinivaas Sekaran

import telebot
import config 
import requests
import json

from timer import time_track
from bs4 import BeautifulSoup


@time_track
def welcome_message(): 
	welcome_string = (
		"Hi, I'm Snowy! Tell me something to do:\n"
		"/movies: Movies to watch\n"
		"/news: News headlines\n"
		)
	return welcome_string


# News Retrieval from JSON API and Parsing

@time_track
def retrieve_news(source, key):
	try: 
		news_response = requests.get(source + key)
	except requests.ConnectionError:
		print('Failed to Connect to News API')
	return news_response

@time_track
def parse_news(news_to_parse):
	news_data = news_to_parse.json()
	news_headline = (
		news_data['articles'][0]['title'] + '\n' 
		+ news_data['articles'][0]['description'] + '\n'
		+ 'To Read More: '
		+ news_data['articles'][0]['url']
		)	
	return news_headline


# Movie Retrieval and Parsing 

@time_track
def retrieve_movies(source):
	try: 
		movie_response = requests.get(source)
	except requests.ConnectionError:
		print('Failed to Connect to Movie Wiki')
	return movie_response

@time_track
def parse_movies(data_to_parse, selector, h_class, sub_selector):
	movies_data = data_to_parse.text
	soup = BeautifulSoup(movies_data, 'lxml')

	try: 
		movies = soup.find(selector, 
			{ 'class' : h_class })
		children = [ movie.text for movie in movies.find_all(sub_selector) ]
	except: 
		print('Could not read page! Check selectors in config file.')

	movie_ret = 'Movies Playing:\n' + ('\n').join(children) 
	return movie_ret


# Bot Config, Initialization, and Handlers

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, welcome_message())

@bot.message_handler(commands=['news'])
def send_news(message):
	news_ret_val = retrieve_news(config.news['SOURCE'], config.news['KEY'])
	bot.reply_to(message, parse_news(news_ret_val))

@bot.message_handler(commands=['movies'])
def send_movies(message):
    movie_ret_val = retrieve_movies(config.movies['SOURCE'])
    bot.reply_to(message, parse_movies(
    	movie_ret_val, config.movies['SELECTOR'], 
    	config.movies['CLASS'], 
    	config.movies['SUB_SELECTOR'] ))

bot.polling()
