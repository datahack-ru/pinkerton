# Pinkerton [![Build Status](https://travis-ci.org/bureaucratic-labs/pinkerton.svg?branch=master)](https://travis-ci.org/bureaucratic-labs/pinkerton)

<img align="right" src="http://i.imgur.com/gRXgf48.png">

`Pinkerton` связывает именованные сущности, упоминаемые в тексте на естественном языке, с данными в внешних хранилищах данных (например, Wikipedia, DaData.ru и др.).

При разборе результатов, `Pinkerton` определяет контекст, в котом упоминается сущность и выбирает наиболее подходящий вариант ответа - так, например, можно быть уверенным, что для персоны `Иван Васильевич`, которая упоминается в контексте художественного фильма, будет выбрана правильная статья из Wikipedia. 

Общая цель этого проекта - сделать открытую и расширяемую альтернативу [Яндекс.Карточкам](https://yandex.ru/promo/yobject/)

# TODO:

- [ ] Извлечение именованных сущностей (отдельный сервис)
- [ ] Поддержка нескольких языков
- [x] Поиск данных в Wikipedia
- [x] Поиск адресов в Yandex Maps
- [x] Сравнение контекстов через LDA

# Быстрый старт:

```bash
$ python --version
Python 3.6.0
$ pip install pinkerton
$ python -m pinkerton
======== Running on http://127.0.0.1:4000 ========
(Press CTRL+C to quit)
```

# API

## Общая информация: `/version`

```bash
$ http http://localhost:4000/version

HTTP/1.1 200 OK
Content-Length: 20
Content-Type: application/json; charset=utf-8
Date: Sun, 07 May 2017 09:49:29 GMT
Server: Python/3.6 aiohttp/2.0.7

{
    "version": "0.0.1"
}
```
