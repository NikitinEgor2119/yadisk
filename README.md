Проект для скачивания файлов по публичной ссылке с API Яндекс.Диска. 

## Описание

Данный проект позволяет взаимодействовать с Яндекс.Диском, включая загрузку, скачивание одного или нескольких файлов.

## Установка и запуск

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/NikitinEgor2119/yadisk.git

2. Перейдите в директорию проекта:
    cd yadisk

3. Создайте и активируйте виртуальное окружение:
    bash
    python3 -m venv venv
    source venv/bin/activate  # для macOS и Linux
    venv\Scripts\activate     # для Windows

4. Установите зависимости:
    bash
    pip install -r requirements.txt

5. python manage.py runserver


Перейдите в браузере по адресу http://127.0.0.1:8000/ для доступа к приложению и в поле ввода, введите вашу ссылку.

При помощи галочек вы сможете выбрать сразу несколько файлов и скачать их сразу в ZIP формате.

Данные использованы с источников:
https://yandex.ru/dev/disk-api/doc/ru/reference/public
https://www.djangoproject.com/

Спасибо за внимание!