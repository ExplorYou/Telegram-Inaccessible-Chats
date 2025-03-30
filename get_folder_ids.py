from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogFiltersRequest

# Bhai, yeh raha tera VIP pass, apne credentials daal de 😎
api_id = 'YOUR_API_ID_HERE'  # Apna API ID daal, nahi toh kaam nahi chalega, samjha na?
api_hash = 'YOUR_API_HASH_HERE'  # Yeh secret code hai, chhupa ke rakhna! 🕵️‍♂️
phone = 'YOUR_PHONE_NUMBER_HERE'  # Number daal +91 ke saath, warna bhool ja script! 📞

# Telegram ka darwaza kholte hain, bhai log!
client = TelegramClient('session_name', api_id, api_hash)

async def main():
    # Darwaza khol, bhai, login time hai! 🚪
    await client.start(phone)
    print("Arre bhai, login ho gaya! Ab dekhte hain teri folder ki shaan! 😎")
    
    # Folders ki list nikalte hain, ekdum filmy style mein 🎬
    dialog_filters = await client(GetDialogFiltersRequest())
    
    # Folders ki parade shuru, dekho kaun kaun aaya! 🎉
    print("\nBhai, yeh raha tere Telegram ka folder ka tamasha:")
    for folder in dialog_filters.filters:
        if hasattr(folder, 'id'):
            folder_title = folder.title.text if hasattr(folder.title, 'text') else folder.title
            print(f"🎯 ID: {folder.id} | Naam: {folder_title} 🎯")
    print("\nBas yahi hai teri folder ki gang, ab ID choose kar aur kaam chalu kar! 😏")
    print("Aur haan, @sup_toon_1 join karna mat bhoolna, wahan asli maza hai! 🔥")

# Script ko dance floor pe bhejo! 💃🕺
with client:
    client.loop.run_until_complete(main())