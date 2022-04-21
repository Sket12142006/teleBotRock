import telebot

# initialization of lists by weekday
listOfSubjectsMon = []
listOfSubjectsTue = []
listOfSubjectsWed = []
listOfSubjectsThu = []
listOfSubjectsFri = []
listOfSubjectsSat = []

# initialization of indicators
fillSubjects = False
viewSubjects = False
subjects = False

# initialization of variables
day = ''

# connecting the API
bot = telebot.TeleBot('5152199984:AAFFEk4-WPZzxf7GRi030ygTiltKSPSoRoQ')

# initialization of keyboards
keywordPrivet = telebot.types.ReplyKeyboardMarkup(True)
keywordPrivet.row('меню', 'пока')

keywordMenu = telebot.types.ReplyKeyboardMarkup(True)
keywordMenu.row('заполнить расписание', 'посмотреть расписание', 'пока')

keywordWeekDay = telebot.types.ReplyKeyboardMarkup(True)
keywordWeekDay.row('меню')
keywordWeekDay.row('понедельник', 'вторник', 'среда')
keywordWeekDay.row('четверг', 'пятница', 'суббота')

keywordNone = telebot.types.ReplyKeyboardRemove()


# start command
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'привет, давайте начнём!', reply_markup=keywordPrivet)


# the logic of the bot
@bot.message_handler(content_types=['text'])
def send_text(message):
    # connecting global variables
    global listOfSubjectsMon
    global listOfSubjectsTue
    global listOfSubjectsWed
    global listOfSubjectsThu
    global listOfSubjectsFri
    global listOfSubjectsSat
    global fillSubjects
    global viewSubjects
    global subjects
    global day

    weekDays = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота']

    # menu
    if message.text.lower() == 'меню':
        bot.send_message(message.chat.id, 'чего бы вам хотелось?', reply_markup=keywordMenu)

        fillSubjects = False
        viewSubjects = False
        day = ''

    # bye
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'всего доброго', reply_markup=keywordPrivet)

    # fill subjects command
    elif message.text.lower() == 'заполнить расписание':
        bot.send_message(message.chat.id, 'на какой день?', reply_markup=keywordWeekDay)

        fillSubjects = True

    # request to enter subjects
    elif message.text.lower() in weekDays and fillSubjects is True:
        bot.send_message(message.chat.id, 'введите уроки по порядку через запятую с пробелом', reply_markup=keywordNone)
        bot.send_message(message.chat.id, 'на место пустого урока ставьте "-"')

        day = message.text.lower()
        subjects = True

    # entering subjects
    elif subjects is True:
        # if day is Monday
        if day == weekDays[0]:
            listOfSubjectsMon = message.text.lower().split(', ')
            print(listOfSubjectsMon)

        # if day is Tuesday
        elif day == weekDays[1]:
            listOfSubjectsTue = message.text.lower().split(', ')

        # if day is Wednesday
        elif day == weekDays[2]:
            listOfSubjectsWed = message.text.lower().split(', ')

        # if day is Thursday
        elif day == weekDays[3]:
            listOfSubjectsThu = message.text.lower().split(', ')

        # if day is Friday
        elif day == weekDays[4]:
            listOfSubjectsFri = message.text.lower().split(', ')

        # if day is Saturday
        elif day == weekDays[5]:
            listOfSubjectsSat = message.text.lower().split(', ')

        bot.send_message(message.chat.id, 'отлично, я всё запомнил, хотите заполнить ещё?', reply_markup=keywordWeekDay)
        day = ''
        subjects = False

    # view subjects command
    elif message.text.lower() == 'посмотреть расписание':
        bot.send_message(message.chat.id, 'на какой день?', reply_markup=keywordWeekDay)

        viewSubjects = True

    # bot sends subjects
    elif message.text.lower() in weekDays and viewSubjects is True:
        # if day is Monday
        if message.text.lower() == weekDays[0]:
            bot.send_message(message.chat.id, *listOfSubjectsMon)

        # if day is Tuesday
        elif message.text.lower() == weekDays[1]:
            bot.send_message(message.chat.id, listOfSubjectsTue)

        # if day is Wednesday
        elif message.text.lower() == weekDays[2]:
            bot.send_message(message.chat.id, listOfSubjectsWed)

        # if day is Thursday
        elif message.text.lower() == weekDays[3]:
            bot.send_message(message.chat.id, listOfSubjectsThu)

        # if day is Friday
        elif message.text.lower() == weekDays[4]:
            bot.send_message(message.chat.id, listOfSubjectsFri)

        # if day is Saturday
        elif message.text.lower() == weekDays[5]:
            bot.send_message(message.chat.id, listOfSubjectsSat)

        bot.send_message(message.chat.id, 'вот, ещё какой-то день интересует?', reply_markup=keywordWeekDay)


bot.polling()
