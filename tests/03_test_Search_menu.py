# How to run:
#  1) Download driver for Chrome:
#     https://chromedriver.chromium.org/downloads
#  2) Install all required python packages library
#
#  3) Run in terminal with line:
#     python -m pytest -v --driver Chrome --driver-path <~>/chromedriver.exe tests/03_test_Search_menu.py

from pages.akson_locators import Header_sticky, Header_top, Card_product


def test_StartPage_search_menu_01(web_browser):
    """ Проверка меню поиска значением в нижнем регистре. """

    page = Header_sticky(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_location.click()
    page.search_menu = "люстра"
    page.search_button.click()

    assert page.result_product.get_text().find('Люстра') != -1, 'Неверный товар в результате поиска'


def test_StartPage_search_menu_02(web_browser):
    """ Проверка меню поиска значением в верхнем регистре. """

    page = Header_sticky(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_location.click()
    page.search_menu = "ЛЮСТРА"
    page.search_button.click()

    assert page.result_product.get_text().find('Люстра') != -1, 'Неверный товар в результате поиска'


def test_StartPage_search_menu_03(web_browser):
    """ Проверка меню поиска значением в верхнем и нижнем регистрах. """

    page = Header_sticky(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_location.click()
    page.search_menu = "ЛюСтРа"
    page.search_button.click()

    assert page.result_product.get_text().find('Люстра') != -1, 'Неверный товар в результате поиска'


def test_StartPage_search_menu_04(web_browser):
    """ Проверка меню поиска значением с цифрой в начале строки. """

    page = Header_sticky(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_location.click()
    page.search_menu = "1люстра"
    page.search_button.click()

    assert page.result_product.get_text().find('Люстра') != -1, 'Неверный товар в результате поиска'


def test_StartPage_search_menu_05(web_browser):
    """ Проверка меню поиска значением с цифрой в конце строки. """

    page = Header_sticky(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_location.click()
    page.search_menu = "люстра9"
    page.search_button.click()

    assert page.result_product.get_text().find('Люстра') != -1, 'Неверный товар в результате поиска'


def test_StartPage_search_menu_06(web_browser):
    """ Проверка меню поиска значением со спецсимволом в начале строки. """

    page = Header_sticky(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_location.click()
    page.search_menu = "%люстра"
    page.search_button.click()

    assert page.result_product.get_text().find('Люстра') != -1, 'Неверный товар в результате поиска'


def test_StartPage_search_menu_07(web_browser):
    """ Проверка меню поиска значением со спецсимволом в конце строки. """

    page = Header_sticky(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_location.click()
    page.search_menu = "люстра@"
    page.search_button.click()

    assert page.result_product.get_text().find('Люстра') != -1, 'Неверный товар в результате поиска'


def test_StartPage_search_menu_08(web_browser):
    """ Проверка меню поиска значением с неправильной раскладкой клавиатуры. """

    page = Header_sticky(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_location.click()
    page.search_menu = "k.cnhf"
    page.search_button.click()

    assert page.result_product.get_text().find('Люстра') != -1, 'Неверный товар в результате поиска'


def test_StartPage_search_menu_09(web_browser):
    """ Проверка меню поиска значением на английском языке. """

    page = Header_sticky(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_location.click()
    page.search_menu = "chandelier"
    page.search_button.click()

    assert page.result_product.get_text().find('Люстра') != -1, 'Неверный товар в результате поиска'


def test_StartPage_search_menu_10(web_browser):
    """ Проверка меню поиска значением на латинице. """

    page = Header_sticky(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_location.click()
    page.search_menu = "lyustra"
    page.search_button.click()

    assert page.result_product.get_text().find('Люстра') != -1, 'Неверный товар в результате поиска'


def test_StartPage_search_menu_11(web_browser):
    """ Проверка меню поиска значением на китайском языке. """

    page = Header_sticky(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_location.click()
    page.search_menu = "枝形吊燈"
    page.search_button.click()

    assert page.result_product.get_text().find('Люстра') != -1, 'Неверный товар в результате поиска'


def test_StartPage_search_menu_12(web_browser):
    """ Проверка меню поиска значением с дублированием искомого значения. """

    page = Header_sticky(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_location.click()
    page.search_menu = "люстралюстралюстра"
    page.search_button.click()

    assert page.result_product.get_text().find('Люстра') != -1, 'Неверный товар в результате поиска'


def test_StartPage_search_menu_13(web_browser):
    """ Поиск товара по коду. """

    page = Header_sticky(web_browser)
    page_city = Header_top(web_browser)
    page_gard = Card_product(web_browser)

    page_city.choice_location.click()
    page.search_menu = "130980"
    page.search_button.click()

    assert page_gard.card_code.get_text().find('130980') != -1, 'Неверный товар в результате поиска'


def test_StartPage_search_menu_14(web_browser):
    """ Проверка меню поиска значением из цифр. """

    page = Header_sticky(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_location.click()
    page.search_menu = "1595566"
    page.search_button.click()
    page.wait_page_loaded()

    assert page.result_all_goods.is_presented() is False, 'Поиск нашел неверное значение'


def test_StartPage_search_menu_15(web_browser):
    """ Проверка меню поиска значением с пробелами. """

    page = Header_sticky(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_location.click()
    page.search_menu = "л ю с т р а"
    page.search_button.click()

    assert page.result_product.get_text().find('Люстра') != -1, 'Неверный товар в результате поиска'


def test_StartPage_search_menu_16(web_browser):
    """ Проверка меню поиска пустым значением. """

    page = Header_sticky(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_location.click()
    page.search_menu = "      "
    page.search_button.click()

    assert page.result_all_goods.is_presented() is False, 'Поиск нашел неверное значение'


def test_StartPage_search_menu_17(web_browser):
    """ Проверка активации меню поиска без значения. """

    page = Header_sticky(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_location.click()

    assert page.search_button.is_presented() is False, 'Поиск активен'


def test_StartPage_search_menu_18(web_browser):
    """ Проверка меню поиска, ввод значения в 49 символов. """

    page = Header_sticky(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_location.click()
    page.search_menu = "люстралюстралюстралюстралюстралюстралюстралюстра"
    page.search_button.click()

    assert page.result_search.get_text().find('люстралюстралюстралюстралюстралюстралюстралюстра') != -1,\
        'Количество символов в воде и в результате поиска не совпадают'


def test_StartPage_search_menu_19(web_browser):
    """ Проверка меню поиска, ввод значения в 50 символов. """

    page = Header_sticky(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_location.click()
    page.search_menu = "люстралюстралюстралюстралюстралюстралюстралюстрал"
    page.search_button.click()

    assert page.result_search.get_text().find('люстралюстралюстралюстралюстралюстралюстралюстрал') != -1,\
        'Количество символов в воде и в результате поиска не совпадают'


def test_StartPage_search_menu_20(web_browser):
    """ Проверка меню поиска, ввод значения в 99 символов. """

    page = Header_sticky(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_location.click()
    page.search_menu = "люстралюстралюстралюстралюстралюстралюстралюстралюстралюстралюстралюстралюстралюстралюстр" \
                       "алюстралю"
    page.search_button.click()

    assert page.result_search.get_text().find('люстралюстралюстралюстралюстралюстралюстралюстрал') != -1,\
        'Превышен лимит ввода максимального количества символов'

