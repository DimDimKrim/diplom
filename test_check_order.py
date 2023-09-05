#Вощинин Дмитрий - 8 когорта, Инженер по тестированию плюс
import requests
import create_order as co
import configuration


#Проверяем статус-код

def test_check_order_by_tracknumber_status():
      responce = requests.get(configuration.URL + configuration.GET_ORDER_BY_TRACK_PATH + co.track_number, headers=None, json=None)
      assert responce.status_code == 200