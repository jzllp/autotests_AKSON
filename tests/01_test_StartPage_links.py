# How to run:
#  1) Download driver for Chrome:
#     https://chromedriver.chromium.org/downloads
#  2) Install all required python packages library
#
#  3) Run in terminal with line:
#     python -m pytest -v --driver Chrome --driver-path <~>/chromedriver.exe tests/01_tests_StartPage_links_01.py

from pages.akson_locators import Header_top, Header_sticky, Header_menu, Main_slider, Main_smarts_main, \
    Footer_content, Header_help


def test_StartPage_city_choice(web_browser):
    """ Проверка модуля выбора города блока header__top. """

    page = Header_top(web_browser)

    page.input_city.send_keys('Рыбинск')
    page.choice_my_city.click()

    assert page.city_choice.get_text() == 'Рыбинск', 'Не найден выбранный город'


def test_StartPage_contact_phone(web_browser):
    """ Проверка изменения контактного телефона при смене города блока header__top. """

    page = Header_top(web_browser)

    before = page.contact_phone.get_text()
    page.input_city.send_keys('Рыбинск')
    page.choice_my_city.click()
    after = page.contact_phone.get_text()

    assert before != after, 'Контактный номер не изменился'


def test_StartPage_contact_phone_active(web_browser):
    """ Проверка активации функции звонка блока header__top. """

    page = Header_top(web_browser)

    assert page.contact_phone.is_clickable(), 'Невозможно кликнуть на контактный номер телефона'


def test_StartPage_link_opt(web_browser):
    """ Проверка корректного пути ссылки "Оптовым клиентам" блока header__top. """

    page = Header_top(web_browser)

    page.opt_akson.click()

    assert page.newopt_general.find(), 'Неверный путь страницы "Оптовым клиентам"'


def test_StartPage_link_master(web_browser):
    """ Проверка корректного пути ссылки "Мастера" блока header__top. """

    page = Header_top(web_browser)

    page.master_akson.click()

    assert page.master_rating.find(), 'Неверный путь страницы "Мастера"'


def test_StartPage_link_bonus_program(web_browser):
    """ Проверка корректного пути ссылки "Бонусная программа" блока header__top. """

    page = Header_top(web_browser)

    page.bonus_program.click()

    assert page.promotion_rules.find(), 'Неверный путь страницы "Бонусная программа"'


def test_StartPage_link_help(web_browser):
    """ Проверка корректного пути ссылки "Помощь" блока header__top. """

    page = Header_top(web_browser)

    page.help.click()

    assert page.to_help.find(), 'Неверный путь страницы "Помощь"'


def test_StartPage_link_payment(web_browser):
    """ Проверка корректного пути ссылки "Оплата" блока "Помощь". """

    page = Header_top(web_browser)
    page_hl = Header_help(web_browser)

    page.help.right_mouse_click()
    page_hl.payment.click()
    assert page_hl.how_to_pay.find(), 'Неверный путь страницы "Оплата"'


def test_StartPage_link_delivery(web_browser):
    """ Проверка корректного пути ссылки "Доставка" блока "Помощь". """

    page = Header_top(web_browser)
    page_hl = Header_help(web_browser)

    page.help.right_mouse_click()
    page_hl.delivery.click()
    assert page_hl.hl_delivery.find(), 'Неверный путь страницы "Доставка"'


def test_StartPage_link_services(web_browser):
    """ Проверка корректного пути ссылки "Услуги" блока "Помощь". """

    page = Header_top(web_browser)
    page_hl = Header_help(web_browser)

    page.help.right_mouse_click()
    page_hl.services.click()
    assert page_hl.hl_services.find(), 'Неверный путь страницы "Услуги"'


def test_StartPage_link_return_pr(web_browser):
    """ Проверка корректного пути ссылки "Возврат товара" блока "Помощь". """

    page = Header_top(web_browser)
    page_hl = Header_help(web_browser)

    page.help.right_mouse_click()
    page_hl.return_pr.click()
    assert page_hl.hl_return.find(), 'Неверный путь страницы "Возврат товара"'


