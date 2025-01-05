from telethon.sync import TelegramClient
from telethon.errors import SessionPasswordNeededError

api_id = 'MYID'
api_hash = 'MYHASH'
phone_number = 'MYPHONENUMBER

client = TelegramClient('session_name', api_id, api_hash)

async def send_message(destination, message):
 
    try:
        await client.start(phone=phone_number)
        await client.send_message(destination, message)
        print(f"message was succesfully sent {destination}")
    except SessionPasswordNeededError:
        print("need password")
    except Exception as e:
        print(f"error {e}")
    finally:
        await client.disconnect()

import asyncio

destination = '@rhusus' 
message = 'Hola Amigo!!!!!!!!'

asyncio.run(send_message(destination, message))
