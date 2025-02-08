import json


class Checking:
    @staticmethod
    def check_status_code(response, status_code):
        """Метод для проверки статус кода"""
        assert status_code == response.status_code, 'ОШИБКА, Статус-код не совпадает'
        print(f'Статус код = {response.status_code} (корректный)')

    @staticmethod
    def check_json_fields(response, expected_fields):
        """Метод для проверки наличия обязательных полей в ответе запроса"""
        fields = json.loads(response.text)
        assert list(fields) == expected_fields, 'ОШИБКА, Список полей не совпадает'
        print(f'Обязательные поля: {list(fields)}')
        print('Все обязательные поля присутствуют в response')

    @staticmethod
    def check_json_value(response, field_name, expected_value):
        """Метод для проверки значений обязательных полей в ответе запроса"""
        response_json = response.json()
        field_name = response_json.get(field_name)
        assert field_name == expected_value, 'ОШИБКА, Значение поля не совпадает'
        print(f'Значение поля {field_name} = {field_name}')
        print(f'Значение поля {field_name} верно!')

    @staticmethod
    def check_json_search_word_in_value(response, field_name, search_word):
        """Метод для проверки значений обязательных полей в ответе запроса при помощи поиска по определенному слову"""
        response_json = response.json()
        field_name = response_json.get(field_name)
        assert search_word in field_name
        print(f'Слово {search_word} присутствует в значении поля')