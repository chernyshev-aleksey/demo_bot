import telebot
from telebot import custom_filters
from telebot import StateMemoryStorage


state_storage = StateMemoryStorage()
bot = telebot.TeleBot("6554038821:AAG4x1rvoeMZQKri3cqpU17l6_6gx7nYfO4",
                      state_storage=state_storage, parse_mode='Markdown')


text_button_1 = "конспект по основам Python"
text_button_2 = "презентация с первого вебинара"
text_button_3 = "таблица расчёта стоимости работы"
text_button_4 = "примеры общения с заказчиком"
text_button_5 = "чек-лист проверки прототипа"
text_button_6 = "записаться на курс"


menu_keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
menu_keyboard.add(
    telebot.types.KeyboardButton(
        text_button_1,
    ),
    telebot.types.KeyboardButton(
        text_button_2,
    ),
)
menu_keyboard.add(
    telebot.types.KeyboardButton(
        text_button_3,
    ),
    telebot.types.KeyboardButton(
        text_button_4,
    ),
)

menu_keyboard.add(
    telebot.types.KeyboardButton(
        text_button_5,
    )
)

menu_keyboard.add(
    telebot.types.KeyboardButton(
        text_button_6,
    )
)


@bot.message_handler(commands=['start'])
def start_ex(message):
    bot.send_message(
        message.chat.id,
        'Привет!'
    )
    bot.send_message(
        message.chat.id,
        'Меню',  # Можно менять текст
        reply_markup=menu_keyboard
    )


@bot.message_handler(func=lambda message: text_button_1 == message.text)
def help_command_5(message):
    bot.send_message(message.chat.id, "[Ссылка на конспект](https://drive.google.com/file/d/1NItSP8ZV0Nok99aVClPmWrF03PjzDmJC/view?usp=share_link)", reply_markup=menu_keyboard)


@bot.message_handler(func=lambda message: text_button_2 == message.text)
def help_command_4(message):
    bot.send_message(message.chat.id, "[Презентация с первого вебинара](https://drive.google.com/file/d/1F7J0FJL5KVacrdaowa6pbUm54FkEwecw/view?usp=share_link)", reply_markup=menu_keyboard)


@bot.message_handler(func=lambda message: text_button_3 == message.text)
def help_command_3(message):
    bot.send_message(message.chat.id, "[Таблица расчёта стоимости работы](https://drive.google.com/file/d/1TAa-l9BmGEkwLf2Aj7iq-87XxjeIv0en/view?usp=share_link)", reply_markup=menu_keyboard)


@bot.message_handler(func=lambda message: text_button_4 == message.text)
def help_command_2(message):
    bot.send_message(message.chat.id, "[примеры общения с заказчиком](https://drive.google.com/file/d/1wO9kjwFaVAkm5OWv9Y7fzVPJBy_sPmGE/view?usp=share_link)", reply_markup=menu_keyboard)


@bot.message_handler(func=lambda message: text_button_5 == message.text)
def help_command_1(message):
    bot.send_message(message.chat.id, "[чек-лист проверки прототипа](https://drive.google.com/file/d/1SslSMr65gZy8OXsonFCAlnpOOzfbGlTe/view?usp=share_link)", reply_markup=menu_keyboard)


@bot.message_handler(func=lambda message: text_button_6 == message.text)
def help_command(message):
    bot.send_message(message.chat.id, "[ссылка на запись](https://landing.umschool.net/python_course)", reply_markup=menu_keyboard)


bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.add_custom_filter(custom_filters.TextMatchFilter())

bot.infinity_polling()
