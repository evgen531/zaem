import sys
sys.path.insert(0, '../')

from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import vk_api
from datetime import datetime
import random
import time
import pickle

hhperem=0



token ='2d99045efaec3912a0f959e4040cac438df98fd7d6b4dacac39f4fde606305bd3a051db1bbd0173c8151f'
vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()

longpoll = VkLongPoll(vk_session)

popo=["1" , "2" ,"3" , "4" , "5" , "1) до 10 000 руб." , "2) до 20 000 руб."  , "3) до 30 000 руб." , "4) до 50 000 руб.", "5) до 100 000 руб."]

def create_keyboard(response):
    keyboard = VkKeyboard(one_time=False)

    if response == 'начать':

        keyboard.add_button('1) до 10 000 руб.', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('2) до 20 000 руб.', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('3) до 30 000 руб.', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('4) до 50 000 руб.', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('5) до 100 000 руб.', color=VkKeyboardColor.PRIMARY)

    elif response in popo:
        keyboard.add_button('Отписаться от рассылки', color=VkKeyboardColor.DEFAULT)

    elif response == "отписаться от рассылки":
        keyboard.add_button('Спасибо', color=VkKeyboardColor.PRIMARY)

    elif response == "4276xyxz":
        keyboard.add_button('Спасибо', color=VkKeyboardColor.PRIMARY)

    else :
        keyboard.add_button('1) до 10 000 руб.', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('2) до 20 000 руб.', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('3) до 30 000 руб.', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('4) до 50 000 руб.', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()  # Переход на вторую строку
        keyboard.add_button('5) до 100 000 руб.', color=VkKeyboardColor.PRIMARY)

    keyboard = keyboard.get_keyboard()
    return keyboard


def send_message(vk_session, id_type, id, message=None, attachment=None, keyboard=None):
    vk_session.method('messages.send',{id_type: id, 'message': message, 'random_id': random.randint(-2147483648, +2147483648), "attachment": attachment, 'keyboard': keyboard})

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
            print('Текст сообщения: ' + str(event.text))
            print(event.user_id)
            response = event.text.lower()
            keyboard = create_keyboard(response)

            now = datetime.now()
            i = ' '
            if now.month == 1:
                i = ' ЯНВАРЯ'
            elif now.month == 2:
                i = ' ФЕВРАЛЯ'
            elif now.month == 3:
                i = ' МАРТА'
            elif now.month == 4:
                i = ' АПРЕЛЯ'
            elif now.month == 5:
                i = ' МАЯ'
            elif now.month == 6:
                i = ' ИЮНЯ'
            elif now.month == 7:
                i = ' ИЮЛЯ'
            elif now.month == 8:
                i = ' АВГУСТА'
            elif now.month == 9:
                i = ' СЕНТЯБРЯ'
            elif now.month == 10:
                i = ' ОКТЯБРЯ'
            elif now.month == 11:
                i = ' НОЯБРЯ'
            elif now.month == 12:
                i = ' ДЕКАБРЯ'

            if (event.from_user and not event.from_me and hhperem==1991 and event.user_id==240718387):

                print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
                print('Текст рассылки: ' + str(event.text))
                print(event.user_id)

                keyboard = create_keyboard(response)

                ffail1 = 'bd15.data' # shopcom ссылка на имя файла, 'combocomnat.data' - название файла
                f = open(ffail1, 'rb')  # 1 открытие
                da1 = pickle.load(f)  # 2 открытие
                for vv in da1:
                    send_message(vk_session, 'user_id', vv, message=event.text,
                                 keyboard=keyboard)


                f.close()  # закрыли
                hhperem=0
                del da1
                print('_________________')
                print('Переменная hhperem='+str(hhperem))
                print('_________________')
                print('Мы послали текст всем')


            if event.from_user and not event.from_me:
                if response == "начать":
                    time.sleep(2)
                    send_message(vk_session, 'user_id', event.user_id, message='Нужны деньги? Тогда скажите сколько вам надо. И я помогу\n'
                                                                               ' получить деньги за 15 минут!\n'
                                                                               '\n'
                                                                               '(нажми на кнопку или напиши цифру от 1 до 5)\n'
                                                                               '\n'
                                                                               '1) до 10 000 руб.\n'
                                                                               '2) до 20 000 руб.\n'
                                                                               '3) до 30 000 руб.\n'
                                                                               '4) до 50 000 руб.\n'
                                                                               '5) до 80 000 руб.',keyboard=keyboard)
                elif response in popo:

                    time.sleep(2)
                    ididid=str(event.user_id)

                    ffail1 = 'bd15.data'  # shopcom ссылка на имя файла, 'bd15.data' - название файла
                    f = open(ffail1, 'rb')  # 1 открытие
                    da1 = pickle.load(f)  # 2 открытие
                    tus2 = da1[:]  # perem наш массив, полученный полной вырезкой
                    f.close()  # закрыли

                    tus2.insert(0, ididid)  # ДОБАВЛЯЕМ В МАССИВ
                    del ididid

                    print('_' * 40)
                    print('В базе: ' + (str(len(tus2) - 1)) + ' человек(а)')
                    print('_' * 40)

                    f = open(ffail1, 'wb')  # Ооткрыли wb
                    pickle.dump(tus2, f)  # поместили
                    f.close()  # закрыли
                    print(('-') * 40)
                    print(tus2)
                    print(('-') * 40)
                    del tus2  # удалили массив tus2

                    #elif response == "1" or "2" or "3" or "4" or "5" or "1) до 10 000 руб." or "2) до 20 000 руб."   or "3) до 30 000 руб." or "4) до 50 000 руб." or "5) до 100 000 руб.":

                    send_message(vk_session, 'user_id', event.user_id, message= 'ТРИ ПРЕДЛОЖЕНИЯ ДЛЯ ВАС И ОДОБРЕНИЯ🔥\n'
                                                                                '\n'
                                                                                '💸 Предоставляет вам займ под 0%!\n'
                                                                                '✔➡ https://vk.cc/9RG4LP\n'
                                                                                '\n'
                                                                                '💸Предложение только для Вас, не упустите!\n'
                                                                                '✔➡ https://vk.cc/9RG5yG\n'
                                                                                '\n'
                                                                                '💸 Онлайн займ хочет вам перевести на карту 💵!\n'
                                                                                '✔➡ https://vk.cc/9RG65e\n'
                                                                                '\n'
                                                                                'ХОТИТЕ ПОЛУЧИТЬ БОЛЬШЕ И ПОВЫСИТЬ ШАНС ОДОБРЕНИЯ💰💰💰 ?\n'
                                                                                '✅Заполните заявки ниже:\n'
                                                                                '\n'
                                                                                '💸15 000 тысяч через 6 минут у вас на карте под 0%!\n'
                                                                                '✔➡ https://vk.cc/9RG6wg \n'
                                                                                '\n'
                                                                                '💸Под 0% - 15.000 руб\n'
                                                                                '✔➡ https://vk.cc/9RG751\n'
                                                                                '\n'
                                                                                '💸 До 100 000 рублей - Первый займ под 0%!\n'
                                                                                '✔➡ https://vk.cc/9RG7Cl\n'
                                                                                '\n'
                                                                                '💸 30 000 на карту\n'
                                                                                '✔➡ https://vk.cc/9RG9k5 \n'
                                                                                '\n'
                                                                                '❗Рекомендую заполнить все заявки, тогда вы гарантированно получите максимально возможную сумму с минимальным риском в отказе❗\n'
                                                                                '\n'
                                                                                'ПРЕДЛОЖЕНИЕ ДЕЙСТВУЕТ ДО '+str(now.day+1)+i,keyboard=keyboard)

                elif response == "отписаться от рассылки":

                    fila = 'bd15.data'
                    f = open(fila, 'rb')
                    dd = pickle.load(f)  # 2 открытие
                    mass = dd[:]  # spis наш массив, полученный полной вырезкой
                    f.close()  # закрыли массив

                    for indexx in range(0, len(mass), 1):  # ПРОХОД ПО ВСЕМ ИНДЕКСАМ В МАССИВЕ
                        dds01 = str(event.user_id)  # СОЗДАНИЕ ССЫЛИ НА СТРАННИЦУ
                        if dds01 in mass[indexx]:
                            print(indexx)
                            del mass[indexx]
                            del indexx
                            del dds01
                            break

                    print('_' * 40)
                    print(mass)
                    print('_' * 40)
                    print('В базе: ' + (str(len(mass) - 1)) + ' человек(а)')
                    print('_' * 40)

                    f = open(fila, 'wb')  # Открыли wb
                    pickle.dump(mass, f)  # поместили
                    f.close()  # закрыли

                    del mass  # удалили оба массива
                    del dd  # удалили оба массива

                    send_message(vk_session, 'user_id', event.user_id, message='Спасибо что воспользовались нашим сервисом.',
                                 keyboard=keyboard)

                elif response == "4276xyxz" and event.user_id==240718387:

                    send_message(vk_session, 'user_id', event.user_id, message='введи текст рассылки Джонни',
                                 keyboard=keyboard)
                    hhperem=1991

                else :

                    send_message(vk_session, 'user_id', event.user_id, message='Нужны деньги? Тогда скажите сколько вам надо. И я помогу\n'
                                                                               ' получить деньги за 15 минут!\n'
                                                                               '\n'
                                                                               '(нажми на кнопку или напиши цифру от 1 до 5)\n'
                                                                               '\n'
                                                                               '1) до 10 000 руб.\n'
                                                                               '2) до 20 000 руб.\n'
                                                                               '3) до 30 000 руб.\n'
                                                                               '4) до 50 000 руб.\n'
                                                                               '5) до 80 000 руб.',keyboard=keyboard)


