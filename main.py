import telebot
from telebot import custom_filters
from telebot import StateMemoryStorage
from telebot.handler_backends import StatesGroup, State


state_storage = StateMemoryStorage()
bot = telebot.TeleBot("6081275728:AAEWUtyKA63RDFQPxI8QScXkLeUi-1N3fvk",
                      state_storage=state_storage, parse_mode='Markdown')


class PollState(StatesGroup):
    first = State()
    name = State()
    age = State()


class HelpState(StatesGroup):
    wait_text = State()


text_poll = "опрос"
text_button_1 = "Кнопка 1"
text_button_2 = "Кнопка 2"
text_button_3 = "Кнопка 3"


menu_keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
menu_keyboard.add(
    telebot.types.KeyboardButton(
        text_poll,
    )
)
menu_keyboard.add(
    telebot.types.KeyboardButton(
        text_button_1,
    )
)

menu_keyboard.add(
    telebot.types.KeyboardButton(
        text_button_2,
    ),
    telebot.types.KeyboardButton(
        text_button_3,
    )
)


@bot.message_handler(state="*", commands=['start'])
def start_ex(message):
    bot.send_message(
        message.chat.id,
        'Привет! Что будем делать?',
        reply_markup=menu_keyboard)
    bot.set_state(message.from_user.id, PollState.first, message.chat.id)


@bot.message_handler(func=lambda message: text_poll == message.text, state=PollState.first)
def first(message):
    bot.send_message(message.chat.id, 'Супер! *Ваше* _имя_?')
    bot.set_state(message.from_user.id, PollState.name, message.chat.id)


@bot.message_handler(state=PollState.name)
def name(message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['name'] = message.text
    bot.send_message(message.chat.id, 'Супер! [Ваш](https://www.example.com/) `возраст?`')
    bot.set_state(message.from_user.id, PollState.age, message.chat.id)


@bot.message_handler(state=PollState.age)
def age(message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['age'] = message.text
    bot.send_message(message.chat.id, 'Спасибо за регистрацию!')
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        bot.send_message(
            message.chat.id,
            f'Ваше имя: {data["name"]}\nВаш возраст: {data["age"]}',
            reply_markup=menu_keyboard
        )
    bot.delete_state(message.from_user.id, message.chat.id)


@bot.message_handler(func=lambda message: text_button_1 == message.text)
def help_command(message):
    bot.send_message(message.chat.id, "Текст 1", reply_markup=menu_keyboard)


@bot.message_handler(func=lambda message: text_button_2 == message.text)
def help_command(message):
    bot.send_message(message.chat.id, "Текст 2", reply_markup=menu_keyboard)


@bot.message_handler(func=lambda message: text_button_3 == message.text)
def help_command(message):
    bot.send_message(message.chat.id, "Текст 3", reply_markup=menu_keyboard)


bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.add_custom_filter(custom_filters.TextMatchFilter())

bot.infinity_polling()
