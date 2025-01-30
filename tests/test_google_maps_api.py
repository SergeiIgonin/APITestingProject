from utils.api import GoogleMapsApi
from utils.checking import Checking


class TestCreatePlace:
    """Класс содержащий тест по работе с локацией"""

    def test_create_new_place(self):
        """Тест по созданию, изменению и удалению новой локации"""

        print("\nМетод POST")
        result_post = GoogleMapsApi.create_new_place()  # отправка метода POST для создания новой локации
        Checking.check_json_fields(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Checking.check_json_value(result_post, 'status', 'OK')
        Checking.check_status_code(result_post, 200)
        check_post = result_post.json()
        place_id = check_post.get("place_id")  # получения place_id для метода GET

        print("Метод GET POST")
        result_get = GoogleMapsApi.get_new_place(place_id)  # отправка метода GET для получения локации по place_id
        Checking.check_json_fields(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_status_code(result_get, 200)

        print("\nМетод PUT")
        result_put = GoogleMapsApi.put_new_place(place_id)  # изменение данных о созданной локации
        Checking.check_json_fields(result_put, ['msg'])
        Checking.check_json_value(result_put, 'msg', 'Address successfully updated')
        Checking.check_status_code(result_put, 200)

        print("Метод GET PUT")
        result_get = GoogleMapsApi.get_new_place(place_id)  # отправка метода Get
        Checking.check_json_fields(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_status_code(result_get, 200)

        print("\nМетод DELETE")
        result_delete = GoogleMapsApi.delete_new_place(place_id)  # удаление данных о созданной локации
        Checking.check_json_fields(result_delete, ['status'])
        Checking.check_json_value(result_delete, 'status', 'OK')
        Checking.check_status_code(result_delete, 200)

        print("Метод GET DELETE")
        result_get = GoogleMapsApi.get_new_place(place_id)  # отправка метода Get
        Checking.check_json_fields(result_get, ['msg'])
        Checking.check_json_search_word_in_value(result_get, 'msg', 'failed' )
        Checking.check_status_code(result_get, 404)
