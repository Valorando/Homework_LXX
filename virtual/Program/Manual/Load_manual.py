def load_manual():
    try:
        with open('rules.txt', 'r', encoding='utf-8') as file:
            content = file.read()
            if content.strip():
                print(content)
            else:
                print("[Ошибка]: Файл пуст. Пожалуйста, проверьте его содержимое.")
    except FileNotFoundError:
        print("[Ошибка]: Файл 'rules.txt' не найден. Убедитесь, что он существует в нужной директории.")
    except Exception as e:
        print(f"[Ошибка]: Произошла непредвиденная ошибка: {str(e)}")