def test_StartPage_link_bonus(web_browser):
    """ Проверка корректного пути ссылки "Бонусная программа" блока "Помощь". """

    page = Header_top(web_browser)
    page_hl = Header_help(web_browser)

    page.help.right_mouse_click()
    page_hl.bonus.click()
    assert page.promotion_rules.find(), 'Неверный путь страницы "Бонусная программа"'


def test_StartPage_link_weekend_discount(web_browser):
    """ Проверка корректного пути ссылки "Скидка выходного дня" блока "Помощь". """

    page = Header_top(web_browser)
    page_hl = Header_help(web_browser)

    page.help.right_mouse_click()
    page_hl.weekend_discount.click()
    assert page_hl.hl_weekend_discount.find(), 'Неверный путь страницы "Скидка выходного дня"'


def test_StartPage_link_logo(web_browser):
    """ Проверка корректного пути ссылки на стартовую страницу блока header__sticky. """

    page = Header_top(web_browser)
    page_home = Header_sticky(web_browser)

    page.help.click()
    page_home.logo.click()
    page.wait_page_loaded()

    assert page.get_current_url() == 'https://akson.ru/', 'Неверный путь стартовой страницы'


def test_StartPage_link_catalog(web_browser):
    """ Проверка активации меню каталога блока header__sticky. """

    page = Header_sticky(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.catalog.click()
    page.wait_page_loaded()

    assert page.catalog_menu.is_visible(), 'Меню каталога не активировалось'


def test_StartPage_search_menu(web_browser):
    """ Проверка активации меню поиска блока header__sticky. """

    page = Header_sticky(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.search_menu = "люстра"
    page.search_button.click()

    assert page.result_search.get_text()[30:] == "люстра", 'Меню поиска не активировалось'


def test_StartPage_link_profile(web_browser):
    """ Проверка корректного пути ссылки "Авторизации профиля" блока header__sticky. """

    page = Header_sticky(web_browser)

    page.profile.click()

    assert page.authorization.find(), 'Неверный путь страницы авторизации'


def test_StartPage_link_cart(web_browser):
    """ Проверка корректного пути ссылки "Корзина" блока header__sticky. """

    page = Header_sticky(web_browser)

    page.cart.click()

    assert page.my_cart.find(), 'Неверный путь страницы "корзина"'


def test_StartPage_link_stock(web_browser):
    """ Проверка корректного пути ссылки "Акции" блока header_menu. """

    page = Header_menu(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.stock.click()
    page.wait_page_loaded()

    assert page.get_current_url() == 'https://akson.ru/stock/', 'Неверный путь страницы "Акции"'


def test_StartPage_link_ready_made_solutions(web_browser):
    """ Проверка корректного пути ссылки "Готовые решения" блока header_menu. """

    page = Header_menu(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.ready_made.click()
    page.wait_page_loaded()

    assert page.get_current_url() == 'https://akson.ru/ready_made_solutions/', 'Неверный путь страницы ' \
                                                                               '"Готовые решения"'


def test_StartPage_link_construction(web_browser):
    """ Проверка корректного пути ссылки "Строительные материалы" блока header_menu. """

    page = Header_menu(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.construction.click()
    page.wait_page_loaded()

    assert page.get_current_url() == 'https://akson.ru/c/stroitelnye_materialy/', 'Неверный путь страницы ' \
                                                                                  '"Строительные материалы"'


def test_StartPage_link_tile(web_browser):
    """ Проверка корректного пути ссылки "Керамическая плитка" блока header_menu. """

    page = Header_menu(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.tile.click()
    page.wait_page_loaded()

    assert page.get_current_url() == 'https://akson.ru/c/keramicheskaya_plitka/', 'Неверный путь страницы ' \
                                                                                  '"Керамическая плитка"'


def test_StartPage_link_paints(web_browser):
    """ Проверка корректного пути ссылки "Краски" блока header_menu. """

    page = Header_menu(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.paints.click()
    page.wait_page_loaded()

    assert page.get_current_url() == 'https://akson.ru/c/kraski/', 'Неверный путь страницы "Краски"'


def test_StartPage_link_plumbing(web_browser):
    """ Проверка корректного пути ссылки "Сантехника" блока header_menu. """

    page = Header_menu(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.plumbing.click()
    page.wait_page_loaded()

    assert page.get_current_url() == 'https://akson.ru/c/santehnika/', 'Неверный путь страницы "Сантехника"'


def test_StartPage_link_laminate(web_browser):
    """ Проверка корректного пути ссылки "Напольные покрытия" блока header_menu. """

    page = Header_menu(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.laminate.click()
    page.wait_page_loaded()

    assert page.get_current_url() == 'https://akson.ru/c/napolnye_pokrytiya/', 'Неверный путь страницы ' \
                                                                               '"Напольные покрытия"'


def test_StartPage_link_household_products(web_browser):
    """ Проверка корректного пути ссылки "Товары для дома" блока header_menu. """

    page = Header_menu(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.household_products.click()
    page.wait_page_loaded()

    assert page.get_current_url() == 'https://akson.ru/c/tovary_dlya_doma/', 'Неверный путь страницы "Товары для дома"'


def test_StartPage_link_windows(web_browser):
    """ Проверка корректного пути ссылки "Окна" блока main-slider. """

    page = Main_slider(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.windows.click()

    assert page.windows_constructor.find(), 'Неверный путь страницы "Окна"'


def test_StartPage_link_ready_made_banner(web_browser):
    """ Проверка корректного пути ссылки "Готовые решения" блока main-slider. """

    page = Main_slider(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.ready_made.click()
    page.wait_page_loaded()

    assert page.my_ready_made.find(), 'Неверный путь страницы "Готовые решения"'


def test_StartPage_link_opt_akson_banner(web_browser):
    """ Проверка корректного пути ссылки "Оптовым клиентам" блока main-slider. """

    page = Main_slider(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.wait_page_loaded()

    assert page.opt_akson.is_visible(), 'Банер "Оптовым клиентам" не виден'
    assert page.opt_akson.is_clickable(), 'Невозможно нажать на банер "Оптовым клиентам"'


def test_StartPage_link_window(web_browser):
    """ Проверка корректного пути ссылки "Окна" блока main_smarts_main. """

    page = Main_slider(web_browser)
    page_city = Header_top(web_browser)
    page_main_smarts = Main_smarts_main(web_browser)

    page_city.choice_my_msk.click()
    page_main_smarts.window.click()

    assert page.windows_constructor.find(), 'Неверный путь страницы "Окна"'


def test_StartPage_link_furniture_details(web_browser):
    """ Проверка корректного пути ссылки "Детали мебели" блока main_smarts_main. """

    page = Main_smarts_main(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.furniture_details.click()

    assert page.furniture_designer.find(), 'Неверный путь страницы "Детали мебели"'


def test_StartPage_link_modular_cabinets(web_browser):
    """ Проверка корректного пути ссылки "Модульные шкафы" блока main_smarts_main. """

    page = Main_smarts_main(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.modular_cabinets.click()

    assert page.cabinet_constructor.find(), 'Неверный путь страницы "Модульные шкафы"'


def test_StartPage_link_cuisine(web_browser):
    """ Проверка корректного пути ссылки "Кухни" блока main_smarts_main. """

    page = Main_smarts_main(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.cuisine.click()

    assert page.kitchen_constructor.find(), 'Неверный путь страницы "Кухни"'


def test_StartPage_link_curtains(web_browser):
    """ Проверка корректного пути ссылки "Шторы" блока main_smarts_main. """

    page = Main_smarts_main(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.curtains.click()

    assert page.curtain_designer.find(), 'Неверный путь страницы "Шторы"'


def test_StartPage_link_facades(web_browser):
    """ Проверка корректного пути ссылки "Фасады" блока main_smarts_main. """

    page = Main_smarts_main(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.facades.click()

    assert page.facade_constructor.find(), 'Неверный путь страницы "Фасады"'


def test_StartPage_link_countertops(web_browser):
    """ Проверка корректного пути ссылки "Столешницы" блока main_smarts_main. """

    page = Main_smarts_main(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.countertops.click()

    assert page.countertop_designer.find(), 'Неверный путь страницы "Столешницы"'


def test_StartPage_link_kitchen_cabinets(web_browser):
    """ Проверка корректного пути ссылки "Кухонные шкафы" блока main_smarts_main. """

    page = Main_smarts_main(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.kitchen_cabinets.click()

    assert page.kitchen_cabinet_designer.find(), 'Неверный путь страницы "Кухонные шкафы"'


def test_StartPage_link_mirrors(web_browser):
    """ Проверка корректного пути ссылки "Зеркала" блока main_smarts_main. """

    page = Main_smarts_main(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.mirrors.click()

    assert page.mirror_constructor.find(), 'Неверный путь страницы "Зеркала"'


def test_StartPage_link_glass(web_browser):
    """ Проверка корректного пути ссылки "Стекла" блока main_smarts_main. """

    page = Main_smarts_main(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.glass.click()

    assert page.glass_constructor.find(), 'Неверный путь страницы "Стекла"'


def test_StartPage_link_posters(web_browser):
    """ Проверка корректного пути ссылки "Постеры" блока main_smarts_main. """

    page = Main_smarts_main(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.posters.click()

    assert page.poster_designer.find(), 'Неверный путь страницы "Постеры"'


def test_StartPage_link_roller_blinds(web_browser):
    """ Проверка корректного пути ссылки "Рулонные шторы" блока main_smarts_main. """

    page = Main_smarts_main(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.roller_blinds.click()

    assert page.roller_blind_designer.find(), 'Неверный путь страницы "Рулонные шторы"'


def test_StartPage_link_aluminum_windows(web_browser):
    """ Проверка корректного пути ссылки "Окна алюминий" блока main_smarts_main. """

    page = Main_smarts_main(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()

    assert page.aluminum_windows.is_visible(), 'Неверный путь страницы "Окна алюминий"'


def test_StartPage_link_wallpaper(web_browser):
    """ Проверка корректного пути ссылки "Обои" блока main_smarts_main. """

    page = Main_smarts_main(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.wallpaper.click()

    assert page.designer_wallpaper.find(), 'Неверный путь страницы "Обои"'


def test_StartPage_link_kitchen_corner(web_browser):
    """ Проверка корректного пути ссылки "Кухонные уголки" блока main_smarts_main. """

    page = Main_smarts_main(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.kitchen_corner.click()

    assert page.kitchen_corner_designer.find(), 'Неверный путь страницы "Кухонные уголки"'


def test_StartPage_link_color_paint(web_browser):
    """ Проверка корректного пути ссылки "Колеровка краски" блока main_smarts_main. """

    page = Main_smarts_main(web_browser)
    page_city = Header_top(web_browser)

    page_city.choice_my_msk.click()
    page.color_paint.click()

    assert page.paint_tinting_designer.find(), 'Неверный путь страницы "Колеровка краски"'


def test_StartPage_link_contact_phone(web_browser):
    """ Проверка корректного пути ссылки "Контактный телефон" блока footer__content. """

    page = Footer_content(web_browser)

    page.contact_phone.scroll_to_element()

    assert page.contact_phone.is_clickable(), 'Невозможно кликнуть на контактный номер телефона'


def test_StartPage_link_fc_help(web_browser):
    """ Проверка корректного пути ссылки "Вопросы и ответы" блока footer__content. """

    page = Footer_content(web_browser)

    page.fc_help.scroll_to_element()
    page.fc_help.click()

    assert page.help_block.find(), 'Неверный путь страницы "Вопросы и ответы"'


def test_StartPage_link_delivery_footer_content(web_browser):
    """ Проверка корректного пути ссылки "Доставка" блока footer__content. """

    page = Footer_content(web_browser)
    page_hl = Header_help(web_browser)

    page.fc_delivery.scroll_to_element()
    page.fc_delivery.click()

    assert page_hl.hl_delivery.find(), 'Неверный путь страницы "Доставка"'


def test_StartPage_link_fc_stock(web_browser):
    """ Проверка корректного пути ссылки "Акции" блока footer__content. """

    page = Footer_content(web_browser)

    page.fc_stock.scroll_to_element()
    page.fc_stock.click()

    assert page.get_current_url() == 'https://akson.ru/stock/', 'Неверный путь страницы "Акции"'


def test_StartPage_link_fc_payment(web_browser):
    """ Проверка корректного пути ссылки "Оплата" блока footer__content. """

    page = Footer_content(web_browser)
    page_hl = Header_help(web_browser)

    page.payment.scroll_to_element()
    page.payment.click()

    assert page_hl.how_to_pay.find(), 'Неверный путь страницы "Оплата"'


def test_StartPage_link_fc_services(web_browser):
    """ Проверка корректного пути ссылки "Услуги" блока footer__content. """

    page = Footer_content(web_browser)
    page_hl = Header_help(web_browser)

    page.services.scroll_to_element()
    page.services.click()

    assert page_hl.hl_services.find(), 'Неверный путь страницы "Услуги"'


def test_StartPage_link_fc_return(web_browser):
    """ Проверка корректного пути ссылки "Сервис и гарантия" блока footer__content. """

    page = Footer_content(web_browser)
    page_hl = Header_help(web_browser)

    page.fc_return.scroll_to_element()
    page.fc_return.click()

    assert page_hl.hl_return.find(), 'Неверный путь страницы "Сервис и гарантия"'


def test_StartPage_link_fc_suggestions(web_browser):
    """ Проверка корректного пути ссылки "Предложения" блока footer__content. """

    page = Footer_content(web_browser)

    page.fc_suggestions.scroll_to_element()
    page.fc_suggestions.click()

    assert page.complaints.find(), 'Неверный путь страницы "Предложения"'


def test_StartPage_link_fc_complaints(web_browser):
    """ Проверка корректного пути ссылки "Жалобы" блока footer__content. """

    page = Footer_content(web_browser)

    page.fc_complaints.scroll_to_element()
    page.fc_complaints.click()

    assert page.complaints.find(), 'Неверный путь страницы "Жалобы"'


def test_StartPage_link_fc_contacts_and_shops(web_browser):
    """ Проверка корректного пути ссылки "Контакты и магазины" блока footer__content. """

    page = Footer_content(web_browser)

    page.contacts_and_shops.scroll_to_element()
    page.contacts_and_shops.click()

    assert page.addresses_and_contacts.find(), 'Неверный путь страницы "Контакты и магазины"'


def test_StartPage_link_fc_bonus_program(web_browser):
    """ Проверка корректного пути ссылки "Бонусная программа" блока footer__content. """

    page = Footer_content(web_browser)
    page_top = Header_top(web_browser)

    page.fc_bonus_program.scroll_to_element()
    page.fc_bonus_program.click()

    assert page_top.promotion_rules.find(), 'Неверный путь страницы "Бонусная программа"'


def test_StartPage_link_fc_vacancy(web_browser):
    """ Проверка корректного пути ссылки "Вакансии" блока footer__content. """

    page = Footer_content(web_browser)

    page.fc_vacancy.scroll_to_element()
    page.fc_vacancy.click()

    assert page.job.find(), 'Неверный путь страницы "Вакансии"'


def test_StartPage_link_fc_about(web_browser):
    """ Проверка корректного пути ссылки "О компании" блока footer__content. """

    page = Footer_content(web_browser)

    page.fc_about.scroll_to_element()
    page.fc_about.click()

    assert page.regions.find(), 'Неверный путь страницы "О компании"'


def test_StartPage_link_fc_provider(web_browser):
    """ Проверка корректного пути ссылки "Поставщикам" блока footer__content. """

    page = Footer_content(web_browser)

    page.fc_provider.scroll_to_element()
    page.fc_provider.click()

    assert page.provider_form.find(), 'Неверный путь страницы "Поставщикам"'


def test_StartPage_link_fc_rent(web_browser):
    """ Проверка корректного пути ссылки "Аренда площадей" блока footer__content. """

    page = Footer_content(web_browser)

    page.fc_rent.scroll_to_element()

    assert page.fc_rent.is_clickable(), 'Невозможно нажать на ссылку "Аренда площадей"'

    page_rent = page.fc_rent.get_attribute('href')
    page.get(page_rent)

    assert page.btn_rent.find(), 'Неверный путь страницы "Поставщикам"'
