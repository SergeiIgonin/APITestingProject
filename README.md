**Демонстрационный проект по автоматизации тестирования  WEB API.** 

Перед запуском автотестов необходимо клонировать данный репозиторий в IDE на вашем ПК, выполнив в его терминале команду:
**git clone https://github.com/SergeiIgonin/APITestingProject.git**
затем перейти в его директорию: **cd APITestingProject**

1. Установка зависимостей:
```bash
pip install -r requirements.txt
```
2. Запуск автотестов с генерацией allur-отчета:
```bash
pytest -v --alluredir=allure-results
```
3. Просмотр allur-отчета:
```bash
allure serve allure-results 
```
4.  При наличии на вашем ПК установленного и запущенного DockerDesktop вы также можете смонтировать docker-образ на основе docker-файла: 
```bash
docker build . -t docker_api_tests     
```
5. Для запуска автотестов внутри запущенного docker-контейнера в команде нужно указать абсолютный путь до папки
allure-results, которая будет создана в корне проекта автоматически:
```bash
docker run --rm -v D:*абсолютный путь к будущей папке allure-results*:/allure-results docker_api_tests
```
6. После прохождения тестов в docker-контейнере в корневой директории проекта автоматически создастся папка
"allure-results" из которой можно сгенерировать allure-отчет:
```bash
allure serve allure-results 
```
7. Для запуска автотестов удаленно на виртуальных машинах GitHub перейдите во вкладку "Actions" данного репозитория, выберите Actions
**"Automated WEB API tests"**, затем выберите и запустите workflow
