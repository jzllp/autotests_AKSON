import os
from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class StartPage(WebPage):
    """ Базовый класс стартовой страницы Akson. """

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://akson.ru/'

        super().__init__(web_driver, url)


class Header_top(StartPage):
    """ Локаторы стартовой страницы блока header__top. """

    # Выбор города
    city_choice = WebElement(xpath='//span[@class="top-bar__city-choice-text"]')

    # Меню ввода города
    input_city = WebElement(xpath='//input[ @class="city-choice__search-input ui-text-medium"]')

    # Выбор искомого города
    choice_my_city = WebElement(xpath='//p[@class="city-choice__city ui-text-small ui-pb-2"]')

    # Выбор города Москва
    choice_my_msk = WebElement(xpath='//p[@class="city-choice__city ui-text-small ui-pb-2" and contains(text(),'
                                     ' "Москва")]')

    # Выбор города по автолокации
    choice_location = WebElement(xpath='//p[@class="city-choice__city ui-text-small ui-pb-2 city-choice__city_active"]')

    # Контактный телефон
    contact_phone = WebElement(xpath='//a[@class="top-bar__contact-phone"]')

    # Ссылка "Оптовым клиентам"
    opt_akson = WebElement(xpath='//a[@href="https://opt.akson.ru"]')

    # Меню авторизации на странице "Оптовым клиентам"
    newopt_general = WebElement(xpath='//div[@class ="newopt-general"]')

    # Ссылка "Мастера"
    master_akson = WebElement(xpath='//a[contains(text(), "Мастера")]')

    # Раздел "Рейтинг мастеров" на страницe "Мастера"
    master_rating = WebElement(xpath='//div[@class="main__title" and contains(text(), "Рейтинг мастеров")]')

    # Раздел "Бонусная программа"
    bonus_program = WebElement(xpath='//a[@href="/bonus-program/" and @class="top-bar__item-text"]')

    # Раздел "Бонусная программа" на странице "Бонусная программа"
    promotion_rules = WebElement(xpath='//div[@class="bonus-program"]')

    # Ссылка "Помощь"
    help = WebElement(xpath='//a[@href="/help/" and @class="top-bar__item-text"]')

    # Раздел "Помощь" на странице "Помощь"
    to_help = WebElement(xpath='//h1[@class="wrapper__hl" and contains(text(), "Помощь")]')


class Header_help(StartPage):
    """ Локаторы стартовой страницы блока "Помощь". """

    # Ссылка "Оплата"
    payment = WebElement(xpath='//a[@href="/help/how-to-pay/"]')

    # Раздел "Как платить" на странице "Оплата"
    how_to_pay = WebElement(xpath='//h1[@class="wrapper__hl" and contains(text(), "Как оплатить")]')

    # Ссылка "Доставка"
    delivery = WebElement(xpath='//a[@href="/help/delivery/"]')

    # Раздел "Доставка" на странице "Доставка"
    hl_delivery = WebElement(xpath='//h1[@class="wrapper__hl" and contains(text(), "Доставка")]')

    # Ссылка "Услуги"
    services = WebElement(xpath='//a[@href="/help/services/"]')

    # Раздел "Услуги" на странице "Услуги"
    hl_services = WebElement(xpath='//h1[@class="wrapper__hl" and contains(text(), "Услуги")]')

    # Ссылка "Возврат товара"
    return_pr = WebElement(xpath='//a[@href="/help/purchase-return/"]')

    # Раздел "Возврат товара" на странице "Возврат товара"
    hl_return = WebElement(xpath='//h1[@class="wrapper__hl" and contains(text(), "Возврат товара")]')

    # Ссылка "Бонусная программа"
    bonus = WebElement(xpath='//a[@href="/bonus-program/"]')

    # Ссылка "Скидка выходного дня"
    weekend_discount = WebElement(xpath='//a[@href="/help/promotion_weekend_cashback/"]')

    # Раздел "Календарь акций" на странице "Скидка выходного дня"
    hl_weekend_discount = WebElement(xpath='//h1[@class="cashback-weekend__title ui-h1" and contains(text(),'
                                           ' "Календарь акции")]')


