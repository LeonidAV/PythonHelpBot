import telebot
from telebot import types
from wiki import getwiki
from weather import get_weather
from datetime import datetime
from pycbrf import ExchangeRates

bot = telebot.TeleBot('5507672712:AAHfDqT2EMVsAjlVM6d6ByhT20hFKAm5_ww')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                      '<b> 🙃 Привет друг!🙃</b>\n\n'
                      '<b>Это PythonHelpBot🤖</b>\n\n'
                      '<b>Он будет твоим помощником в поиске нужных ответов🙈</b>\n'
                      '<b>Не стесняйся обращаться😊</b>\n\n'
                      '<b>Доступные команды ниже.</b>\n\n'
                      '<b>• /help - Сейчас появятся📌📌📌\n\n</b>'
                      '<b>• /wiki - Вики 🧠\n\n</b>'
                      '<b>• /money - Курсы валют к рублю💰\n\n</b>'
                      '<b>• /weather - Погода⛅\n\n</b>',
                      parse_mode='HTML')


@bot.message_handler(commands=["wiki"])
def wiki(message):
    bot.send_message(
        message.chat.id, 'Отправьте мне любое слово, и я найду его значение на Википедии❗')

    def asking(message):
        mesg = bot.send_message(message.chat.id, 'Что ищем❓')
        bot.register_next_step_handler(mesg, answer)

    def answer(message):
        bot.send_message(message.chat.id, getwiki(message.text))
    asking(message)


@bot.message_handler(commands=['weather'])
def weather(message):
    def asking(message):
        mesg = bot.send_message(
            message.chat.id, '<b>Введите название города !</b>', parse_mode='HTML')
        bot.register_next_step_handler(mesg, answer)

    def answer(message):
        bot.send_message(message.chat.id, get_weather(message.text))
    asking(message)


