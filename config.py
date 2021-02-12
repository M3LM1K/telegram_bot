import telebot # импорт библиотеки

from telebot import types # из telebot имортируем types

token = '1604726938:AAEqV-UnjyNBX6bcSfDFoBf9BzBiXikP2w4' # токен бота

# первая клавиатура
# созаем фукцию, добавляем тип клавиатуры, добавляем кнопки, выводим кнопки
def keyboard1():
	keyboard1 = types.InlineKeyboardMarkup(row_width=2)
	item1 = types.InlineKeyboardButton("Посмотреть расписание", callback_data="schedule")
	item2 = types.InlineKeyboardButton("Внести изменения", callback_data="change")

	keyboard1.add(item1, item2)
	
	return keyboard1

# вторая клавиатура
# созаем фукцию, добавляем тип клавиатуры, добавляем кнопки, выводим кнопки
def keyboard2_for_schedule():
	keyboard2 = types.InlineKeyboardMarkup(row_width=2)
	item1 = types.InlineKeyboardButton("Понедельник", callback_data='monday')
	item2 = types.InlineKeyboardButton("Вторник", callback_data='tuesday')
	item3 = types.InlineKeyboardButton("Среда", callback_data='wednesday')
	item4 = types.InlineKeyboardButton("Четверг", callback_data='thursday')
	item5 = types.InlineKeyboardButton("Пятница", callback_data='friday')
	item6 = types.InlineKeyboardButton("Суббота", callback_data='saturday')
	item7 = types.InlineKeyboardButton("Воскресенье", callback_data='sunday')
	item8 = types.InlineKeyboardButton("Назад", callback_data='back')

	keyboard2.add(item1, item2)
	keyboard2.add(item3, item4)
	keyboard2.add(item5, item7)
	keyboard2.add(item8)

	return keyboard2 


def keyboard2_for_chande():
	keyboard21 = types.InlineKeyboardMarkup(row_width=2)
	item1 = types.InlineKeyboardButton("Понедельник", callback_data='mondays')
	item2 = types.InlineKeyboardButton("Вторник", callback_data='tuesdays')
	item3 = types.InlineKeyboardButton("Среда", callback_data='wednesdays')
	item4 = types.InlineKeyboardButton("Четверг", callback_data='thursdays')
	item5 = types.InlineKeyboardButton("Пятница", callback_data='fridays')
	item6 = types.InlineKeyboardButton("Суббота", callback_data='saturdays')
	item7 = types.InlineKeyboardButton("Воскресенье", callback_data='sundays')
	item8 = types.InlineKeyboardButton("Назад", callback_data='back')

	keyboard21.add(item1, item2)
	keyboard21.add(item3, item4)
	keyboard21.add(item5, item7)
	keyboard21.add(item8)

	return keyboard21 

# третья клавиатура
# созаем фукцию, добавляем тип клавиатуры, добавляем кнопки, выводим кнопки
def keyboard3():
	keyboard3 = types.InlineKeyboardMarkup(row_width=2)
	item8 = types.InlineKeyboardButton("Назад", callback_data='back')

	keyboard3.add(item8)

	return keyboard3


'''def password(message):
    if message.text.lower() == '43045839':
        bot.send_message(message.from_user.id, 'Окей, выдерите день:', reply_markup=keyboard2())
        return
'''