class Header_sticky(StartPage):
    """ Локаторы стартовой страницы блока header__sticky. """

    # Ссылка стартовой страницы
    logo = WebElement(xpath='//div[@class="logo"]')

    # Ссылка "Каталог"
    catalog = WebElement(xpath='//div[@class="header__top-menu"]')

    # Меню каталога
    catalog_menu = WebElement(xpath='//div[@class="categories__root-list"]')

    # Меню поиска
    search_menu = WebElement(xpath='//input[@name="q"]')

    # Кнопка поиска
    search_button = WebElement(xpath='//button[@class="search__button-find search__button-find_focused"]')

    # Результат поиска в заголовке
    result_search = WebElement(xpath='//h1[@class="search__h1"]')

    # Название первого товара в результате поиска
    result_product = WebElement(xpath='//div[@class="product-matrix__info info"]/a/span')

    # Таблица результата поиска со всеми товарами
    result_all_goods = WebElement(xpath='//div[@class="goods-list__content"]')

    # Ссылка на меню авторизации
    profile = WebElement(xpath='//a[@href="/auth/"]')

    # Меню авторизации
    authorization = WebElement(xpath='//div[@class="form form_active"]')

    # Ссылка на страницу "Корзина"
    cart = WebElement(xpath='//div[@class="header__actions-right-wrapper"]')

    # Раздел "Корзина" на страницы "Корзина"
    my_cart = WebElement(xpath='//p[@class="ui-h1"]')


class Header_menu(StartPage):
    """ Локаторы стартовой страницы блока header_menu. """

    # Ссылка на страницу "Акции"
    stock = WebElement(xpath='//a[@href="/stock/"]')

    # Ссылка на страницу "Готовые решения"
    ready_made = WebElement(xpath='//a[@href="/ready_made_solutions/"]')

    # Ссылка на страницу "Строительные материалы"
    construction = WebElement(xpath='//a[@href="/c/stroitelnye_materialy/"]')

    # Ссылка на страницу "Керамическая плитка"
    tile = WebElement(xpath='//a[@href="/c/keramicheskaya_plitka/"]')

    # Ссылка на страницу "Краски"
    paints = WebElement(xpath='//a[@href="/c/kraski/"]')

    # Ссылка на страницу "Сантехника"
    plumbing = WebElement(xpath='//a[@href="/c/santehnika/"]')

    # Ссылка на страницу "Напольные покрытия"
    laminate = WebElement(xpath='//a[@href="/c/napolnye_pokrytiya/"]')

    # Ссылка на страницу "Товары для дома"
    household_products = WebElement(xpath='//a[@href="/c/tovary_dlya_doma/"]')


class Main_slider(StartPage):
    """ Локаторы стартовой страницы блока main-slider. """

    # Ссылка на страницу "Окна"
    windows = WebElement(xpath='//div[2]/a/div[@class="image-box main-slider__main-img"]')

    # Конструктор окон на странице "Окна"
    windows_constructor = WebElement(xpath='//h1[@class="constructor__title" and contains(text(), '
                                           '"Изготовление окон по индивидуальным размерам")]')

    # Ссылка на страницу "Готовые решения"
    ready_made = WebElement(xpath='//a[@href="/ready_made_solutions/" and @class="main-slider__link"]')

    # Фильтр проектов на странице "Готовые решения"
    my_ready_made = WebElement(xpath='//div[@class="projects__options"]')

    # Ссылка на страницу "Оптовым клиентам"
    opt_akson = WebElement(xpath='//a[@href="https://opt.akson.ru/"]')


