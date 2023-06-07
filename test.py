# Ксения Грушецкая, 5-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_send_request
import data

#Функция для проверки, что код ответа равен 200
def test_get_200_response():
    status_code = sender_send_request.get_new_order(data.order_body) #Сохраняем полученный статус
    assert status_code == 200 # Проверяется, что код ответа равен 200






