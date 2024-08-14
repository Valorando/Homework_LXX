import requests

def get_utxo(address, amount):
    try:
        amount = int(amount)
        url = f'https://api.blockcypher.com/v1/btc/test3/addrs/{address}?unspentOnly=true'
        response = requests.get(url)
        if response.status_code == 200:
            utxo_list = response.json().get('txrefs', [])
        else:
            print("[Ошибка]: Не удалось получить UTXO по адресу отправителя.")
            print("[Внимание]: Создание транзакции отменено, возврат в меню...")
            return False
        
        if not utxo_list:
            print("[Ошибка]: По адресу отправителя не обнаружено ни одного UTXO.")
            print("[Внимание]: Создание транзакции отменено, возврат в меню...")
            return False
        else:
            print(f"[Успешно]: По адресу отправителя обнаружено {len(utxo_list)} UTXO:")
        total_available = 0 
        for i, utxo in enumerate(utxo_list, start=1):
            print(f"\nUTXO №{i}:")
            print(f"  - Хэш транзакции: {utxo['tx_hash']}")
            print(f"  - Высота блока: {utxo['block_height']}")
            print(f"  - Номер входа в транзакции: {utxo['tx_input_n']}")
            print(f"  - Номер выхода в транзакции: {utxo['tx_output_n']}")
            print(f"  - Значение: {utxo['value']}")
            print(f"  - Баланс после этой транзакции: {utxo['ref_balance']}")
            print(f"  - Потрачен: {'Да.' if utxo['spent'] else 'Нет.'}")
            print(f"  - Количество подтверждений: {utxo['confirmations']}")
            print(f"  - Время подтверждения: {utxo['confirmed']}")
            print(f"  - Двойная трата: {'Да.' if utxo['double_spend'] else 'Нет.'}")

        total_available += utxo['value']

        print(f"\n\n[Внимание]: Выполняется проверка палежеспособности на основе UTXO...")
        if total_available >= amount:
            print(f"[Успешно]: На балансе достаточно средств для совершения транзакции.")
        else:
            print(f"[Ошибка]: На балансе недостаточно средств для совершения транзакции.")
            print("[Внимание]: Создание транзакции отменено, возврат в меню...")
            return False

    except ConnectionError:
        print(f"[Ошибка]: Не удалось подключиться к ресурсу. Проверьте соединение и попробуйте снова.")
        print("[Внимание]: Создание транзакции отменено, возврат в меню...")
        return False