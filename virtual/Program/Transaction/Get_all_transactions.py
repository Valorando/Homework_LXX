import requests

def get_all_transactions():
    try:
        address = input("Вставьте сюда адрес своего кошелька: ")
        print("[Внимание]: Выполняется запрос на получение информации о транзакциях по текущему адресу...")
        url = f"https://api.blockcypher.com/v1/btc/test3/addrs/{address}/full"
        response = requests.get(url)   

        if response.status_code == 200:
            data = response.json()
            transactions = data['txs']
            print(f"[Успешно]: Найдено {len(transactions)} транзакций для адреса {address}")

            for tx in transactions:
                print(f"\nID: {tx['hash']}")
                print(f"Дата: {tx['received']}")
                print(f"Подтверждения: {tx['confirmations']}")
                print(f"Размер: {tx['size']} байт")
                print("Входящие:")
                for input_tx in tx['inputs']:
                    print(f"  Адрес: {input_tx.get('addresses', ['неизвестно'])[0]}")
                    print(f"  Сумма: {input_tx.get('output_value', 'неизвестно')} сатоши")
                print("Исходящие:")
                for output_tx in tx['outputs']:
                    print(f"  Адрес: {output_tx.get('addresses', ['неизвестно'])[0]}")
                    print(f"  Сумма: {output_tx.get('value', 'неизвестно')} сатоши")

                total_input_value = sum(input_tx.get('output_value', 0) for input_tx in tx['inputs'])
                total_output_value = sum(output_tx.get('value', 0) for output_tx in tx['outputs'])
                fee = total_input_value - total_output_value
                print(f"Комиссия: {fee} сатоши")
        else:
            print(f"[Ошибка]: По адресу {address} не совершалось ни одной транзакции.")
    except ConnectionError:
        print(f"[Ошибка]: Не удалось подключиться к ресурсу. Проверьте соединение и попробуйте снова.")
        print("[Внимание]: Возврат в меню...")          