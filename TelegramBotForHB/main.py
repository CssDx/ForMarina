import telebot
import time
from telebot import types
import pytz
from datetime import datetime

bot = telebot.TeleBot('5819954828:AAGeULI1e-ExYnevY5nUxVnsePKAuy6Hfqs') #8
named_tuple = time.localtime()
time_string = time.strftime("%m/%d", named_tuple)
print(time_string)

ist_time = (pytz.timezone('Australia/Brisbane')) #13
rt = str(datetime.now(tz=ist_time))
print(rt[5:10])
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, "Добро пожаловать в бота, который преднозначен для отправки в забытые уголки памяти (напиши '/help')") #19

    elif message.text == "/help":
        keyboard1 = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Подарок!', callback_data='Present') #23
        keyboard1.add(key_yes)
        bot.send_message(message.from_user.id, 'Подарок?', reply_markup=keyboard1) #25
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    id_to = call.message.chat.id
    if call.data == 'Present':
        ist_time = (pytz.timezone('Australia/Brisbane')) #33
        rt = str(datetime.now(tz=ist_time))
        print(rt[5:10])
        if rt[5:10] == '05-18': #36
            keyboard = types.InlineKeyboardMarkup()
            key_yes = types.InlineKeyboardButton(text='Да!', callback_data='yes')
            keyboard.add(key_yes)
            key_no = types.InlineKeyboardButton(text='Нет(', callback_data='no')
            keyboard.add(key_no)
            bot.send_message(id_to, "Ты готова увидеть это зрелище))!?", reply_markup=keyboard) #42
        else:
            bot.send_message(id_to, "Если не время, значит не время")
    if call.data == "yes":
        bot.send_message(id_to, 'Юхуууу!! Тогда начинаем!') #46

        photo1 = open('ScreenOfLife/1.jpg', 'rb')
        photo2 = open('ScreenOfLife/2.jpg', 'rb')
        photo3 = open('ScreenOfLife/3.jpg', 'rb')
        photo4 = open('ScreenOfLife/4.jpg', 'rb')
        photo5 = open('ScreenOfLife/5.jpg', 'rb')
        photo6 = open('ScreenOfLife/6.jpg', 'rb')
        photo7 = open('ScreenOfLife/7.jpg', 'rb')
        photo8 = open('ScreenOfLife/8.jpg', 'rb')
        photo9 = open('ScreenOfLife/9.jpg', 'rb')
        photo10 = open('ScreenOfLife/10.jpg', 'rb')
        photo11 = open('ScreenOfLife/11.jpg', 'rb')
        photo12 = open('ScreenOfLife/12.jpg', 'rb')
        photo13 = open('ScreenOfLife/13.jpg', 'rb')
        photo14 = open('ScreenOfLife/14.jpg', 'rb')
        photo15 = open('ScreenOfLife/15.jpg', 'rb')
        #Важно соблюдать табуляцию(отступы от начала строчки)
        #Если нужно больше фотографий, то создаешь новую переменную, как тебе удобно, но лучше понятное название(как сверху) и даешь порядковый номер.
        # photoN = open('тут указываешь путь до фотографии, но можешь кинуть в папку, которую кину, тогда просто название писать', 'rb')

        #for another photo u should create a new variable and paste them adress to the photo(for example upper)

        for i in range(1, 6):
            time.sleep(1)
            bot.send_message(id_to, f'{i}')

        time.sleep(3)

        #Если тебе понадобится, ты можешь увеличить интервал между сообщениями командой time.sleep(время в секундах)
        #За отправку сообщения отвечает команда bot.send_message(id_to, 'Текст сообщения')
        #Параметр id_to отвечает за отправку пользователю, который сделал запрос
        #Команда bot.send_photo(id_to, photoN) отвчает за отправку фотографии
        #PhotoN - фотография, которую ты загрузила


        bot.send_message(id_to, 'А ты помнишь, как все начиналось?)') #82
        bot.send_photo(id_to, photo1)
        time.sleep(2)

        bot.send_message(call.message.chat.id, 'Это был далекий 18 год, но я помню как сейчас каждый момент и обещание, которые тогда были написаны в моих сообщениях тебе') #86
        time.sleep(1)
        bot.send_photo(id_to, photo2)
        time.sleep(1)
        bot.send_photo(id_to, photo5)
        time.sleep(1)
        bot.send_photo(id_to, photo6)
        time.sleep(3)

        bot.send_message(id_to, 'Это точно ты?)') #95
        time.sleep(2)
        bot.send_photo(id_to, photo3)
        time.sleep(3)

        bot.send_message(id_to, 'Сколько веселых моментов было даже так)') #100
        time.sleep(1)
        bot.send_photo(id_to, photo4)
        time.sleep(1)
        bot.send_photo(id_to, photo7)
        time.sleep(1)
        bot.send_photo(id_to, photo9)
        time.sleep(3)

        bot.send_message(id_to, 'Ну...Тут только одно можно сказать. Главное это светлое будущее.') #109
        time.sleep(2)
        bot.send_photo(id_to, photo12)
        time.sleep(2)
        bot.send_message(id_to, 'Светлое нефильтрованное, естественно') #113
        time.sleep(3)


        bot.send_message(id_to, 'Ты всегда умела выбирать правильный путь, и никогда не теряла покоя в сердце и мозгов в голове. Оставайся такойже') #117
        time.sleep(2)
        bot.send_photo(id_to, photo13)
        time.sleep(1)
        bot.send_photo(id_to, photo14)
        time.sleep(1)
        bot.send_photo(id_to, photo11)
        time.sleep(1)
        bot.send_photo(id_to, photo10)
        time.sleep(3)
        bot.send_message(id_to, 'Мариночка(Максимушка), я поздравляю тебя с твоим днем. Неважно, день это рождения или варенья), но это твой день. Я желаю, чтобы твой огонь никогда не погас, чтобы ты не теряла себя в самой же себе. Ты самая лучшая и самая крутая. Никогда не грусти, твоя улыбка заставляет других забыть про свои невзгоды. Краш(Крашиха)') #127
        time.sleep(5)
        bot.send_message(id_to, 'Ты даже не представляешь как я благодарен случайности и тому боту в ВК, который дал мне такой большой шанс. Я даже сейчас с теплотой вспоминаю каждый момент и каждое сообщение. Каждый стих, который я отправлял тебе перед сном, которые часто писал не самостоятельно, но сейчас это уже и не важно. Но одно я могу сказать, что этот от души.') #129
        time.sleep(5)
        bot.send_photo(id_to, photo15)
        bot.send_message(id_to, '❤')

    elif call.data == 'no':
        bot.send_message(id_to, 'Аэм...Мне кажется ты попухла...Ну и сиди.') #135

    if call.data == 'Life':
        keyboard3 = types.InlineKeyboardMarkup()
        key_on = types.InlineKeyboardButton(text='Еще', callback_data='Life')
        keyboard3.add(key_on)
        #rndm = random.choice(photos)
        #photos.remove(rndm)
        #photoMainLife = open(rndm, 'rb')
        #bot.send_photo(call.message.chat.id, photoMainLife, reply_markup=keyboard3)
        #if len(photos) == 0:
        #    keyboard4 = types.InlineKeyboardMarkup()
        #    key_yes2 = types.InlineKeyboardButton(text='Обнови!', callback_data='yes1')
        #    keyboard4.add(key_yes2)
        #    bot.send_message(call.message.chat.id, "Фотографии кончились, если хотите увидеть еще, то попросите разработчика добавить их. Я могу запустить эти фотографии еще раз, хотиет?", reply_markup=keyboard4)
    #if call.data == 'yes1':
    #    photos = photosCopy
bot.polling(none_stop=True, interval=0)