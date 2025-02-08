import requests, allure


class HttpMethods:
    """Класс по хранению HTTP методов"""

    headers = {'Content-type': 'application/json'}  # Заголовки нашего проекта
    cookie = ""  # Куки нашего проекта

    @staticmethod
    def get(url):
        with allure.step("GET"):
            response = requests.get(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
            return response

    @staticmethod
    def post(url, body):
        with allure.step("POST"):
            result = requests.post(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
            return result

    @staticmethod
    def put(url, body):
        with allure.step("PUT"):
            result = requests.put(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
            return result

    @staticmethod
    def delete(url, body):
        with allure.step("DELETE"):
            result = requests.delete(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
            return result
