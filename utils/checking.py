import json


class Checking:
    @staticmethod
    def check_status_code(result, status_code):
        """Метод для проверки статус кода"""
        assert status_code == result.status_code, 'ОШИБКА, Статус-код не совпадает'
        print(f"Статус код = {result.status_code} (корректный)")

    @staticmethod
    def check_json_fields(result, expected_fields):
        """Метод для проверки наличия полей в ответе запроса"""
        fields = json.loads(result.text)
        assert list(fields) == expected_fields, 'ОШИБКА, Список полей не совпадает'
        print(f'Обязательные поля: {list(fields)}')
        print("Все поля присутствуют")