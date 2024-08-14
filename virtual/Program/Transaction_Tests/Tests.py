import requests
from requests.exceptions import ConnectionError

def validate_address_and_key_test(value, name):
    if not value:
        print(f"[Ошибка]: {name} не должен быть пустым.")
        print("[Внимание]: Создание транзакции отменено, возврат в меню...")
        return False
    elif value.isdigit():
        print(f"[Ошибка]: {name} не должен быть числом.")
        print("[Внимание]: Создание транзакции отменено, возврат в меню...")
        return False
    else:
        print(f"[Успешно]: {name} прошёл проверку.")

def authenticity_address_test(address, name):
    try:
        url = f"https://api.blockcypher.com/v1/btc/test3/addrs/{address}/balance"
        response = requests.get(url)
        if response.status_code == 200:
            print(f"[Успешно]: {name} достоверен.")
        else:
            print(f"[Ошибка]: {name} недостоверен.")
            print("[Внимание]: Создание транзакции отменено, возврат в меню...")
            return False
    except ConnectionError:
        print(f"[Ошибка]: Не удалось подключиться к ресурсу. Проверьте соединение и попробуйте снова.")
        print("[Внимание]: Создание транзакции отменено, возврат в меню...")
        return False

def validate_amount_test(value, name):
    try:
        value = int(value)
    except ValueError:
        print(f"[Ошибка]: {name} не должна быть пустым, символьным или буквенным значением.")
        print("[Внимание]: Создание транзакции отменено, возврат в меню...")
        return False
    if value == 0:
        print(f"[Ошибка]: {name} не должна быть равна нулю.")
        print("[Внимание]: Создание транзакции отменено, возврат в меню...")
        return False
    elif value < 0:
        print(f"[Ошибка]: {name} не должна быть отрицательной.")
        print("[Внимание]: Создание транзакции отменено, возврат в меню...")
        return False
    else:
        print(f"[Успешно]: {name} прошла проверку.")

def solvency_sender_test(address, amount):
    try:
        amount = int(amount)
        url = f"https://api.blockcypher.com/v1/btc/test3/addrs/{address}/balance"
        response = requests.get(url)

        if response.status_code != 200:
            print(f"[Ошибка]: Не удалось получить информацию об адресе {address}.")
            print("[Внимание]: Создание транзакции отменено, возврат в меню...")
            return False
        
        balance = response.json().get('balance')

        if balance >= amount:
            print(f"[Успешно]: На балансе достаточно средств для совершения транзакции, текущий баланс: {balance} сатоши.")
        else:
            print(f"[Ошибка]: На балансе недостаточно средств для совершения транзакции, текущий баланс: {balance} сатоши.")
            print("[Внимание]: Создание транзакции отменено, возврат в меню...")
            return False
    except ConnectionError:
        print(f"[Ошибка]: Не удалось подключиться к ресурсу. Проверьте соединение и попробуйте снова.")
        print("[Внимание]: Создание транзакции отменено, возврат в меню...")
        return False
