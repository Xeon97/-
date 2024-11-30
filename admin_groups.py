
# -*- coding: utf-8 -*-

# This is a custom module for Hikka Userbot
# Author: Your Name
# Description: Checks the groups where the user is an admin and provides links to those groups.

from telethon import types
from .. import loader, utils

class AdminGroupsMod(loader.Module):
    """Checks groups where you are an admin and provides links to those groups."""
    strings = {"name": "AdminGroups"}

    async def admgrpscmd(self, message):
        """Finds groups where you are an admin.
        Usage: .admgrps
        """
        result = []
        me = await message.client.get_me()
        async for dialog in message.client.iter_dialogs():
            if dialog.is_group or dialog.is_channel:
                chat = dialog.entity
                if isinstance(chat, (types.Chat, types.Channel)) and chat.creator:
                    # You are the creator
                    result.append(f"👑 <b>{chat.title}</b> - <a href='https://t.me/{chat.username if chat.username else f'c/{chat.id}' }'>link</a>")
                elif hasattr(chat, "admin_rights") and chat.admin_rights:
                    # You are an admin
                    result.append(f"🛡 <b>{chat.title}</b> - <a href='https://t.me/{chat.username if chat.username else f'c/{chat.id}' }'>link</a>")

        if not result:
            await message.edit("<b>You are not an admin in any groups or channels.</b>")
        else:
            await message.edit("<b>Groups where you are an admin:</b>\n\n" + "\n".join(result))
