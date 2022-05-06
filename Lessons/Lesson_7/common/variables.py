"""Константы"""
from logging import DEBUG, ERROR

DEFAULT_PORT = 7777  # Стандартная настройка порта для сетевого ваимодействия
DEFAULT_IP_ADDRESS = '127.0.0.1'   # Стандартная настройка IP адрес  для подключения клиента
MAX_CONNECTIONS = 5   # Максимальная количество подключений
MAX_MESSAGE_SIZE = 1024    # Максимальный размер сообщения в байтах
ENCODING = 'utf-8'   # Стандартная кодировка
LOGGING_LEVEL = DEBUG    # Текущий уровень логирования
LOGGING_LEVEL_FOR_STREAM_HANDLER = ERROR  # Текущий уровень логирования для потокового вывода
# SERVER_DATABASE = 'sqlite:///server_db.db3'   # База данных для хранения данных сервера
SERVER_CONFIG = 'server.ini'
# Прококол JIM основные ключи:
ACTION = 'action'
TIME = 'time'
USER = 'user'
ACCOUNT_NAME = 'account_name'
SENDER = 'from'
DESTINATION = 'to'
DATA = 'bin'
PUBLIC_KEY = 'pubkey'

# Прочие ключи, используемые в протоколе
PRESENCE = 'presence'
RESPONSE = 'response'
ERROR = 'error'
MESSAGE = 'message'
MESSAGE_TEXT = 'mess_text'
EXIT = 'exit'
GET_CONTACTS = 'get_contacts'
LIST_INFO = 'data_list'
REMOVE_CONTACT = 'remove'
ADD_CONTACT = 'add'
USERS_REQUEST = 'get_users'
PUBLIC_KEY_REQUEST = 'pubkey_need'

# Словари - ответы:
# 200
RESPONSE_200 = {RESPONSE: 200}
# 202
RESPONSE_202 = {RESPONSE: 202,
                LIST_INFO: None
                }
# 400
RESPONSE_400 = {
    RESPONSE: 400,
    ERROR: None
}
# 205
RESPONSE_205 = {
    RESPONSE: 205
}

# 511
RESPONSE_511 = {
    RESPONSE: 511,
    DATA: None
}

IMG = 'server/img'
EXIT_IMG = f'{IMG}/exit.png'