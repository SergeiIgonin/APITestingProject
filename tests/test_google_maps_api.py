import allure
from utils.services.google_maps_api import GoogleMapsApi
from utils.checking import Checking


@allure.epic('Test create place')
class TestCreatePlace:
    """Класс содержащий тест по работе с локацией"""
    @allure.title('Test create, read, upgrade, delete new place')
    def test_create_new_place(self):
        """Тест по созданию, изменению и удалению новой локации"""

        print("\nМетод POST")
        response_post = GoogleMapsApi.create_new_place()  # отправка метода POST для создания новой локации
        Checking.check_json_fields(response_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Checking.check_json_value(response_post, 'status', 'OK')
        Checking.check_status_code(response_post, 200)
        check_post = response_post.json()
        place_id = check_post.get("place_id")  # получения place_id для метода GET

        print("Метод GET POST")
        response_get = GoogleMapsApi.get_new_place(place_id)  # отправка метода GET для получения локации по place_id
        Checking.check_json_fields(response_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_status_code(response_get, 200)

        print("\nМетод PUT")
        response_put = GoogleMapsApi.put_new_place(place_id)  # изменение данных о созданной локации
        Checking.check_json_fields(response_put, ['msg'])
        Checking.check_json_value(response_put, 'msg', 'Address successfully updated')
        Checking.check_status_code(response_put, 200)

        print("Метод GET PUT")
        response_get = GoogleMapsApi.get_new_place(place_id)  # отправка метода Get
        Checking.check_json_fields(response_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_status_code(response_get, 200)

        print("\nМетод DELETE")
        response_delete = GoogleMapsApi.delete_new_place(place_id)  # удаление данных о созданной локаpytest -sv ции
        Checking.check_json_fields(response_delete, ['status'])
        Checking.check_json_value(response_delete, 'status', 'OK')
        Checking.check_status_code(response_delete, 200)

        print("Метод GET DELETE")
        response_get = GoogleMapsApi.get_new_place(place_id)  # отправка метода Get
        Checking.check_json_fields(response_get, ['msg'])
        Checking.check_json_search_word_in_value(response_get, 'msg', 'failed' )
        Checking.check_status_code(response_get, 404)
