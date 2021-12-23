from telethon.events import ChatAction
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from telethon.tl.types import MessageEntityMentionName

from Lucifer import CMD_HELP
from Lucifer.utils import admin_cmd


async def get_full_user(event):
    args = event.pattern_match.group(1).split(":", 1)
    extra = None
    if event.reply_to_msg_id and not len(args) == 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("`User ID Is Required")
            return
        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except Exception as err:
            return await event.edit("Something Went Wrong", str(err))
    return user_obj, extra


async def get_user_sender_id(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj


@borg.on(admin_cmd(pattern="gban ?(.*)"))
async def gspider(userbot):
    lol = userbot
    await lol.get_sender()
    me = await lol.client.get_me()

    await lol.edit("ωαιт ℓεммε ρяσcεss...")
    me = await userbot.client.get_me()
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    await lol.edit(
        f"gℓσвαℓ вαη ιs cσммιηg мү вσι! נυsт ωαιт αη∂ ωαтcн🔥🔥 \nвү үσυя ∂α∂ {my_mention}"
    )

    f"@{me.username}" if me.username else my_mention
    await userbot.get_chat()
    a = b = 0
    if userbot.is_private:
        user = userbot.chat
        reason = userbot.pattern_match.group(1)
    else:
        userbot.chat.title
    try:
        user, reason = await get_full_user(userbot)
    except BaseException:
        pass
    try:
        if not reason:
            reason = "Private"
    except BaseException:
        return await lol.edit(f"**sσмεтнιηg ωεηт ωяσηg**")
    if user:
        if user.id == 804329190 or user.id == 1363797554:
            return await lol.edit(
                f"**нε ιs үσυя ғαтнεя υ cαη'т вαη нιм ғυк σғ вιтcн🖕🖕**"
            )
        try:
            from userbot.modules.sql_helper.gmute_sql import gmute
        except BaseException:
            pass
        try:
            await userbot.client(BlockRequest(user))
        except BaseException:
            pass
        testuserbot = [
            d.entity.id
            for d in await userbot.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testuserbot:
            try:
                await userbot.client.edit_permissions(i, user, view_messages=False)
                a += 1
                await lol.edit(f"**gвαηηε∂ ηιggα // тσтαℓ gяσυρ αғғεcтε∂**: `{a}`")
            except BaseException:
                b += 1
    else:
        await lol.edit(f"**Reply to a user !!**")
    try:
        if gmute(user.id) is False:
            return await lol.edit(f"**εяяσя! нεү мαsтεя тнε υsεя ιs αℓяεα∂ү gвαηηε∂.**")
    except BaseException:
        pass
    return await lol.edit(
        f"**gвαηηε∂ [{user.first_name}](tg://user?id={user.id}) тσтαℓ αғғεcтε∂ cнαтs : {a} **"
    )


@borg.on(admin_cmd(pattern="ungban ?(.*)"))
async def gspider(userbot):
    lol = userbot
    sender = await lol.get_sender()
    me = await lol.client.get_me()
    if not sender.id == me.id:
        await lol.reply("`ωαιт ℓεммε ρяσcεss`")
    else:
        await lol.edit("נυsт α sεcση∂s ")
    me = await userbot.client.get_me()
    await lol.edit(f"тяүιηg тσ υηgвαη!")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    f"@{me.username}" if me.username else my_mention
    await userbot.get_chat()
    a = b = 0
    if userbot.is_private:
        user = userbot.chat
        reason = userbot.pattern_match.group(1)
    else:
        userbot.chat.title
    try:
        user, reason = await get_full_user(userbot)
    except BaseException:
        pass
    try:
        if not reason:
            reason = "Private"
    except BaseException:
        return await lol.edit("Someting Went Wrong 🤔")
    if user:
        if user.id == 1415798813 or user.id == 1363797554:
            return await lol.edit(
                "**You Cant gban him... as a result you can not ungban him... He is My Creator!**"
            )
        try:
            from userbot.modules.sql_helper.gmute_sql import ungmute
        except BaseException:
            pass
        try:
            await userbot.client(UnblockRequest(user))
        except BaseException:
            pass
        testuserbot = [
            d.entity.id
            for d in await userbot.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testuserbot:
            try:
                await userbot.client.edit_permissions(i, user, send_messages=True)
                a += 1
                await lol.edit(f"**UNGBANNING // AFFECTED CHATS - {a} **")
            except BaseException:
                b += 1
    else:
        await lol.edit("**Reply to a user !!**")
    try:
        if ungmute(user.id) is False:
            return await lol.edit("**Error! User probably already ungbanned.**")
    except BaseException:
        pass
    return await lol.edit(
        f"**UNGBANNED // USER - [{user.first_name}](tg://user?id={user.id}) CHATS : {a} **"
    )


@borg.on(ChatAction)
async def handler(rkG):
    if rkG.user_joined or rkG.user_added:
        try:
            from userbot.modules.sql_helper.gmute_sql import is_gmuted

            guser = await rkG.get_user()
            gmuted = is_gmuted(guser.id)
        except BaseException:
            return
        if gmuted:
            for i in gmuted:
                if i.sender == str(guser.id):
                    chat = await rkG.get_chat()
                    admin = chat.admin_rights
                    creator = chat.creator
                    if admin or creator:
                        try:
                            await client.edit_permissions(
                                rkG.chat_id, guser.id, view_messages=False
                            )
                            await rkG.reply(
                                f"**gвsηηε∂ ηιggα нεяε\nℓεммε вαη нιм!!** \n"
                                f"**vιcтяιм ι∂**: [{guser.id}](tg://user?id={guser.id})\n"
                                f"**αcтιση **  : `Banned`"
                            )
                        except BaseException:
                            rkG.reply("`ғυк ι ∂σηт нαв ρεямιssιση тσ вαη нιм`")
                            return


CMD_HELP.update({"gban": "gban any user using username or tag dont use id "})