@bot.message_handler(commands=['money'])
def money(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    usd = types.KeyboardButton('USD')
    eur = types.KeyboardButton('EUR')
    gbp = types.KeyboardButton('GBP')
    liry = types.KeyboardButton('TRY')
    chf = types.KeyboardButton('CHF')
    cny = types.KeyboardButton('CNY')
    cad = types.KeyboardButton('CAD')
    markup.add(usd, eur, gbp, liry, chf, cny, cad)
    bot.send_message(message.chat.id, 'Выбирай нужную валюту, и узнай курс рубля!', reply_markup=markup)


@bot.message_handler(commands=['help'])
def get_user(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    podskazka = types.KeyboardButton('Подсказки по Python')
    really = types.KeyboardButton('Полезные ссылки')
    pythonkurs = types.KeyboardButton('Курсы по Python')
    github = types.KeyboardButton('Оформление Github')
    pythongui = types.KeyboardButton('Обучение Python GUI')
    markup.add(really, pythonkurs, github, pythongui, podskazka)
    bot.send_message(message.chat.id, '❗Нажимай на них скорее❗', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def info(message):
    if message.chat.type == 'private':
        message_norm = message.text.strip().lower()

        if message_norm in ['usd', 'eur', 'gbp', 'try', 'chf', 'cny', 'cad']:
            rates = ExchangeRates(datetime.now())
            bot.send_message(chat_id=message.chat.id,
                             text=f"<b> Один {message_norm.upper()} равен {float(rates[message_norm.upper()].rate)} руб.</b>",
                             parse_mode="html")
        if message.text == 'Миграции':
            bot.send_message(message.chat.id,
                             'python manage.py makemigrations\n'
                             'python manage.py migrate\n',
                             parse_mode='html')
        elif message.text == 'Подсказки по Python':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            programm = types.KeyboardButton('Программы')
            migrate = types.KeyboardButton('Миграции')
            venv = types.KeyboardButton('Виртуальное окружение')
            git = types.KeyboardButton('Команды Git')
            codestail = types.KeyboardButton('Кодстайл')
            requirements = types.KeyboardButton('Requirements')
            back = types.KeyboardButton('Назад')
            markup.add(programm, migrate, venv, git, codestail, requirements, back)
            bot.send_message(message.chat.id, 'Подсказки по Python', reply_markup=markup)

        elif message.text == 'Виртуальное окружение':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            window = types.KeyboardButton('Windows')
            macos = types.KeyboardButton('MacOS')
            back = types.KeyboardButton('Назад')
            markup.add(window, macos, back)
            bot.send_message(message.chat.id, 'Виртуальное окружение', reply_markup=markup)
        elif message.text == 'Windows':
            bot.send_message(message.chat.id,
                             'python -m venv venv\n'
                             'source venv/Scripts/activate',
                             parse_mode='html')
        elif message.text == 'MacOS':
            bot.send_message(message.chat.id,
                             'python3 -m venv ven\n'
                             'source venv/bin/activate',
                             parse_mode='html')
        elif message.text == 'Команды Git':
            bot.send_message(message.chat.id,
                             'git add . - Загружаем\n'
                             'git status - Проверяем\n'
                             'git commit -m " "  - Пишем комментарий\n'
                             'git push - Закидываем\n',
                             parse_mode='html')
        elif message.text == 'Кодстайл':
            code = types.ReplyKeyboardMarkup(resize_keyboard=True)
            flake = types.KeyboardButton('Flake8')
            mypy = types.KeyboardButton('Mypy')
            isort = types.KeyboardButton('Isort')
            back = types.KeyboardButton('Назад')
            code.add(flake, mypy, isort, back)
            bot.send_message(message.chat.id, 'Кодстайл', reply_markup=code)
        elif message.text == 'Flake8':
            bot.send_message(message.chat.id,
                             'pip install flake8 - Установка\n'
                             'flake8 my_project - Запуск',
                             parse_mode='html')
        elif message.text == 'Mypy':
            bot.send_message(message.chat.id,
                             'pip install mypy',
                             parse_mode='html')
        elif message.text == 'Isort':
            bot.send_message(message.chat.id,
                             'pip install isort - Установка\n'
                             'isort .  - Запуск и проверка',
                             parse_mode='html')
        elif message.text == 'Программы':
            programm = types.ReplyKeyboardMarkup(resize_keyboard=True)
            python = types.KeyboardButton('Python')
            pycharm = types.KeyboardButton('Pycharm')
            vscode = types.KeyboardButton('Visual Studio Code')
            vs = types.KeyboardButton('Visual Studio')
            back = types.KeyboardButton('Назад')
            programm.add(python, pycharm, vscode, vs, back)
            bot.send_message(message.chat.id, 'Программы', reply_markup=programm)
        elif message.text == 'Python':
            bot.send_message(message.chat.id,
                             'https://www.python.org/downloads/',
                             parse_mode='html')
        elif message.text == 'Pycharm':
            bot.send_message(message.chat.id,
                             'https://www.jetbrains.com/ru-ru/pycharm/download/#section=windows',
                             parse_mode='html')
        elif message.text == 'Visual Studio Code':
            bot.send_message(message.chat.id,
                             'https://code.visualstudio.com/download',
                             parse_mode='html')
        elif message.text == 'Visual Studio':
            bot.send_message(message.chat.id,
                             'https://visualstudio.microsoft.com/ru/vs/',
                             parse_mode='html')

        elif message.text == 'Полезные ссылки':
            really = types.ReplyKeyboardMarkup(resize_keyboard=True)
            python = types.KeyboardButton('Идеи проектов для портфолио')
            pycharm = types.KeyboardButton('Актуальные вакансии')
            vscode = types.KeyboardButton('Огромный архив по Python')
            vs = types.KeyboardButton('Курсы на Stepik по Python')
            back = types.KeyboardButton('Назад')
            really.add(python, pycharm, vscode, vs, back)
            bot.send_message(message.chat.id, 'Полезные ссылки', reply_markup=really)
        elif message.text == 'Идеи проектов для портфолио':
            bot.send_message(message.chat.id,
                             'https://www.goskills.com/Development/Resources/What-can-I-do-with-Python',
                             parse_mode='html')
        elif message.text == 'Актуальные вакансии':
            bot.send_message(message.chat.id,
                             'https://hh.ru/search/vacancy?text=Python&from=suggest_post&area=1',
                             parse_mode='html')
        elif message.text == 'Огромный архив по Python':
            bot.send_message(message.chat.id,
                             'https://cloud.mail.ru/public/Kxvb/mhXTAUNct',
                             parse_mode='html')
        elif message.text == 'Курсы на Stepik по Python':
            bot.send_message(message.chat.id,
                             'https://stepik.org/catalog/search?free=true&q=python',
                             parse_mode='html')
        elif message.text == 'Requirements':
            requirements = types.ReplyKeyboardMarkup(resize_keyboard=True)
            install = types.KeyboardButton('Установка')
            doc = types.KeyboardButton('Документация')
            back = types.KeyboardButton('Назад')
            requirements.add(install, doc, back)
            bot.send_message(message.chat.id, 'Requirements', reply_markup=requirements)
        elif message.text == 'Установка':
            bot.send_message(message.chat.id,
                             'pip install -r requirements.txt',
                             parse_mode='html')
        elif message.text == 'Документация':
            bot.send_message(message.chat.id,
                             'https://pip.pypa.io/en/stable/user_guide/ \n\n'
                             'https://dvmn.org/encyclopedia/pip/pip_requirements_txt/',
                             parse_mode='html')

        elif message.text == 'Курсы по Python':
            pythonkurs = types.ReplyKeyboardMarkup(resize_keyboard=True)
            one = types.KeyboardButton('Создание мини-блога')
            two = types.KeyboardButton('Создание сайта на Django')
            three = types.KeyboardButton('Погодное приложение на Django за час')
            four = types.KeyboardButton('Создаем веб-приложение ToDo на Django + Semantic UI')
            five = types.KeyboardButton('Django 4 пишем сайт с нуля')
            back = types.KeyboardButton('Назад')
            pythonkurs.add(one, two, three, four, five, back)
            bot.send_message(message.chat.id, 'Курсы по Python', reply_markup=pythonkurs)
        elif message.text == 'Создание мини-блога':
            bot.send_message(message.chat.id,
                             'https://www.youtube.com/watch?v=wCDn6pYhLxg&list=PLs2IpQwiXpT2V0brYrq1gxbRJVeR9t5jY&index=1',
                             parse_mode='html')
        elif message.text == 'Создание сайта на Django':
            bot.send_message(message.chat.id,
                             'https://www.youtube.com/watch?v=_HuZ-lI68bc&list=PLxbd7ySXT5YqE71F2CmADjMTI_ILDTBYN',
                             parse_mode='html')
        elif message.text == 'Погодное приложение на Django за час':
            bot.send_message(message.chat.id,
                             'https://www.youtube.com/watch?v=lsAbq2RcWlQ',
                             parse_mode='html')
        elif message.text == 'Создаем веб-приложение ToDo на Django + Semantic UI':
            bot.send_message(message.chat.id,
                             'https://www.youtube.com/watch?v=YMFm0_fSjUQ',
                             parse_mode='html')
        elif message.text == 'Django 4 пишем сайт с нуля':
            bot.send_message(message.chat.id,
                             'https://www.youtube.com/playlist?list=PLuZJ9n46uMzXVj9JEjULImuBKRVKKS9To',
                             parse_mode='html')

        elif message.text == 'Оформление Github':
            github= types.ReplyKeyboardMarkup(resize_keyboard=True)
            gitup = types.KeyboardButton('Оформление профиля')
            gitreadme = types.KeyboardButton('Оформление README')
            back = types.KeyboardButton('Назад')
            github.add(gitup, gitreadme, back)
            bot.send_message(message.chat.id, 'Оформление Github', reply_markup=github)
        elif message.text == 'Оформление профиля':
            bot.send_message(message.chat.id,
                             'https://www.youtube.com/watch?v=pm17VwdJ6UI',
                             parse_mode='html')
        elif message.text == 'Оформление README':
            bot.send_message(message.chat.id,
                             'https://www.youtube.com/watch?v=NXNf9aYTCZ0&list=WL&index=4',
                             parse_mode='html')
        elif message.text == 'Обучение Python GUI':
            gui= types.ReplyKeyboardMarkup(resize_keyboard=True)
            tkinter = types.KeyboardButton('Уроки по Tkinter')
            back = types.KeyboardButton('Назад')
            gui.add(tkinter, back)
            bot.send_message(message.chat.id, 'Оформление Github', reply_markup=gui)
        elif message.text == 'Уроки по Tkinter':
            bot.send_message(message.chat.id,
                             'https://pythonru.com/uroki/obuchenie-python-gui-uroki-po-tkinter#:~:text=%D0%A1%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%20%D1%81%D0%B2%D0%BE%D0%B5%D0%B3%D0%BE%20%D0%BF%D0%B5%D1%80%D0%B2%D0%BE%D0%B3%D0%BE%20%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%BE%D0%B3%D0%BE%20%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D1%84%D0%B5%D0%B9%D1%81%D0%B0&text=%D0%9F%D0%BE%D1%81%D0%BB%D0%B5%D0%B4%D0%BD%D1%8F%D1%8F%20%D1%81%D1%82%D1%80%D0%BE%D0%BA%D0%B0%20%D0%B2%D1%8B%D0%B7%D1%8B%D0%B2%D0%B0%D0%B5%D1%82%20%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D1%8E%20mainloop,%D0%B4%D0%BB%D1%8F%20%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8F%20%D0%BD%D0%B8%D1%87%D0%B5%D0%B3%D0%BE%20%D0%BD%D0%B5%20%D0%BE%D1%82%D0%BE%D0%B1%D1%80%D0%B0%D0%B7%D0%B8%D1%82%D1%81%D1%8F.',
                             parse_mode='html')

        elif message.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            podskazka = types.KeyboardButton('Подсказки по Python')
            really = types.KeyboardButton('Полезные ссылки')
            pythonkurs = types.KeyboardButton('Курсы по Python')
            github = types.KeyboardButton('Оформление Github')
            pythongui = types.KeyboardButton('Обучение Python GUI')
            markup.add(really, pythonkurs, github, pythongui, podskazka)
            bot.send_message(message.chat.id, '❗Нажимай на них скорее❗', reply_markup=markup)


bot.polling(none_stop=True)
