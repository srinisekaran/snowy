import telebot
import config 
import requests
import json

def welcome_message(): 
	welcome_string = (
		"Hi, I'm Snowy! Tell me something to do:\n"
		"/movies: Movies to watch\n"
		"/news: News headlines\n"
		)
	return welcome_string

def retrieve_news():
	try: 
		response = requests.get(config.news['SOURCE'] + config.news['KEY'])
	except requests.ConnectionError:
		print('Failed to Connect to News API')
	return response

def parse_news(news_to_parse):
	news_data = news_to_parse.json()
	news_headline = (
		news_data['articles'][0]['title'] + '\n' 
		+ news_data['articles'][0]['description'] + '\n'
		+ 'To Read More: '
		+ news_data['articles'][0]['url']
		)	
	return news_headline


def retrieve_movies():
	pass

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, welcome_message())

@bot.message_handler(commands=['news'])
def send_news(message):
    bot.reply_to(message, parse_news(retrieve_news()))

bot.polling()
