import telebot
import config 
from bs4 import BeautifulSoup
import requests

def welcome_message(): 
	welcome_string = (
		"Hi, I'm Snowy! Tell me something to do:\n"
		"/movies: Movies to watch\n"
		"/news: News headlines\n"
		)
	return welcome_string

def retrieve_news():
	# response = requests.get('http://news.google.com')
	# if (response.status_code == 200):
	#     soup = BeautifulSoup(response.text, 'lxml')
	#     news = soup.find_all('span', 'titletext').text
	    
def retrieve_movies():
	pass

bot = telebot.TeleBot(config.user['TOKEN'])

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, welcome_message())

@bot.message_handler(commands=['news'])
def send_news(message):
    bot.reply_to(message, retrieve_news())

bot.polling()
