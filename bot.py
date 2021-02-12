import telebot # импорт библиотеки
import config # импорт настроек
from config import * # из настроек имортируем все что находится в файле
from telebot import types # из telebot имортируем types

user_id = 848252730

bot = telebot.TeleBot(config.token) 
'''в переменную "бот" мы указываем токен, который находится в файле настроек'''


''' создаем обработчик команды старт, который нам отправляет приветственный стикер и надпись
с обращением у пользователю '''
@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('stikers/welcome.tgs', 'rb')
	bot.send_sticker(message.chat.id, sti)

	bot.send_message(message.chat.id, '''Привет, {0.first_name}!\n
	Я - <b>{1.first_name}</b>, бот созаднный для проверки рассписания ☺️.
	Что бы посмотреть перечень команд напиши команду /help.'''.format(message.from_user, bot.get_me()),
	parse_mode='html')

''' теперь создадим обработчик комманд для команды хелп, которая так же отправляет стикер и надпись
с просьбой выбрать одну из указанных комманд. команды представленны в роли кнопок клавиатуры, что бы 
подключить эти кнопки мы вызываем функцию которую мы написали в файле настроек '''
@bot.message_handler(commands=['help'])
def comm(message):
	sti = open('stikers/help.tgs', 'rb')
	bot.send_sticker(message.chat.id, sti)

	bot.send_message(message.chat.id, '''Так, {0.first_name}!\nВот все команды, развлекайся ☺️.'''.format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=keyboard1())
	return

''' эта часть кода не так важна для нас, но все же поясню что это такое, данный обработчик
обрабатывает сообщения пользователя и отправляет ему обратно, что то вроде попугая'''
@bot.message_handler(content_types=['text'])
def text(message):
	bot.send_message(message.chat.id, message.text)

''' это обработчик отзыва кнопок на их нажатие '''
@bot.callback_query_handler(func=lambda call:True )
def callback_inline(call):
	try:
		if call.message:
			if call.data == 'schedule':
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выбери день недели.", reply_markup=keyboard2())

			elif call.data == 'change':
				if user_id == 848252730:
					 bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выбери день недели.", reply_markup=keyboard2_for_chande())
				else:
					bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Кнопка (изменить расписание) вам не доступна", reply_markup=keyboard1())
			elif call.data == 'back':
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выбери:", reply_markup=keyboard1())

			




	except Exception as e:
		print(repr(e))		

''' запуск бота '''
bot.polling(none_stop=True)



