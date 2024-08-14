from Program.Manual.Load_manual import load_manual
from Program.Balance.Get_balance import get_balance
from Program.Transaction.Get_all_transactions import get_all_transactions
from Program.Transaction.Create_Transaction import create_transaction
from Program.Generating_Keys.Key_and_address_generating import generate_keys

while True:
    print()
    print("Для выбора необходимой вам опции введите её номер и нажмите Enter.")
    print("1 - Посмотреть руководство(прочтите перед использованием опций).")
    print("2 - Посмотреть баланс кошелька.")
    print("3 - Посмотреть историю транзакций.")
    print("4 - Провести транзакцию.")
    print("5 - Сгенерировать адрес и ключ для кошелька.")
    print("6 - Выйти.")
    print()

    selected_option = int(input("Поле для ввода: "))
    print()
    match selected_option:
        case 1:
            print()
            load_manual()
            print()
        case 2:
            print()
            get_balance()
            print()
        case 3:
            print()
            get_all_transactions()
            print()
        case 4:
            print()
            create_transaction()
            print()
        case 5:
            print()
            generate_keys()
            print()                
        case 6:
            exit(0)
        case _:
            print()
            print("Введёное вами значение отсутствует в списке опций.")