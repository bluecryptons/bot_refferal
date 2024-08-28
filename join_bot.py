from telethon import TelegramClient
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.errors import SessionPasswordNeededError
import asyncio

# Ganti dengan API ID dan API Hash dari aplikasi Telegram Anda
API_ID = '29445957'
API_HASH = 'ea1dc93974f40fcad641e45ef93d4e59'
# Ganti dengan nomor telepon Anda (format internasional)
PHONE = '+6285161403991'
# URL undangan referral
INVITE_URL = 't.me/catsgang_bot?startapp=TIEKxkfrpd5cD_0cxJeoe'

async def main():
    # Membuat instance TelegramClient
    client = TelegramClient('session_name', 29445957, ea1dc93974f40fcad641e45ef93d4e59)
    
    # Memulai client
    await client.start(PHONE)
    
    try:
        # Bergabung ke grup atau channel menggunakan link undangan
        await client(ImportChatInviteRequest(INVITE_URL))
        print(f"Successfully joined using invite link: {INVITE_URL}")
    except SessionPasswordNeededError:
        print("Two-step verification is enabled. Please enter your password.")
        await client.start(PHONE, password=input("Password: "))
        await client(ImportChatInviteRequest(INVITE_URL))
        print(f"Successfully joined using invite link: {INVITE_URL}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    asyncio.run(main())
