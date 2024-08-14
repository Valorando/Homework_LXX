import requests

def decode_transaction(tx_hex):
    url = 'https://api.blockcypher.com/v1/btc/test3/txs/decode'

    response = requests.post(url, json={'tx': tx_hex})

    if response.status_code != 200:
        print(f"[Ошибка]: Не удалось получить ответ от ресурса: {response.status_code}.")
        return False

    tx_info = response.json()

    sender_addresses = set()
    for input in tx_info.get('inputs', []):
        sender_addresses.update(input.get('addresses', []))

    receiver_addresses = set()
    total_output_value = 0

    for output in tx_info.get('outputs', []):
        if set(output.get('addresses', [])) & sender_addresses:
            continue
        else:
            receiver_addresses.update(output.get('addresses', []))
            total_output_value += output.get('value', 0)

    fee = tx_info.get('fees', 0)
    amount_sent = total_output_value

    return {
        'sender_addresses': list(sender_addresses),
        'receiver_addresses': list(receiver_addresses),
        'amount_sent': amount_sent,
        'fee': fee
    }