#Вощинин Дмитрий - 8 когорта, Инженер по тестированию плюс

import requests
import configuration
import data

#Создаём заказ
def get_order_track_number():
    responce = requests.post(configuration.URL + configuration.CREATE_ORDER_PATH, headers=None, json=data.user_body)
    if responce.status_code == 201:
       return(responce.json()['track'])

track_number = str(get_order_track_number())   #Сохраняем номер в переменную track_number

#Получаем информацию о заказе
def get_order_info():
    responce = requests.get(configuration.URL + configuration.GET_ORDER_BY_TRACK_PATH + track_number, headers=None, json=None)
    if responce.status_code == 200:
        print(responce.json())

get_order_info()



