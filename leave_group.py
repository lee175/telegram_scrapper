from telethon import TelegramClient, connection
import logging
from telethon import sync, TelegramClient, events
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, UserStatusOffline, UserStatusRecently, UserStatusLastMonth, \
    UserStatusLastWeek
from telethon.tl.types import ChannelParticipantsSearch
from telethon.tl.functions.channels import GetParticipantsRequest
import json
from datetime import datetime, timedelta
from telethon.tl.functions.channels import JoinChannelRequest

logging.basicConfig(level=logging.WARNING)

# I need entity of the channel/group
SOURCE = "https://t.me/mantrimall0002"
TARGET = "https://t.me/Tc_clubTrisha" 
folder_session = 'session/'

with open('config.json', 'r', encoding='utf-8') as f:
    config = json.loads(f.read())
accounts = config['accounts']
account = accounts[0]
account_phone = account["phone"]
account_api_id = account["api_id"]
account_api_hash = account["api_hash"]

# now i need to get the client

# get account
client = TelegramClient(folder_session + account_phone, account_api_id, account_api_hash)
client.connect()

if client.is_user_authorized():
    print(account_phone + ' login success')
else:
    print(account_phone + ' login fail')
    print( 'quiting application')
    quit()


SOURCE_CHANNEL_ENTITY = client.get_entity(SOURCE)
TARGET_CHANNEL_ENTITY = client.get_entity(TARGET)

try:
    client(JoinChannelRequest(SOURCE_CHANNEL_ENTITY))
except:
    print('error occured while joining SOURCE CHANNEL')
    print('quiting application')
    quit()

try:
    client(JoinChannelRequest(TARGET_CHANNEL_ENTITY))
except:
    print('error occured while joining TARGET CHANNEL')
    print('quiting application')
    quit()