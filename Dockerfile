# для сборки образа выполнить: docker build . -t docker_api_tests
# для сборки контейнера выполнить: docker run --rm -v D:\PycharmProjects\APITestingProject\allure-results:/allure-results docker_api_tests
# для просмотра Allure-отчета выполнить: allure serve allure-results

FROM python:3.10-alpine3.19
COPY . .
RUN pip install -r requirements.txt
RUN apk add --no-cache chromium chromium-chromedriver tzdata
RUN mkdir allure-results
CMD ["pytest", "-v", "tests", "--alluredir=allure-results"]
