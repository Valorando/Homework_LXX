import requests

def get_balance():
    try:
        address = input("Вставьте сюда адрес своего кошелька: ")
        print("[Внимание]: Выполняется запрос на получение информации о балансе по текущему адресу...")
        url = f"https://api.blockcypher.com/v1/btc/test3/addrs/{address}/balance"
        response = requests.get(url)

        if response.status_code == 200:
            balance = response.json()
            print(f"[Успешно]: Информация о балансе по адресу {address} ...")
            print(f"Баланс: {balance['balance']} сатоши.")
            print(f"Получено за всё время: {balance['total_received']} сатоши.")
            print(f"Отправлено за всё время: {balance['total_sent']} сатоши.")
        else:
            print(f"[Ошибка]: Информация о балансе по адресу {address} не найдена.")
            print("[Внимание]: Возврат в меню...")
    except ConnectionError:
        print(f"[Ошибка]: Не удалось подключиться к ресурсу. Проверьте соединение и попробуйте снова.")
        print("[Внимание]: Возврат в меню...")    
