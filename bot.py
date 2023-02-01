import telebot
from telebot import types
from wiki import getwiki
from weather import get_weather

bot = telebot.TeleBot('5507672712:AAHfDqT2EMVsAjlVM6d6ByhT20hFKAm5_ww')


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


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                      '<b> 🙃 Привет друг!🙃</b>\n\n'
                      '<b>Это PythonHelpBot🤖</b>\n\n'
                      '<b>Он будет твоим помощником в поиске нужных ответов🙈</b>\n'
                      '<b>Не стесняйся обращаться😊</b>\n\n'
                      '<b>Пока доступна одна команда, которая выведет бесконечное множество кнопок.</b>\n'
                      '<b><u>• /help - Сейчас появятся📌📌📌\n\n</u></b>'
                      '<b><u>• /wiki - Вики 🧠\n\n</u></b>'
                      '<b><u>• /weather - Погода⛅\n\n</u></b>',
                      parse_mode='HTML')


@bot.message_handler(commands=['help'])
def get_user(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    programm = types.KeyboardButton('Программы')
    migrate = types.KeyboardButton('Миграции')
    venv = types.KeyboardButton('Виртуальное окружение')
    git = types.KeyboardButton('Команды Git')
    codestail = types.KeyboardButton('Кодстайл')
    really = types.KeyboardButton('Полезные ссылки')
    requirements = types.KeyboardButton('Requirements')
    pythonkurs = types.KeyboardButton('Курсы по Python')
    markup.add(migrate, venv, git, codestail, programm, really, requirements, pythonkurs)
    bot.send_message(message.chat.id, '❗Нажимай на них скорее❗', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def info(message):
    if message.chat.type == 'private':
        if message.text == 'Миграции':
            bot.send_message(message.chat.id,
                             'python manage.py makemigrations\n'
                             'python manage.py migrate\n',
                             parse_mode='html')
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
            really = types.ReplyKeyboardMarkup(resize_keyboard=True)
            install = types.KeyboardButton('Установка')
            doc = types.KeyboardButton('Документация')
            back = types.KeyboardButton('Назад')
            really.add(install, doc, back)
            bot.send_message(message.chat.id, 'Requirements', reply_markup=really)
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
            really = types.ReplyKeyboardMarkup(resize_keyboard=True)
            one = types.KeyboardButton('Создание мини-блога')
            two = types.KeyboardButton('Создание сайта на Django')
            three = types.KeyboardButton('Погодное приложение на Django за час')
            four = types.KeyboardButton('Создаем веб-приложение ToDo на Django + Semantic UI')
            five = types.KeyboardButton('Django 4 пишем сайт с нуля')
            back = types.KeyboardButton('Назад')
            really.add(one, two, three, four, five, back)
            bot.send_message(message.chat.id, 'Курсы по Python', reply_markup=really)
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

        elif message.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            programm = types.KeyboardButton('Программы')
            migrate = types.KeyboardButton('Миграции')
            venv = types.KeyboardButton('Виртуальное окружение')
            git = types.KeyboardButton('Команды Git')
            codestail = types.KeyboardButton('Кодстайл')
            really = types.KeyboardButton('Полезные ссылки')
            markup.add(migrate, venv, git, codestail, programm, really)
            bot.send_message(message.chat.id, '❗Нажимай на них скорее❗', reply_markup=markup)


bot.polling(none_stop=True)
