from mnemonic import Mnemonic
from hashlib import sha256
from hmac import new as hmac_new
from bit import PrivateKeyTestnet

def generate_keys():
    print("[Внимание]: Если желаете использовать собственную mnemo-фразу для генерации - введите Y и нажмите Enter.")
    print("[Внимание]: В противном случае введите любое другое значение и тоже нажмите Enter")
    choice = input("Поле для ввода: ")
    
    if choice == "Y":
        user_mnemo = input("Вставьте сюда свою mnemo-фразу: ").strip()
        if not user_mnemo:
            print("[Ошибка]: Введённая вами строка оказалась пустой.")
            print("[Внимание]: Возврат в меню...")
            return False
        
        mnemo = Mnemonic("english")
        if not mnemo.check(user_mnemo):
            print("[Ошибка]: Введённая вами mnemo-фраза не является корректной.")
            print("[Внимание]: Возврат в меню...")
            return False
        
        print("[Внимание]: Выполняется генерация ключа и адреса...")
        seed = mnemo.to_seed(user_mnemo)
        master_key = hmac_new(b"Bitcoin seed", seed, sha256).digest()
        private_key = master_key[:32]
        key = PrivateKeyTestnet.from_bytes(private_key)
        wif = key.to_wif()
        address = key.address
        print("[Успешно]: Сгенерированные ключ и адрес из вашей mnemo-фразы...")
        print(f"Mnemo-фраза: {user_mnemo}")
        print(f"Приватный ключ формата Base58: {wif}")
        print(f"Адрес кошелька формата Legacy: {address}")
    else:
        print("[Внимание]: Выполняется генерация ключа и адреса...")
        mnemo = Mnemonic("english")
        mnemonic_phrase = mnemo.generate(strength=128)
        seed = mnemo.to_seed(mnemonic_phrase)
        master_key = hmac_new(b"Bitcoin seed", seed, sha256).digest()
        private_key = master_key[:32]
        key = PrivateKeyTestnet.from_bytes(private_key)
        wif = key.to_wif()
        address = key.address
        print("[Успешно]: Сгенерированные ключ и адрес...")
        print(f"Mnemo-фраза: {mnemonic_phrase}")
        print(f"Приватный ключ формата Base58: {wif}")
        print(f"Адрес кошелька формата Legacy: {address}")