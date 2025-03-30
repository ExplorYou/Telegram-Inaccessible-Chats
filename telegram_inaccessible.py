from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogFiltersRequest, UpdateDialogFilterRequest
from telethon.tl.types import InputPeerUser, InputPeerChannel, InputPeerChat

# Bhai, yeh teri entry gate hai, apne VIP details daal de! 😜
api_id = 'YOUR_API_ID_HERE'  # ID nahi daala toh gate band, samjha? 😏
api_hash = 'YOUR_API_HASH_HERE'  # Yeh hai tera secret masala! 🌶️
phone = 'YOUR_PHONE_NUMBER_HERE'  # Apna number daal, warna bhool ja maza! 📱

# Telegram ka DJ booth shuru, bhai log! 🎧
client = TelegramClient('session_name', api_id, api_hash)

async def main():
    # Party shuru karo, login time hai! 🎉
    await client.start(phone)
    print("Arre bhai, swagat hai Telegram ke jungle mein! 😎")
    
    # Inaccessible chats ka gang taiyar karo, jo band hai woh aayega! 🚫
    inaccessible_peers = []
    async for dialog in client.iter_dialogs():
        entity = dialog.entity
        if hasattr(entity, 'id'):
            # Sirf woh chats jo band ya restricted hai, bots bhi add karo!
            if (hasattr(entity, 'left') and entity.left) or \
               (hasattr(entity, 'restricted') and entity.restricted) or \
               (hasattr(entity, 'bot') and entity.bot and not entity.access_hash):
                if hasattr(entity, 'access_hash') and entity.access_hash:
                    if isinstance(entity, InputPeerChannel.__base__):
                        peer = InputPeerChannel(entity.id, entity.access_hash)
                    elif isinstance(entity, InputPeerUser.__base__) and entity.bot:
                        peer = InputPeerUser(entity.id, entity.access_hash)
                    else:
                        continue
                else:
                    if isinstance(entity, InputPeerChat.__base__):
                        peer = InputPeerChat(entity.id)
                    else:
                        continue
                inaccessible_peers.append(peer)
    
    if not inaccessible_peers:
        print("Arre bhai, koi band chat nahi mila, sab khule hai kya? 😂")
        return
    
    # Folders ka jasoosi mission shuru! 🕵️‍♂️
    dialog_filters = await client(GetDialogFiltersRequest())
    
    # "All For One" ko dhoondho, bhai ka favourite folder! 🌟
    target_folder = None
    for folder in dialog_filters.filters:
        if hasattr(folder, 'id'):
            folder_title = folder.title.text if hasattr(folder.title, 'text') else folder.title
            if folder_title == "All For One":
                target_folder = folder
                break
    
    if not target_folder:
        print("Arre 'All For One' kahan gum ho gaya? Yeh raha pura folder ka tamasha:")
        for folder in dialog_filters.filters:
            if hasattr(folder, 'id'):
                folder_title = folder.title.text if hasattr(folder.title, 'text') else folder.title
                print(f"🎯 ID: {folder.id} | Naam: {folder_title} 🎯")
        return
    
    # Purane chats ko dhakka maaro, naye inaccessible chats add karo! 💪
    updated_folder = target_folder.__class__(
        id=target_folder.id,
        title=target_folder.title,
        pinned_peers=target_folder.pinned_peers or [],
        include_peers=inaccessible_peers,  # Sirf band chats ka swag!
        exclude_peers=target_folder.exclude_peers or [],
        contacts=target_folder.contacts,
        non_contacts=target_folder.non_contacts,
        groups=target_folder.groups,
        broadcasts=target_folder.broadcasts,
        bots=target_folder.bots,
        exclude_muted=target_folder.exclude_muted,
        exclude_read=target_folder.exclude_read,
        exclude_archived=target_folder.exclude_archived,
        emoticon=target_folder.emoticon
    )
    
    # Folder ko update karo, bhai ka style dikhao! 😎
    result = await client(UpdateDialogFilterRequest(
        id=target_folder.id,
        filter=updated_folder
    ))
    
    if result:
        print(f"Pehle wale sab nikal diye, ab 'All For One' (ID: {target_folder.id}) mein band chats ka dhamaka!")
        print(f"Total {len(inaccessible_peers)} band groups, channels, aur bots add kiye gaye! 🎉")
        print("Aur bhai, @sup_toon_1 pe aaja, wahan asli shaan hai! 🔥")
    else:
        print("Arre update mein gadbad ho gayi, Telegram ko thok do ek baar! 😡")

# Party ka aakhri beat, chalo! 🎵
with client:
    client.loop.run_until_complete(main())