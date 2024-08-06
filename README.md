# Graphics Cards Parser for Rozetka.ua

## Description

This script is designed to parse information about graphics cards from the Rozetka website and save the data to a CSV file. It uses the `selenium` library to retrieve the HTML page, `BeautifulSoup` for HTML parsing, and `csv` for data storage.

## Requirements

- Python 3.x
- Libraries: `selenium`, `beautifulsoup4`, `csv`
- WebDriver for Chrome (chromedriver)

## Dependency Installation

Install the required libraries using pip:

```sh
pip install selenium beautifulsoup4
```

Make sure you have `chromedriver` installed and accessible in your PATH.

## Function Descriptions

### `get_data_by_selenium(url: str) -> str`

Fetches the HTML code of the page at the specified URL using Selenium.

**Parameters:**
- `url` (str): The URL of the page to load.

**Returns:**
- `str`: The HTML code of the page.

### `parse_data(data: str) -> list`

Parses data from the HTML document.

**Parameters:**
- `data` (str): The HTML code of the page.

**Returns:**
- `list`: A list of dictionaries with data about graphics cards. Each dictionary contains the following keys:
  - `title` (str): The name of the graphics card.
  - `href` (str): The link to the graphics card's page.
  - `price` (int): The current price.
  - `old_price` (int): The old price.

### `save_to_csv(rows: list) -> None`

Saves data to a CSV file.

**Parameters:**
- `rows` (list): A list of dictionaries with data about graphics cards.

**Returns:**
- None

### `main() -> None`

The main function that orchestrates the process of retrieving and saving data.

**Parameters:**
- None

**Returns:**
- None

### `random_sleep(min_seconds=1, max_seconds=10) -> int`

Returns a random sleep time in seconds.

**Parameters:**
- `min_seconds` (int): The minimum sleep time.
- `max_seconds` (int): The maximum sleep time.

**Returns:**
- `int`: A random sleep time in seconds.

## Usage Example

To run the script, execute the command:

```sh
python your_script.py
```

The script will gather data about graphics cards from the Rozetka website and save it to a file named `videocards.csv`.

## Notes

- Ensure you have `chromedriver` installed and it is in your PATH.
- The script processes pages with graphics cards using Selenium for loading pages and BeautifulSoup for parsing.
- Data is saved in a CSV file with a `;` delimiter.

## License

This project is licensed under the MIT License.


***


# Парсер видеокарт с сайта Rozetka.ua

## Описание

Этот скрипт предназначен для парсинга информации о видеокартах с сайта Rozetka и сохранения данных в CSV файл. Он использует библиотеку `selenium` для получения HTML страницы, `BeautifulSoup` для парсинга HTML, и `csv` для сохранения данных.

## Требования

- Python 3.x
- Библиотеки: `selenium`, `beautifulsoup4`, `csv`
- WebDriver для браузера Chrome (chromedriver)

## Установка зависимостей

Установите необходимые библиотеки с помощью pip:

```sh
pip install selenium beautifulsoup4
```

Убедитесь, что у вас установлен `chromedriver` и он доступен в PATH.

## Описание функций

### `get_data_by_selenium(url: str) -> str`

Забирает HTML-код страницы по указанному URL с использованием Selenium.

**Параметры:**
- `url` (str): URL страницы, которую нужно загрузить.

**Возвращает:**
- `str`: HTML-код страницы.

### `parse_data(data: str) -> list`

Парсит данные из HTML документа.

**Параметры:**
- `data` (str): HTML-код страницы.

**Возвращает:**
- `list`: Список словарей с данными о видеокартах. Каждый словарь содержит следующие ключи:
  - `title` (str): Название видеокарты.
  - `href` (str): Ссылка на страницу видеокарты.
  - `price` (int): Текущая цена.
  - `old_price` (int): Старая цена.

### `save_to_csv(rows: list) -> None`

Сохраняет данные в CSV файл.

**Параметры:**
- `rows` (list): Список словарей с данными о видеокартах.

**Возвращает:**
- None

### `main() -> None`

Главная функция, которая оркестрирует процесс получения и сохранения данных.

**Параметры:**
- Нет

**Возвращает:**
- None

### `random_sleep(min_seconds=1, max_seconds=10) -> int`

Возвращает случайное значение времени ожидания в секундах.

**Параметры:**
- `min_seconds` (int): Минимальное значение времени ожидания.
- `max_seconds` (int): Максимальное значение времени ожидания.

**Возвращает:**
- `int`: Случайное значение времени ожидания в секундах.

## Пример использования

Для запуска скрипта выполните команду:

```sh
python your_script.py
```

Скрипт соберет данные с сайта Rozetka о видеокартах и сохранит их в файл `videocards.csv`.

## Примечания

- Убедитесь, что у вас установлен `chromedriver` и он находится в PATH.
- Скрипт обрабатывает страницы с видеокартами, используя Selenium для загрузки страниц и BeautifulSoup для парсинга.
- Данные сохраняются в CSV файл с разделителем `;`.

## Лицензия

Этот проект лицензирован под лицензией MIT.