class Main_smarts_main(StartPage):
    """ Локаторы стартовой страницы блока main_smarts_main. """

    # Ссылка на страницу "Окна"
    window = WebElement(xpath='//a[@href="/window/"]')

    # Ссылка на страницу "Детали мебели"
    furniture_details = WebElement(xpath='//a[@href="/ldsp/"]')

    # Конструктор мебели на странице "Детали мебели"
    furniture_designer = WebElement(xpath='//h1[@class="constructor__title" and contains(text(), '
                                          '"Детали мебельные по индивидуальным размерам")]')

    # Ссылка на страницу "Модульные шкафы"
    modular_cabinets = WebElement(xpath='//a[@href="/modular_cabinet/"]')

    # Конструктор шкафов на странице "Модульные шкафы"
    cabinet_constructor = WebElement(xpath='//h1[@class="title mb-3" and contains(text(),'
                                           ' "Конструктор модульных шкафов")]')

    # Ссылка на страницу "Кухни"
    cuisine = WebElement(xpath='//a[@href="/kitchen/"]')

    # Конструктор кухни на странице "Кухни"
    kitchen_constructor = WebElement(xpath='//div[@class="title mb-3" and contains(text(), "Конструктор кухни")]')

    # Ссылка на страницу "Шторы"
    curtains = WebElement(xpath='//a[@href="/curtains/"]')

    # Конструктор шторы на странице "Шторы"
    curtain_designer = WebElement(xpath='//h1[@class="constructor__title" and contains(text(), '
                                        '"Шторы по индивидуальным размерам")]')

    # Ссылка на страницу "Фасады"
    facades = WebElement(xpath='//a[@href="/facade/"]')

    # Конструктор фасады на странице "Фасады"
    facade_constructor = WebElement(xpath='//h1[@class="constructor__title" and contains(text(), "Фасады")]')

    # Ссылка на страницу "Столешницы"
    countertops = WebElement(xpath='//a[@href="/tabletop/"]')

    # Конструктор столешниц на странице "Столешницы"
    countertop_designer = WebElement(xpath='//h1[@class="constructor__title" and contains(text(), '
                                           '"Столешницы по индивидуальным размерам")]')

    # Ссылка на страницу "Кухонные шкафы"
    kitchen_cabinets = WebElement(xpath='//a[@href="/body/"]')

    # Конструктор кухонных шкафов на странице "Кухонные шкафы"
    kitchen_cabinet_designer = WebElement(xpath='//h1[@class="constructor__title" and contains(text(), '
                                                '"Кухонные шкафы")]')

    # Ссылка на страницу "Зеркала"
    mirrors = WebElement(xpath='//a[@href="/mirrors/"]')

    # Конструктор зеркал на странице "Зеркала"
    mirror_constructor = WebElement(xpath='//h1[@class="constructor__title" and contains(text(), '
                                          '"Зеркала по индивидуальным размерам")]')

    # Ссылка на страницу "Стекла"
    glass = WebElement(xpath='//a[@href="/glass/"]')

    # Конструктор стекол на странице "Стекла"
    glass_constructor = WebElement(xpath='//h1[@class="constructor__title" and contains(text(), '
                                         '"Стекла по индивидуальным размерам")]')

    # Ссылка на страницу "Постеры"
    posters = WebElement(xpath='//a[@href="/posters/"]')

    # Конструктор постеров на странице "Постеры"
    poster_designer = WebElement(xpath='//h1[@class="constructor__title" and contains(text(), "Постер на заказ")]')

    # Ссылка на страницу "Рулонные шторы"
    roller_blinds = WebElement(xpath='//a[@href="/roller_blinds/"]')

    # Конструктор рулонных штор на странице "Рулонные шторы"
    roller_blind_designer = WebElement(xpath='//h1[@class="constructor__title" and contains(text(), '
                                             '"Рулонные шторы по вашим размерам")]')

    # Ссылка на страницу "Окна алюминий"
    aluminum_windows = WebElement(xpath='//a[@class="main__smarts-item router-link-exact-active router-link-active"]')

    # Ссылка на страницу "Обои"
    wallpaper = WebElement(xpath='//a[@href="/wallpaper/"]')

    # Конструктор рулонных обои на странице "Обои"
    designer_wallpaper = WebElement(xpath='//h1[@class="constructor__title" and contains(text(), "Обои на заказ")]')

    # Ссылка на страницу "Кухонные уголки"
    kitchen_corner = WebElement(xpath='//a[@href="/kitchen_corner/"]')

    # Конструктор кухонных уголков на странице "Кухонные уголки"
    kitchen_corner_designer = WebElement(xpath='//h1[@class="title mb-3" and contains(text(), '
                                               '"Кухонные уголки на заказ")]')

    # Ссылка на страницу "Колеровка краски"
    color_paint = WebElement(xpath='//a[@href="/color_paint/ext/"]')

    # Конструктор колеровки краски на странице "Колеровка краски"
    paint_tinting_designer = WebElement(xpath='//h1[@class="color__title" and contains(text(), '
                                              '"Колеровка краски онлайн")]')


