from Program.Transaction_Tests.Tests import validate_address_and_key_test , authenticity_address_test, validate_amount_test , solvency_sender_test
from Program.Transaction.Get_UTXO import get_utxo
from Program.Transaction.Decode_Transaction import decode_transaction
from bit import PrivateKeyTestnet

def create_transaction():
    sender_address = input("Вставьте сюда адрес отправителя: ")
    base58_key = input("Вставьте сюда приватный ключ отправителя: ")
    receiver_address = input("Вставьте сюда адрес получателя: ")
    amount = input("Введите сумму перевода: ")

    print("\n\n[Внимание]: Введённая вами информация для совершения транзакции")
    print(f"Адрес отправителя: {sender_address}")
    print(f"Приватный ключ отправителя: {base58_key}")
    print(f"Адрес получателя: {receiver_address}")
    print(f"Сумма перевода: {amount} сатоши")
    print(f"[Внимание]: За транзакцию взимается комиссия, она зависит от суммы перевода, нагрузки на сеть и размера транзакции. Будьте к этому готовы!")

    print("\n\n[Внимание]: Выполняется проверка валидности адресов и ключа...")

    sender_address_validate_test = validate_address_and_key_test(sender_address, "Адрес отправителя")
    if sender_address_validate_test == False:
        return False
    
    receiver_address_validate_test = validate_address_and_key_test(receiver_address, "Адрес получателя")
    if receiver_address_validate_test == False:
        return False
    
    base58_key_validate_test = validate_address_and_key_test(base58_key, "Приватный ключ отправителя")
    if base58_key_validate_test == False:
        return False

    print("\n\n[Внимание]: Выполняется проверка достоверности адресов и ключа...")

    sender_address_authenticity_test = authenticity_address_test(sender_address, "Адрес отправителя")
    if sender_address_authenticity_test == False:
        return False
    
    receiver_address_authenticity_test = authenticity_address_test(receiver_address, "Адрес получателя")
    if receiver_address_authenticity_test == False:
        return False

    try:
        key = PrivateKeyTestnet(base58_key)
        print(f"[Успешно]: Приватный ключ отправителя достоверен.")
    except Exception:
        print(f"[Ошибка]: Приватнаый ключ отправителя недостоверен.")
        print("[Внимание]: Создание транзакции отменено, возврат в меню...")
        return False


    print("\n\n[Внимание]: Выполняется проверка валидности суммы...")

    amount_test = validate_amount_test(amount, "Сумма перевода")
    if amount_test == False:
        return False

    print("\n\n[Внимание]: Выполняется проверка платежеспособности отправителя...")

    solvency_test = solvency_sender_test(sender_address, amount)
    if solvency_test == False:
        return False

    print("\n\n[Внимание]: Выполняется поиск UTXO по адресу отправителя...")

    utxo_search = get_utxo(sender_address, amount)
    if utxo_search == False:
        return False

    print("\n\n[Внимание]: Выполняется построение транзакции...")

    try:
        tx = key.create_transaction([(receiver_address, amount, 'satoshi')])
        print(f"[Успешно]: Транзакция построена, HEX: {tx}")
    except Exception as e:
        print(f"[Ошибка]: Транзакция не построенна: {str(e)}.")
        print("[Внимание]: Создание транзакции отменено, возврат в меню...")
        return False

    print("\n\n[Внимание]: Выполняется декодирование HEX-a транзакц...")

    try:
        transaction_info = decode_transaction(tx)
        print("[Успешно]: Транзакция декодирована.")
        print(f"Адрес отправителя: {', '.join(transaction_info['sender_addresses'])}")
        print(f"Адрес получателя: {', '.join(transaction_info['receiver_addresses'])}")
        print(f"Сумма отправки: {transaction_info['amount_sent']} сатоши")
        print(f"Сумма комиссии: {transaction_info['fee']} сатоши")

    except Exception as e:
        print(f"[Ошибка]: Транзакция не декодирована: {str(e)}.")
        print("[Внимание]: Создание транзакции отменено, возврат в меню...")
        return False

    print("\n\n[Внимание]: Транзакция готова к отправке...")
    print("[Внимание]: Если желаете отправить эту транзакцию в сеть - введите Y и нажмите Enter.")
    print("[Внимание]: В противном случае введите любое другое значение и тоже нажмите Enter")
    choice = input("Поле для ввода: ")
    if choice == "Y":
        tx = key.send([(receiver_address, amount, 'satoshi')])
        print(f"[Успешно]: Транзакция отправлена, Txid: {tx} , возврат в меню...")
        return False
    else:
        print("[Успешно]: Пользователь отменил отправку транзакции, возврат в меню...")
        return False   