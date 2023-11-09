import configuration
import requests
import data

# Функция создания заказа
def create_order(body):
    return requests.post (configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body)

# Функция получения заказа по номеру трекера
def get_order_by(track):
    get_order_api = f"{configuration.URL_SERVICE}{configuration.ORDER_TRACK}?t={track}"
    response = requests.get(get_order_api)
    return response

# Тестирование создания заказа и получение ответа
def test_create_order_and_getting_response():
    response = create_order(data.order_body)

    track = response.json()["track"]
    print("Заказ создан. Номер трека:", track)

    # Получение данных заказа по номеру трека
    order_response = get_order_by(track)

    assert order_response.status_code == 200
    order_data = order_response.json()
    print("Данные заказа:")
    print(order_data)

# Ишкильдин Дмитрий , 10-я когорта — Финальный проект. Инженер по тестированию плюс