class Footer_content(StartPage):
    """ Локаторы стартовой страницы блока footer__content. """

    # Контактный телефон
    contact_phone = WebElement(xpath='//a[@class="fc__text fc__text_selectable fc__phone"]')

    # Ссылка на страницу "Вопросы и ответы"
    fc_help = WebElement(xpath='//a[@class="fc__help"]')

    # Раздел "Помощь" на странице "Вопросы и ответы"
    help_block = WebElement(xpath='//h1[@class="wrapper__hl" and contains(text(), "Помощь")]')

    # Ссылка на страницу "Доставка"
    fc_delivery = WebElement(xpath='//div/a[@href="/help/delivery/"]')

    # Ссылка на страницу "Акции"
    fc_stock = WebElement(xpath='//a[2][@href="/stock/"]')

    # Ссылка на страницу "Оплата"
    payment = WebElement(xpath='//a[3][@href="/help/how-to-pay/"]')

    # Ссылка на страницу "Услуги"
    services = WebElement(xpath='//a[4][@href="/help/services/"]')

    # Ссылка на страницу "Сервис и гарантия"
    fc_return = WebElement(xpath='//a[5][@href="/help/purchase-return/"]')

    # Ссылка на страницу "Предложения"
    fc_suggestions = WebElement(xpath='//a[@href="/appeal/" and contains(text(), "Предложения")]')

    # Раздел "Жалобы и предложения" на странице "Предложения"
    complaints = WebElement(xpath='//h1[@class="appeal__hl" and contains(text(), "Жалобы и предложения")]')

    # Ссылка на страницу "Жалобы"
    fc_complaints = WebElement(xpath='//a[@href="/appeal/" and contains(text(), "Жалобы")]')

    # Ссылка на страницу "Контакты и магазины"
    contacts_and_shops = WebElement(xpath='//a[@class="fc__link fc__text" and contains(text(), "Контакты и магазины")]')

    # Раздел "Контакты и магазины" на странице "Контакты и магазины"
    addresses_and_contacts = WebElement(xpath='//h1[@class="addresses-and-contacts-title" and contains(text(),'
                                              ' "Контакты и магазины")]')
    # Ссылка на страницу "Бонусная программа"
    fc_bonus_program = WebElement(xpath='//a[2][@href="/bonus-program/"]')

    # Ссылка на страницу "Вакансии"
    fc_vacancy = WebElement(xpath='//a[@href="/vacancy/"]')

    # Раздел "Работа в Аксон" на странице "Вакансии"
    job = WebElement(xpath='//h1[@class="vc__hl" and contains(text(), "Работа в Аксон")]')

    # Ссылка на страницу "О компании"
    fc_about = WebElement(xpath='//a[@href="/about/"]')

    # Раздел "Регионы присутствия" на странице "О компании"
    regions = WebElement(xpath='//h2[@class="about-region__hl" and contains(text(), "Регионы присутствия")]')

    # Ссылка на страницу "Поставщикам"
    fc_provider = WebElement(xpath='//a[@class="fc__link fc__text" and contains(text(), "Поставщикам")]')

    # Раздел "Авторизации" на странице "Поставщикам"
    provider_form = WebElement(xpath='//div[@class="forms-wrap-box reg"]')

    # Ссылка на страницу "Аренда площадей"
    fc_rent = WebElement(xpath='//a[@class="fc__link fc__text" and contains(text(), "Аренда площадей")]')

    # Раздел "Подать заявку" на странице "Аренда площадей"
    btn_rent = WebElement(xpath='//button[@class="arenda-header-apply arenda-btn-apply js-handler-modal '
                                '_bid_modalOpen-js"]')


