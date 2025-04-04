
---

### `get_folder_ids.py` (Folder Ka Jasoos – Masti Ke Saath) 🕵️‍♂️
```python
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogFiltersRequest

# Bhai, yeh tera VIP pass – apne details daal! 😎
api_id = 'YOUR_API_ID_HERE'  # ID nahi toh entry nahi!
api_hash = 'YOUR_API_HASH_HERE'  # Secret code, chhupa ke rakhna! 🕵️‍♂️
phone = 'YOUR_PHONE_NUMBER_HERE'  # +91 wala number, samjha? 📞

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start(phone)
    print("Arre bhai, login ho gaya! Ab dekhte hain teri folder ki shaan! 😎")
    
    dialog_filters = await client(GetDialogFiltersRequest())
    print("\nBhai, yeh raha tere Telegram ka folder ka tamasha:")
    for folder in dialog_filters.filters:
        if hasattr(folder, 'id'):
            folder_title = folder.title.text if hasattr(folder.title, 'text') else folder.title
            print(f"🎯 ID: {folder.id} | Naam: {folder_title} 🎯")
    print("\nID le aur agla kaam shuru kar, @Lets_CreateExplor_Tech pe shaan badha! 🔥")

with client:
    print("Bhai ka Folder Jasoos shuru – @Lets_CreateExplor_Tech ka jadoo! 😎")
    client.loop.run_until_complete(main())
