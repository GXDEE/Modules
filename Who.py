__version__ = ("-beta",1,0)

# module: Who
# meta developer: GXDEE.t.me

from .. import loader, utils
@loader.tds
class Who(loader.Module):
    strings = {"name": "Who"}

#1#

    error_reply = "<emoji document_id=5208777366964311643>😵</emoji><b> Error: </b>no reply"
    no_photo_msg = "<emoji document_id=5208777366964311643>😵</emoji><b> Error: </b>user hid the avatar or blocked you"

#2#

    @loader.command(ru_doc="Gives information about user")
    async def who(self, message):
        check_reply = message.is_reply
        if not check_reply:
            await utils.answer(message, self.error_reply)
            return

#3.1#

        reply = await message.get_reply_message()
        user = await message.client.get_entity(reply.sender_id)
        first_name = user.first_name or ""
        last_name = user.last_name or ""
        name = f"{first_name} {last_name}".strip()

#3.2#

        if user.username and user.username.strip():
            display_name = utils.escape_html(name)
            username_text = f"@{user.username}"
        else:
            display_name = utils.escape_html(name)
            username_text = f'<a href="tg://user?id={user.id}">{utils.escape_html(name)}</a>'

#4#

        user_id = user.id
        text = (
            "<emoji document_id=5213351489954677363>🔝</emoji><b> Name:</b> "
            f"{display_name}\n"
            "<emoji document_id=5210696650409935856>🤟</emoji><b> Username:</b> "
            f"{username_text}\n"
            "<emoji document_id=5211051925809695623>📀</emoji><b> User ID:</b> "
            f"<code>{user_id}</code>"
        )
        await utils.answer(message, text, parse_mode="HTML")

#5#

    @loader.command(ru_doc="Gives information about user with photo")
    async def whop(self, message):
        check_reply = message.is_reply
        if not check_reply:
            await utils.answer(message, self.error_reply)
            return

#6.1#

        reply = await message.get_reply_message()
        user = await message.client.get_entity(reply.sender_id)
        try:
            test_photo = await message.client.download_profile_photo(user)
        except:
            test_photo = None
        if not test_photo:
            await utils.answer(message, self.no_photo_msg)
            return
        first_name = user.first_name or ""
        last_name = user.last_name or ""
        name = f"{first_name} {last_name}".strip()

#6.2#

        if user.username and user.username.strip():
            display_name = utils.escape_html(name)
            username_text = f"@{user.username}"
        else:
            display_name = utils.escape_html(name)
            username_text = f'<a href="tg://user?id={user.id}">{utils.escape_html(name)}</a>'

#7#

        user_id = user.id
        text = (
            "<emoji document_id=5213351489954677363>🔝</emoji><b> Name:</b> "
            f"{display_name}\n"
            "<emoji document_id=5210696650409935856>🤟</emoji><b> Username:</b> "
            f"{username_text}\n"
            "<emoji document_id=5211051925809695623>📀</emoji><b> User ID:</b> "
            f"<code>{user_id}</code>"
        )

#8#

        await message.edit(
            file=test_photo,
            text=text,
            parse_mode="HTML"
        )
#TODO добавить логику для чека видаоватарка у человека или нет, если видео то качать как mov а не PNG, сделать блок текстовых переменных в начале кода а не в блоке вывода функции, в выводе использовать текстовые переменные вместо текста, проверять есть у человека несколько юзов, если несколько то вывод будет другой со списком юзой взятых в цитату, добавить просмотр датацентра