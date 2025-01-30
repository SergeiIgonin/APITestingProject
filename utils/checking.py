import json


class Checking:
    @staticmethod
    def check_status_code(result, status_code):
        """Метод для проверки статус кода"""
        assert status_code == result.status_code, 'ОШИБКА, Статус-код не совпадает'
        print(f'Статус код = {result.status_code} (корректный)')

    @staticmethod
    def check_json_fields(result, expected_fields):
        """Метод для проверки наличия обязательных полей в ответе запроса"""
        fields = json.loads(result.text)
        assert list(fields) == expected_fields, 'ОШИБКА, Список полей не совпадает'
        print(f'Обязательные поля: {list(fields)}')
        print('Все обязательные поля присутствуют в response')

    @staticmethod
    def check_json_value(result, field_name, expected_value):
        """Метод для проверки значений обязательных полей в ответе запроса"""
        check = result.json()
        check_info = check.get(field_name)
        assert check_info == expected_value, 'ОШИБКА, Значение поля не совпадает'
        print(f'Значение поля {field_name} = {check_info}')
        print(f'Значение поля {field_name} верно!')

    @staticmethod
    def check_json_search_word_in_value(result, field_name, search_word):
        """Метод для проверки значений обязательных полей в ответе запроса при помощи поиска по определенному слову"""
        check = result.json()
        check_info = check.get(field_name)
        assert search_word in check_info
        print(f'Слово {search_word} присутствует в значении поля')