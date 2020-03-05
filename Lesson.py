import telebot
import pyowm

owm = pyowm.OWM('fb9a4eb5b6fc2b1ee8bfb45a816b7cba', language = "ru")

bot = telebot.TeleBot("1128092060:AAEvV5oxWbCSvQ0tUMPxyg1ZBuvL-3cFKX0")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	observation = owm.weather_at_place( message.text )
	w = observation.get_weather()
	temp = w.get_temperature('celsius')["temp"]

	answer = "В городе " + message.text + " сейчас " + w.get_detailed_status() +"\n"
	answer += "Температура сейчас в районе " + str(temp) + "\n\n"

	if temp < 10:
		answer +="Ебать холодно, одевайся теплее" 
	elif temp > 10 and temp < 20:
		answer += "Не так холодно, но всё равно оденься тепло" 
	elif temp > 20:
		answer += "Та похуй, хоть в трусах иди" 

	bot.send_message(message.chat.id, answer)
bot.polling( none_stop = True)