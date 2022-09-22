# How to run:
#  1) Download driver for Chrome:
#     https://chromedriver.chromium.org/downloads
#  2) Install all required python packages library
#
#  3) Run in terminal with line:
#     python -m pytest -v --driver Chrome --driver-path <~>/chromedriver.exe tests/05_test_Filter_and_sort.py


from pages.akson_locators import Header_sticky, Header_top, Categories_sections, Card_product


def test_categories_01(web_browser):
    """ Проверка фильтра по категориям товаров. """

    page = Header_sticky(web_browser)
    page_city = Header_top(web_browser)
    page_categories = Categories_sections(web_browser)

    page_city.choice_location.click()
    page.search_menu = "лестница"
    page.search_button.click()
    categories = page_categories.first_section.get_text()
    page_categories.first_section.click()

    assert categories == page_categories.category_name.get_text(), 'Названия категории не совпадают'

    page_categories.first_item.scroll_to_element()
    page_categories.first_item.click()

    assert categories == page_categories.root_category.get_text(), 'Название категории в карточке товара не совпадает'


def test_categories_02(web_browser):
    """ Проверка фильтра по категориям товаров. """

    page = Header_sticky(web_browser)
    page_city = Header_top(web_browser)
    page_categories = Categories_sections(web_browser)

    page_city.choice_location.click()
    page.search_menu = "лестница"
    page.search_button.click()
    page_categories.spoiler.click()
    categories = page_categories.last_section.get_text()
    page_categories.last_section.click()

    assert categories == page_categories.category_name.get_text(), 'Названия категории не совпадают'

    page_categories.first_item.scroll_to_element()
    page_categories.first_item.click()

    assert categories == page_categories.root_category.get_text(), 'Название категории в карточке товара не совпадает'


def test_categories_min_price_03(web_browser):
    """ Проверка фильтра по минимальной стоимости товара. """

    page = Header_sticky(web_browser)
    page_city = Header_top(web_browser)
    page_categories = Categories_sections(web_browser)

    page_city.choice_location.click()
    page.search_menu = "лестница"
    page.search_button.click()
    page_categories.min_price = '00'
    page_categories.max_price.click()
    page.wait_page_loaded()
    sort = page_categories.min_price_impl.get_text()
    sort_price = int(sort.replace('Цена (руб): ', ''))
    page.scroll_down()

    all_prices = page_categories.price_all.get_text()
    all_prices = [int(p.replace(' ', '')) for p in all_prices]

    price_bad = []
    for i in all_prices:
        if i < sort_price:
            price_bad.append(+1)

    assert price_bad == [], 'Фильтр по минимальной цене не сработал'


def test_categories_max_price_04(web_browser):
    """ Проверка фильтра по максимальной стоимости товара. """

    page = Header_sticky(web_browser)
    page_city = Header_top(web_browser)
    page_categories = Categories_sections(web_browser)

    page_city.choice_location.click()
    page.search_menu = "лестница"
    page.search_button.click()
    page_categories.max_price.click()
    page_categories.max_price.send_keys('\ue003')
    page_categories.min_price.click()
    page.wait_page_loaded()

    sort = page_categories.min_price_impl.get_text()
    sort_price = int(sort.replace('Цена (руб): ', ''))
    page.scroll_down()

    all_prices = page_categories.price_all.get_text()
    all_prices = [int(p.replace(' ', '')) for p in all_prices]

    price_bad = []
    for i in all_prices:
        if i > sort_price:
            price_bad.append(+1)

    assert price_bad == [], 'Фильтр по максимальной цене не сработал'


def test_categories_brand_first_05(web_browser):
    """ Проверка фильтра по категории 'бренд'. """

    page = Header_sticky(web_browser)
    page_city = Header_top(web_browser)
    page_categories = Categories_sections(web_browser)
    page_card = Card_product(web_browser)

    page_city.choice_location.click()
    page.search_menu = "лестница"
    page.search_button.click()
    brand_cat = page_categories.brand_first.get_text()
    page_categories.brand_first.click()
    page.wait_page_loaded()
    page_categories.first_item.click()
    page.wait_page_loaded()
    page_card.brand.scroll_to_element()

    assert brand_cat == page_card.brand.get_text(), 'Название бренда не совпадает'


def test_categories_country_06(web_browser):
    """ Проверка фильтра по категории 'страна'. """

    page = Header_sticky(web_browser)
    page_city = Header_top(web_browser)
    page_categories = Categories_sections(web_browser)
    page_card = Card_product(web_browser)

    page_city.choice_location.click()
    page.search_menu = "лестница"
    page.search_button.click()
    page.wait_page_loaded()
    page_categories.country_first.scroll_to_element()
    country_cat = page_categories.country_first.get_text()
    page_categories.country_first.scroll_to_element()
    page_categories.country_first.click()
    page.wait_page_loaded()
    page_categories.first_item.click()
    page_card.country.scroll_to_element()

    assert country_cat == page_card.country.get_text(), 'Название страны не совпадает'


def test_categories_sort_by_price_min_7(web_browser):
    """ Проверка сортировки цены от минимума к максимуму. """

    page = Header_sticky(web_browser)
    page_city = Header_top(web_browser)
    page_categories = Categories_sections(web_browser)

    page_city.choice_location.click()
    page.search_menu = "лестница"
    page.search_button.click()
    page_categories.first_section.click()
    page_categories.sort_by_price.click()
    page.wait_page_loaded()

    assert page_categories.min_price_by_price.get_text() == page_categories.sort_min_price.get_text(), \
        'Сортировка от минимальной цены не сработала'


def test_categories_sort_by_price_max_8(web_browser):
    """ Проверка сортировки цены от максимума к минимуму. """

    page = Header_sticky(web_browser)
    page_city = Header_top(web_browser)
    page_categories = Categories_sections(web_browser)

    page_city.choice_location.click()
    page.search_menu = "лестница"
    page.search_button.click()
    page_categories.first_section.click()
    page_categories.sort_by_price.click()
    page_categories.sort_by_price_act.click()
    page.wait_page_loaded()

    assert page_categories.max_price_by_price.get_text() == page_categories.sort_max_price.get_text().replace(' ', ''),\
        'Сортировка от максимальной цены не сработала'
