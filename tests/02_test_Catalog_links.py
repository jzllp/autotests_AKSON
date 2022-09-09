# How to run:
#  1) Download driver for Chrome:
#     https://chromedriver.chromium.org/downloads
#  2) Install all required python packages library
#
#  3) Run in terminal with line:
#     python -m pytest -v --driver Chrome --driver-path <~>/chromedriver.exe tests/02_test_Catalog_links.py

from pages.akson_locators import Header_sticky, Catalog_links, Header_top, Main_slider


def test_Catalog_link_do_it(web_browser):
    """ Проверка ссылки каталога "Сделай сам". """

    page = Header_sticky(web_browser)
    page_ctl = Catalog_links(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.catalog.click()

    assert page_ctl.do_it.find(), 'Неверный путь раздела "Сделай сам"'


def test_Catalog_link_turnkey_solutions(web_browser):
    """ Проверка ссылки каталога "Готовые решения". """

    page = Header_sticky(web_browser)
    page_ctl = Catalog_links(web_browser)
    page_city = Header_top(web_browser)
    page_ms = Main_slider(web_browser)

    page_city.choice_my_msk.click()
    page.catalog.click()
    page_ctl.turnkey_solutions.click()

    assert page_ms.my_ready_made.find(), 'Неверный путь раздела "Готовые решения"'


def test_Catalog_link_construction_materials(web_browser):
    """ Проверка ссылки каталога "Строительные материалы". """

    page = Header_sticky(web_browser)
    page_ctl = Catalog_links(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.catalog.click()
    page_ctl.construction_materials.click()

    assert page_ctl.ctl_construction_materials.find(), 'Неверный путь раздела "Строительные материалы"'


def test_Catalog_link_lumber(web_browser):
    """ Проверка ссылки каталога "Пиломатериалы". """

    page = Header_sticky(web_browser)
    page_ctl = Catalog_links(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.catalog.click()
    page_ctl.lumber.click()

    assert page_ctl.ctl_lumber.find(), 'Неверный путь раздела "Пиломатериалы"'


def test_Catalog_water_supply(web_browser):
    """ Проверка ссылки каталога "Водоснабжение". """

    page = Header_sticky(web_browser)
    page_ctl = Catalog_links(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.catalog.click()
    page_ctl.water_supply.click()

    assert page_ctl.ctl_water_supply.find(), 'Неверный путь раздела "Водоснабжение"'


def test_Catalog_ventilation(web_browser):
    """ Проверка ссылки каталога "Вентиляция". """

    page = Header_sticky(web_browser)
    page_ctl = Catalog_links(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.catalog.click()
    page_ctl.ventilation.click()

    assert page_ctl.ctl_ventilation.find(), 'Неверный путь раздела "Вентиляция"'


def test_Catalog_electrical(web_browser):
    """ Проверка ссылки каталога "Электротовары". """

    page = Header_sticky(web_browser)
    page_ctl = Catalog_links(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.catalog.click()
    page_ctl.electrical.click()

    assert page_ctl.ctl_electrical.find(), 'Неверный путь раздела "Электротовары"'


def test_Catalog_hardware(web_browser):
    """ Проверка ссылки каталога "Скобяные изделия". """

    page = Header_sticky(web_browser)
    page_ctl = Catalog_links(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.catalog.click()
    page_ctl.hardware.click()

    assert page_ctl.ctl_hardware.find(), 'Неверный путь раздела "Скобяные изделия"'


def test_Catalog_ceramic_tile(web_browser):
    """ Проверка ссылки каталога "Керамическая плитка". """

    page = Header_sticky(web_browser)
    page_ctl = Catalog_links(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.catalog.click()
    page_ctl.ceramic_tile.click()

    assert page_ctl.ctl_ceramic_tile.find(), 'Неверный путь раздела "Керамическая плитка"'


def test_Catalog_paints(web_browser):
    """ Проверка ссылки каталога "Краски". """

    page = Header_sticky(web_browser)
    page_ctl = Catalog_links(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.catalog.click()
    page_ctl.paints.click()

    assert page_ctl.ctl_paints.find(), 'Неверный путь раздела "Краски"'


def test_Catalog_tools(web_browser):
    """ Проверка ссылки каталога "Инструменты для ремонта и строительства". """

    page = Header_sticky(web_browser)
    page_ctl = Catalog_links(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.catalog.click()
    page_ctl.tools.click()

    assert page_ctl.ctl_tools.find(), 'Неверный путь раздела "Инструменты для ремонта и строительства"'


def test_Catalog_plumbing(web_browser):
    """ Проверка ссылки каталога "Сантехника". """

    page = Header_sticky(web_browser)
    page_ctl = Catalog_links(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.catalog.click()
    page_ctl.plumbing.click()

    assert page_ctl.ctl_plumbing.find(), 'Неверный путь раздела "Сантехника"'


def test_Catalog_decoration(web_browser):
    """ Проверка ссылки каталога "Отделка стен и потолков". """

    page = Header_sticky(web_browser)
    page_ctl = Catalog_links(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.catalog.click()
    page_ctl.decoration.click()

    assert page_ctl.ctl_decoration.find(), 'Неверный путь раздела "Отделка стен и потолков"'


def test_Catalog_wallpaper(web_browser):
    """ Проверка ссылки каталога "Обои". """

    page = Header_sticky(web_browser)
    page_ctl = Catalog_links(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.catalog.click()
    page_ctl.wallpaper.click()

    assert page_ctl.ctl_wallpaper.find(), 'Неверный путь раздела "Обои"'


def test_Catalog_floor_covering(web_browser):
    """ Проверка ссылки каталога "Напольные покрытия". """

    page = Header_sticky(web_browser)
    page_ctl = Catalog_links(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.catalog.click()
    page_ctl.floor_coverings.click()

    assert page_ctl.ctl_floor_coverings.find(), 'Неверный путь раздела "Напольные покрытия"'


def test_Catalog_doors(web_browser):
    """ Проверка ссылки каталога "Двери". """

    page = Header_sticky(web_browser)
    page_ctl = Catalog_links(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.catalog.click()
    page_ctl.doors.scroll_to_element()
    page_ctl.doors.click()

    assert page_ctl.ctl_doors.find(), 'Неверный путь раздела "Двери"'


def test_Catalog_windows(web_browser):
    """ Проверка ссылки каталога "Окна". """

    page = Header_sticky(web_browser)
    page_ctl = Catalog_links(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.catalog.click()
    page_ctl.windows.scroll_to_element()
    page_ctl.windows.click()

    assert page_ctl.ctl_windows.find(), 'Неверный путь раздела "Окна"'


def test_Catalog_storage_systems(web_browser):
    """ Проверка ссылки каталога "Системы хранения". """

    page = Header_sticky(web_browser)
    page_ctl = Catalog_links(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.catalog.click()
    page_ctl.storage_systems.scroll_to_element()
    page_ctl.storage_systems.click()

    assert page_ctl.ctl_storage_systems.find(), 'Неверный путь раздела "Системы хранения"'


def test_Catalog_lighting(web_browser):
    """ Проверка ссылки каталога "Освещение". """

    page = Header_sticky(web_browser)
    page_ctl = Catalog_links(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.catalog.click()
    page_ctl.lighting.scroll_to_element()
    page_ctl.lighting.click()

    assert page_ctl.ctl_lighting.find(), 'Неверный путь раздела "Освещение"'


def test_Catalog_furniture(web_browser):
    """ Проверка ссылки каталога "Мебель". """

    page = Header_sticky(web_browser)
    page_ctl = Catalog_links(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.catalog.click()
    page_ctl.furniture.scroll_to_element()
    page_ctl.furniture.click()

    assert page_ctl.ctl_furniture.find(), 'Неверный путь раздела "Мебель"'


def test_Catalog_decor(web_browser):
    """ Проверка ссылки каталога "Интерьер и декор". """

    page = Header_sticky(web_browser)
    page_ctl = Catalog_links(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.catalog.click()
    page_ctl.decor.scroll_to_element()
    page_ctl.decor.click()

    assert page_ctl.ctl_decor.find(), 'Неверный путь раздела "Интерьер и декор"'


def test_Catalog_appliances(web_browser):
    """ Проверка ссылки каталога "Бытовая техника". """

    page = Header_sticky(web_browser)
    page_ctl = Catalog_links(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.catalog.click()
    page_ctl.appliances.scroll_to_element()
    page_ctl.appliances.click()

    assert page_ctl.ctl_appliances.find(), 'Неверный путь раздела "Бытовая техника"'


def test_Catalog_auto_products(web_browser):
    """ Проверка ссылки каталога "Автотовары". """

    page = Header_sticky(web_browser)
    page_ctl = Catalog_links(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.catalog.click()
    page_ctl.auto_products.scroll_to_element()
    page_ctl.auto_products.click()

    assert page_ctl.ctl_auto_products.find(), 'Неверный путь раздела "Автотовары"'


def test_Catalog_hobby(web_browser):
    """ Проверка ссылки каталога "Товары для отдыха и хобби". """

    page = Header_sticky(web_browser)
    page_ctl = Catalog_links(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.catalog.click()
    page_ctl.hobby.scroll_to_element()
    page_ctl.hobby.click()

    assert page_ctl.ctl_hobby.find(), 'Неверный путь раздела "Товары для отдыха и хобби"'


def test_Catalog_household_products(web_browser):
    """ Проверка ссылки каталога "Товары для дома". """

    page = Header_sticky(web_browser)
    page_ctl = Catalog_links(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.catalog.click()
    page_ctl.household_products.scroll_to_element()
    page_ctl.household_products.click()

    assert page_ctl.ctl_household_products.find(), 'Неверный путь раздела "Товары для дома"'


def test_Catalog_tableware(web_browser):
    """ Проверка ссылки каталога "Посуда". """

    page = Header_sticky(web_browser)
    page_ctl = Catalog_links(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.catalog.click()
    page_ctl.tableware.scroll_to_element()
    page_ctl.tableware.click()

    assert page_ctl.ctl_tableware.find(), 'Неверный путь раздела "Посуда"'


def test_Catalog_garden_supplies(web_browser):
    """ Проверка ссылки каталога "Товары для сада". """

    page = Header_sticky(web_browser)
    page_ctl = Catalog_links(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.catalog.click()
    page_ctl.garden_supplies.scroll_to_element()
    page_ctl.garden_supplies.click()

    assert page_ctl.ctl_garden_supplies.find(), 'Неверный путь раздела "Товары для сада"'


def test_Catalog_smart_house(web_browser):
    """ Проверка ссылки каталога "Умный дом". """

    page = Header_sticky(web_browser)
    page_ctl = Catalog_links(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.catalog.click()
    page_ctl.smart_house.scroll_to_element()
    page_ctl.smart_house.click()

    assert page_ctl.ctl_smart_house.find(), 'Неверный путь раздела "Умный дом"'
