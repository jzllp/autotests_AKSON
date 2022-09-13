# How to run:
#  1) Download driver for Chrome:
#     https://chromedriver.chromium.org/downloads
#  2) Install all required python packages library
#
#  3) Run in terminal with line:
#     python -m pytest -v --driver Chrome --driver-path <~>/chromedriver.exe tests/04_test_Card_product.py

from pages.akson_locators import Header_sticky, Header_top, Card_product


def test_Card_product_01(web_browser):
    """ Проверка перехода в карточку товара. """

    page = Header_sticky(web_browser)
    page_city = Header_top(web_browser)
    page_card = Card_product(web_browser)

    page_city.choice_location.click()
    page.search_menu = "лестница"
    page.search_button.click()
    page.result_product.click()

    assert page_card.card_in_card.find(), 'Раздел карточки товара не найден'


def test_Card_product_02(web_browser):
    """ Проверка соответствия названия товара в поиске и в карточке товара. """

    page = Header_sticky(web_browser)
    page_city = Header_top(web_browser)
    page_card = Card_product(web_browser)

    page_city.choice_location.click()
    page.search_menu = "лестница"
    page.search_button.click()
    header = page.result_product.get_text()
    page.result_product.click()

    assert header == page_card.title_card.get_text(), 'Название в заголовках не совпадают'


def test_Card_product_03(web_browser):
    """ Проверка соответствия кода товара в поиске и в карточке товара. """

    page = Header_sticky(web_browser)
    page_city = Header_top(web_browser)
    page_card = Card_product(web_browser)

    page_city.choice_location.click()
    page.search_menu = "лестница"
    page.search_button.click()
    code = page_card.result_code.get_text()
    page.result_product.click()

    assert code == page_card.card_code.get_text(), 'Коды товара не совпадают'


def test_Card_product_04(web_browser):
    """ Проверка соответствия цены товара в поиске и в карточке товара. """

    page = Header_sticky(web_browser)
    page_city = Header_top(web_browser)
    page_card = Card_product(web_browser)

    page_city.choice_location.click()
    page.search_menu = "лестница"
    page.search_button.click()
    price = page_card.result_price.get_text()
    page.result_product.click()

    assert price == page_card.card_price.get_text().replace(' ₽ / шт', ''), 'Цена товара не совпадает'


def test_Card_product_05(web_browser):
    """ Активация функции 'Сравнить товары'. """

    page = Header_sticky(web_browser)
    page_city = Header_top(web_browser)
    page_card = Card_product(web_browser)

    page_city.choice_location.click()
    page.search_menu = "лестница"
    page.search_button.click()
    page.result_product.click()
    page_card.product_comparison.click()

    assert page.authorization.find(), "Функция 'Сравнить товары' не активировалась"


def test_Card_product_06(web_browser):
    """ Активация миниатюры фото товара. """

    page = Header_sticky(web_browser)
    page_city = Header_top(web_browser)
    page_card = Card_product(web_browser)

    page_city.choice_location.click()
    page.search_menu = "лестница"
    page.search_button.click()
    page.result_product.click()
    page_card.photo_box.click()

    assert page_card.photo_full.find(), "Фото товара не активировалось"


def test_Card_product_07(web_browser):
    """ Переход к разделу меню 'Характеристики' товара. """

    page = Header_sticky(web_browser)
    page_city = Header_top(web_browser)
    page_card = Card_product(web_browser)

    page_city.choice_location.click()
    page.search_menu = "лестница"
    page.search_button.click()
    page.result_product.click()
    page_card.characteristics_link.scroll_to_element()
    page_card.characteristics_link.click()

    assert page_card.characteristics.is_visible(), "Переход к разделу меню 'Характеристики' товара не активировался."


def test_Card_product_08(web_browser):
    """ Переход к разделу меню 'Отзывы о товаре'. """

    page = Header_sticky(web_browser)
    page_city = Header_top(web_browser)
    page_card = Card_product(web_browser)

    page_city.choice_location.click()
    page.search_menu = "лестница"
    page.search_button.click()
    page.result_product.click()
    page_card.reviews_link.scroll_to_element()
    page_card.reviews_link.click()

    assert page_card.reviews.is_visible(), "Переход к разделу меню 'Отзывы о товаре' не активировался."


def test_Card_product_09(web_browser):
    """ Переход к разделу меню 'Вопросы и ответы покупателей'. """

    page = Header_sticky(web_browser)
    page_city = Header_top(web_browser)
    page_card = Card_product(web_browser)

    page_city.choice_location.click()
    page.search_menu = "лестница"
    page.search_button.click()
    page.result_product.click()
    page_card.answers_link.scroll_to_element()
    page_card.answers_link.click()

    assert page_card.answers.is_visible(), "Переход к разделу меню 'Вопросы и ответы покупателей' не активировался."


def test_Card_product_10(web_browser):
    """ Переход к разделу меню 'Похожие товары'. """

    page = Header_sticky(web_browser)
    page_city = Header_top(web_browser)
    page_card = Card_product(web_browser)

    page_city.choice_location.click()
    page.search_menu = "лестница"
    page.search_button.click()
    page.result_product.click()
    page_card.recommend_link.scroll_to_element()
    page_card.recommend_link.click()

    assert page_card.recommend.is_visible(), "Переход к разделу меню 'Похожие товары' не активировался."


def test_Card_product_11(web_browser):
    """ Проверка кнопки выхода из карточки товара. """

    page = Header_sticky(web_browser)
    page_city = Header_top(web_browser)
    page_card = Card_product(web_browser)

    page_city.choice_location.click()
    page.search_menu = "лестница"
    page.search_button.click()
    page.result_product.click()

    assert page_card.card_in_card.find(), 'Раздел карточки товара не найден'

    page_card.btn_backwards.click()

    assert page.result_product.find(), "Выход из карточки товара не активировался."
