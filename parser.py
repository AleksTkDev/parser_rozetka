# import csv
# import time
# import random
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
#
# header = {
#     'User-Agent':
#         'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
#         '(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
#     'Accept':
#         'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
# }
#
#
# def get_data_by_selenium(url: str) -> str:
#     """ Звертається до сервера за url адресою і повертає HTML сайту"""
#     service = Service(path="geckodriver")
#     driver = webdriver.Chrome(service=service)
#     driver.get(url)
#     time.sleep(random_sleep())
#     data = driver.page_source
#     driver.quit()
#     return data
#
#
# def parse_data(data: str) -> list:
#     """ Функція парсингу даних з хтмл документа"""
#     rez = []
#     if data:
#         soup = BeautifulSoup(data, 'html.parser')
#         li_list = soup.find_all('li', attrs={'class': 'catalog-grid__cell'})
#         for li in li_list:
#             # Пошук тега а
#             a = li.find('a', attrs={'class': 'goods-tile__heading'})
#             # Беремо у тега а атрибут href
#             href = a['href']
#             # За допомогою атрибуту текст, забираємо всю текстову
#             # інформацію, що міститься в цьому тегу
#             title = a.text
#             old = li.find('div', attrs={'class': 'goods-tile__price--old'})
#             price = li.find('div', attrs={'class': 'goods-tile__price'})
#             # Стара ціна є не у всіх, тому потрібно зробити дефолтне значення
#             old_price = ''
#             if old:
#                 # Якщо контейнер із старою ціною є
#                 old = old.text
#                 # І в цьому контейнер є інфа
#                 if old:
#                     # Забираємо лише те, що є цифрами та формуємо значення ціни
#                     old_price = int(''.join(c for c in old if c.isdigit()))  #14500
#             # Звичайна ціна є скрізь, тому формуємо значення
#             price = int(''.join(c for c in price.text if c.isdigit()))
#             # Результат за кожною відеокартою записуємо у вигляді словника
#             rez.append({
#                 'title': title, 'href': href, 'price': price,
#                 'old_price': old_price
#             })
#     return rez
#
#
# def save_to_csv(rows) -> None:
#     """Функція збереження даних у csv-файл"""
#     csv_title = ['title', 'href', 'price', 'old_price', ]
#     with open('videocards.csv', 'w') as f:
#         writer = csv.DictWriter(f, fieldnames=csv_title, delimiter=';')
#         writer.writeheader()
#         writer.writerows(rows)
#
#
# def main() -> None:
#     """ Головна функція диригент"""
#     url = 'https://hard.rozetka.com.ua/videocards/c80087/page={}/'
#     rows = []
#     for i in range(1, 3):
#         data = get_data_by_selenium(url.format(i))
#         rows += parse_data(data)
#         time.sleep(random_sleep())
#
#     save_to_csv(rows)
#
#
# def random_sleep():
#     return random.randint(1, 10)
#
#
# if __name__ == '__main__':
#     main()
#


# or
import csv
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}


def get_data_by_selenium(url: str) -> str:
    """Звертається до сервера за url адресою і повертає HTML сайту"""
    service = Service('chromedriver')  # убедитесь, что у вас установлен chromedriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument(f'user-agent={header["User-Agent"]}')

    with webdriver.Chrome(service=service, options=options) as driver:
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'catalog-grid__cell'))
        )
        time.sleep(random_sleep(2, 6))  # более короткое случайное ожидание
        data = driver.page_source
    return data


def parse_data(data: str) -> list:
    """Функція парсингу даних з HTML документа"""
    rez = []
    if data:
        soup = BeautifulSoup(data, 'html.parser')
        li_list = soup.find_all('li', class_='catalog-grid__cell')
        for li in li_list:
            a = li.find('a', class_='goods-tile__heading')
            if not a:
                continue
            href = a['href']
            title = a.text.strip()
            old = li.find('div', class_='goods-tile__price--old')
            price = li.find('div', class_='goods-tile__price')

            old_price = ''
            if old:
                old_price_text = old.text
                if old_price_text:
                    old_price = int(''.join(c for c in old_price_text if c.isdigit()))

            price = int(''.join(c for c in price.text if c.isdigit())) if price else 0
            rez.append({'title': title, 'href': href, 'price': price, 'old_price': old_price})
    return rez


def save_to_csv(rows) -> None:
    """Функція збереження даних у CSV-файл"""
    csv_title = ['title', 'href', 'price', 'old_price']
    with open('videocards.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=csv_title, delimiter=';')
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    """Головна функція диригент"""
    url = 'https://hard.rozetka.com.ua/videocards/c80087/page={}/'
    rows = []
    for i in range(1, 3):
        data = get_data_by_selenium(url.format(i))
        rows += parse_data(data)
        time.sleep(random_sleep(3, 10))
    save_to_csv(rows)


def random_sleep(min_seconds=1, max_seconds=10):
    return random.randint(min_seconds, max_seconds)


if __name__ == '__main__':
    main()
