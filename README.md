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



Этот проект лицензирован под лицензией MIT.