class Catalog_links(StartPage):
    """ Локаторы раздела "Каталог". """

    # Подраздел "Сделай сам"
    do_it = WebElement(xpath='//div[@class="categories__children-title" and contains(text(), "Сделай сам")]')

    # Раздел "Готовые решения"
    turnkey_solutions = WebElement(xpath='//a[@class="categories__root-item" and contains(text(), '
                                              '"Готовые решения")]')

    # Раздел "Строительные материалы"
    construction_materials = WebElement(xpath='//a[@class="categories__root-item" and contains(text(), '
                                              '"Строительные материалы")]')

    # Подраздел "Строительные материалы"
    ctl_construction_materials = WebElement(xpath='//div[@class="categories__children-title" and contains(text(), '
                                                  '"Строительные материалы")]')

    # Раздел "Пиломатериалы"
    lumber = WebElement(xpath='//a[@class="categories__root-item" and contains(text(), "Пиломатериалы")]')

    # Подраздел "Пиломатериалы"
    ctl_lumber = WebElement(xpath='//div[@class="categories__children-title" and contains(text(), "Пиломатериалы")]')

    # Раздел "Водоснабжение"
    water_supply = WebElement(xpath='//a[@class="categories__root-item" and contains(text(),'
                                    ' "Водоснабжение и отопление")]')

    # Подраздел "Водоснабжение"
    ctl_water_supply = WebElement(xpath='//div[@class="categories__children-title" and contains(text(),'
                                        ' "Водоснабжение и отопление")]')

    # Раздел "Вентиляция"
    ventilation = WebElement(xpath='//a[@class="categories__root-item" and contains(text(), "Вентиляция")]')

    # Подраздел "Вентиляция"
    ctl_ventilation = WebElement(xpath='//div[@class="categories__children-title" and contains(text(), "Вентиляция")]')

    # Раздел "Электротовары"
    electrical = WebElement(xpath='//a[@class="categories__root-item" and contains(text(), "Электротовары")]')

    # Подраздел "Электротовары"
    ctl_electrical = WebElement(xpath='//div[@class="categories__children-title" and contains(text(),'
                                      ' "Электротовары")]')

    # Раздел "Скобяные изделия"
    hardware = WebElement(xpath='//a[@class="categories__root-item" and contains(text(), "Скобяные изделия")]')

    # Подраздел "Скобяные изделия"
    ctl_hardware = WebElement(xpath='//div[@class="categories__children-title" and contains(text(), '
                                    '"Скобяные изделия")]')

    # Раздел "Керамическая плитка"
    ceramic_tile = WebElement(xpath='//a[@class="categories__root-item" and contains(text(), "Керамическая плитка")]')

    # Подраздел "Керамическая плитка"
    ctl_ceramic_tile = WebElement(xpath='//div[@class="categories__children-title" and contains(text(), '
                                        '"Керамическая плитка")]')

    # Раздел "Краски"
    paints = WebElement(xpath='//a[@class="categories__root-item" and contains(text(), "Краски")]')

    # Подраздел "Краски"
    ctl_paints = WebElement(xpath='//div[@class="categories__children-title" and contains(text(), '
                                  '"Краски")]')

    # Раздел "Инструменты для ремонта и строительства"
    tools = WebElement(xpath='//a[@class="categories__root-item" and contains(text(), '
                             '"Инструменты для ремонта и строительства")]')

    # Подраздел "Инструменты для ремонта и строительства"
    ctl_tools = WebElement(xpath='//div[@class="categories__children-title" and contains(text(), '
                                 '"Инструменты для ремонта и строительства")]')

    # Раздел "Сантехника"
    plumbing = WebElement(xpath='//a[@class="categories__root-item" and contains(text(), "Сантехника")]')

    # Подраздел "Сантехника"
    ctl_plumbing = WebElement(xpath='//div[@class="categories__children-title" and contains(text(), "Сантехника")]')

    # Раздел "Отделка стен и потолков"
    decoration = WebElement(xpath='//a[@class="categories__root-item" and contains(text(), "Отделка стен и потолков")]')

    # Подраздел "Отделка стен и потолков"
    ctl_decoration = WebElement(xpath='//div[@class="categories__children-title" and contains(text(), '
                                '"Отделка стен и потолков")]')

    # Раздел "Обои"
    wallpaper = WebElement(xpath='//a[@class="categories__root-item" and contains(text(), "Обои")]')

    # Подраздел "Обои"
    ctl_wallpaper = WebElement(xpath='//div[@class="categories__children-title" and contains(text(), "Обои")]')

    # Раздел "Напольные покрытия"
    floor_coverings = WebElement(xpath='//a[@class="categories__root-item" and contains(text(), "Напольные покрытия")]')

    # Подраздел "Напольные покрытия"
    ctl_floor_coverings = WebElement(xpath='//div[@class="categories__children-title" and contains(text(), '
                                     '"Напольные покрытия")]')

    # Раздел "Двери"
    doors = WebElement(xpath='//a[@class="categories__root-item" and contains(text(), "Двери")]')

    # Подраздел "Двери"
    ctl_doors = WebElement(xpath='//div[@class="categories__children-title" and contains(text(), "Двери")]')

    # Раздел "Окна"
    windows = WebElement(xpath='//a[@class="categories__root-item" and contains(text(), "Окна")]')

    # Подраздел "Окна"
    ctl_windows = WebElement(xpath='//div[@class="categories__children-title" and contains(text(), "Окна")]')

    # Раздел "Системы хранения"
    storage_systems = WebElement(xpath='//a[@class="categories__root-item" and contains(text(), "Системы хранения")]')

    # Подраздел "Системы хранения"
    ctl_storage_systems = WebElement(xpath='//div[@class="categories__children-title" and contains(text(), '
                                           '"Системы хранения")]')

    # Раздел "Освещение"
    lighting = WebElement(xpath='//a[@class="categories__root-item" and contains(text(), "Освещение")]')

    # Подраздел "Освещение"
    ctl_lighting = WebElement(xpath='//div[@class="categories__children-title" and contains(text(), "Освещение")]')

    # Раздел "Мебель"
    furniture = WebElement(xpath='//a[@class="categories__root-item" and contains(text(), "Мебель")]')

    # Подраздел "Мебель"
    ctl_furniture = WebElement(xpath='//div[@class="categories__children-title" and contains(text(), "Мебель")]')

    # Раздел "Интерьер и декор"
    decor = WebElement(xpath='//a[@class="categories__root-item" and contains(text(), "Интерьер и декор")]')

    # Подраздел "Интерьер и декор"
    ctl_decor = WebElement(xpath='//div[@class="categories__children-title" and contains(text(), "Интерьер и декор")]')

    # Раздел "Бытовая техника"
    appliances = WebElement(xpath='//a[@class="categories__root-item" and contains(text(), "Бытовая техника")]')

    # Подраздел "Бытовая техника"
    ctl_appliances = WebElement(xpath='//div[@class="categories__children-title" and contains(text(), '
                                      '"Бытовая техника")]')

    # Раздел "Автотовары"
    auto_products = WebElement(xpath='//a[@class="categories__root-item" and contains(text(), "Автотовары")]')

    # Подраздел "Автотовары"
    ctl_auto_products = WebElement(xpath='//div[@class="categories__children-title" and contains(text(), '
                                         '"Автотовары")]')

    # Раздел "Товары для отдыха и хобби"
    hobby = WebElement(xpath='//a[@class="categories__root-item" and contains(text(), "Товары для отдыха и хобби")]')

    # Подраздел "Товары для отдыха и хобби"
    ctl_hobby = WebElement(xpath='//div[@class="categories__children-title" and contains(text(), '
                                 '"Товары для отдыха и хобби")]')

    # Раздел "Товары для дома"
    household_products = WebElement(xpath='//a[@class="categories__root-item" and contains(text(), "Товары для дома")]')

    # Подраздел "Товары для дома"
    ctl_household_products = WebElement(xpath='//div[@class="categories__children-title" and contains(text(), '
                                              '"Товары для дома")]')

    # Раздел "Посуда"
    tableware = WebElement(xpath='//a[@class="categories__root-item" and contains(text(), "Посуда")]')

    # Подраздел "Посуда"
    ctl_tableware = WebElement(xpath='//div[@class="categories__children-title" and contains(text(), "Посуда")]')

    # Раздел "Товары для сада"
    garden_supplies = WebElement(xpath='//a[@class="categories__root-item" and contains(text(), "Товары для сада")]')

    # Подраздел "Товары для сада"
    ctl_garden_supplies = WebElement(xpath='//div[@class="categories__children-title" and contains(text(), '
                                           '"Товары для сада")]')

    # Раздел "Умный дом"
    smart_house = WebElement(xpath='//a[@class="categories__root-item" and contains(text(), "Умный дом")]')

    # Подраздел "Умный дом"
    ctl_smart_house = WebElement(xpath='//div[@class="categories__children-title" and contains(text(), "Умный дом")]')