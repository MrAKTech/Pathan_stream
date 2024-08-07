import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '22225617'))
    API_HASH = str(getenv('API_HASH', 'ef16f7597376f1689663304c954e4493'))
    PICS = (environ.get('PICS','https://graph.org/file/8cd764fbdf3ccd34abe22.jpg')).split()
    BOT_TOKEN = str(getenv('BOT_TOKEN', '7242317141:AAGAIjdTlThKtArXmB0bD7bDMmus10Ur6G0'))
    name = str(getenv('name', 'NobitaStreamBot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1002053122232'))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "6072149828").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'I_Am_MrAK'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL', True))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://akmonsterprogrammer:S.Aruna1155182089@filetolink.erqitim.mongodb.net/?retryWrites=true&w=majority&appName=filetolink'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', 'MrAK_LinkZz'))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "")).split()))
