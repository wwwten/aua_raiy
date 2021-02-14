import pyowm 
import telebot

bot = telebot.TeleBot("1620987069:AAFPNiugSwS3wx3trOECp_73NAz8f8Lk520")
from google_trans_new import google_translator
owm = pyowm.OWM('17f262412e507221a9ca06a471f08324')

translator = google_translator()



@bot.message_handler(content_types=['text'])

def weather(message):
	observation = owm.weather_at_place(message.text)
	w = observation.get_weather()

	temp = w.get_temperature('celsius')['temp']

	status = translator.translate(w.get_detailed_status(), lang_tgt = 'kk')
	message.text = translator.translate(message.text, lang_tgt = 'ru')
	
	

	answer = message.text + " қаласында қазір " + status + "\n"
	answer += "Ауа температурасы шамамен " + str(temp) + "\n"

	if temp < 10:
		answer += "Дала суық, жылы киініңіз!"
	elif temp < 20:
		answer += "Далаға мүлде шықпауға тырысыңыз!"
	else:
		answer += "Қыдыруға болады!"

	bot.send_message(message.chat.id, answer)
bot.polling(none_stop = True)