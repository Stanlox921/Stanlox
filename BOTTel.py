
import telebot
from pyowm import OWM
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('c821f4964e8b0fe69bca755fcd844645', config_dict)
bot = telebot.TeleBot("1339191678:AAE7VY-3gbCkWAvGNnEaI12RL9_7Qb2GUfI")
@bot.message_handler(content_types=['text'])
def send_echo(message):
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    temp = w.temperature('celsius')["temp"]
    answer = "В вашем городе " + message.text + " сейчас " + w.detailed_status + "\n"
    answer += "Температура сейчас в районе " + str(temp) + "\n\n"
    if temp < 10:
        answer += "Очень холодно"
    elif temp < 20:
        answer += "Прохладно, одевайся"
    elif temp > 20:
        answer += "Тепло"
    bot.send_message(message.chat.id, answer)
bot.polling(none_stop=True)