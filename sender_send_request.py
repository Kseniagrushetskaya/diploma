# Ксения Грушецкая, 5-я когорта — Финальный проект. Инженер по тестированию плюс
import data
import requests
import config

#Создание нового заказа для получения трека
def get_new_order(body):
    new_order = requests.post(config.URL_SERVICE + config.CREATE_NEW_ORDER,  # подставляем полный url для создания нового заказа
                         json=body,  # тут тело
                         headers=data.headers)  # а здесь заголовки
    track = new_order.json()['track'] #Возвращаем трекер нового заказа в переменную
    get_order = requests.get(config.URL_SERVICE + config.GET_TRACK_ORDER + str(track))  # подставляем полный url для получения заказа по треку
    return get_order.status_code #Получаем статус ответа