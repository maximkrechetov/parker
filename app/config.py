# coding: utf8
from collections import OrderedDict

URL_REPLACE_RULES = OrderedDict((
    ('http://novosibirsk.e2e4online.ru/shop/catalog/item/?id=', 'https://beta.e2e4.ru/nsk/offer/'),
    ('http://novosibirsk.e2e4online.ru/shop/catalog/#/search=', 'https://beta.e2e4.ru/nsk/search?text='),
    ('http://novosibirsk.e2e4online.ru/shop/info/action/', 'https://beta.e2e4.ru/nsk/promotions/'),
    ('http://novosibirsk.e2e4online.ru/shop/info/events/?id=', 'https://beta.e2e4.ru/nsk/events/'),
    ('http://novosibirsk.e2e4online.ru/shop/info/events/?type=47', 'https://beta.e2e4.ru/nsk/articles/'),
    ('http://novosibirsk.e2e4online.ru/shop/info/events/?type=1', 'https://beta.e2e4.ru/nsk/news/'),
    ('http://novosibirsk.e2e4online.ru/shop/', 'https://beta.e2e4.ru/nsk/'),
    ('http://novosibirsk.e2e4online.ru/catalog2/', 'https://beta.e2e4.ru/nsk/catalog/')
))

OUTPUT_FILE_EXTENSIONS = ['.txt', '.rtf']
INPUT_FILE_VALIDATORS = ['existence', 'exactly', 'xml_extension']
OUTPUT_FILE_VALIDATORS = ['extension']
