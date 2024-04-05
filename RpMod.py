from .. import loader, utils

rplist = {"чмок": "😘 | <a href=tg://user?id={}>{}</a> чмокнул(-а) <a href=tg://user?id={}>{}</a>",
          "чпок": "👉👌 | <a href=tg://user?id={}>{}</a> чпокнул(-а) <a href=tg://user?id={}>{}</a>",
          "кусь": "🦷 | <a href=tg://user?id={}>{}</a> кусьнул(-а) <a href=tg://user?id={}>{}</a>",
          "обнять": "🥰 | <a href=tg://user?id={}>{}</a> обнял(-а) <a href=tg://user?id={}>{}</a>",
          "шлеп": "🖐 | <a href=tg://user?id={}>{}</a> шлепнул(-а) <a href=tg://user?id={}>{}</a>",
          "убить": "🔪 | <a href=tg://user?id={}>{}</a> убил(-а) <a href=tg://user?id={}>{}</a>",
          "выебать": "👺 | <a href=tg://user?id={}>{}</a> выебал(-а) <a href=tg://user?id={}>{}</a>",
          "связать": "⛓ | <a href=tg://user?id={}>{}</a> связал(-а) <a href=tg://user?id={}>{}</a>",
          "ударить": "👊 | <a href=tg://user?id={}>{}</a> ударил(-а) <a href=tg://user?id={}>{}</a>",
          "уебать": "🤜 | <a href=tg://user?id={}>{}</a> уебал(-а) <a href=tg://user?id={}>{}</a>",
          "отсосать": "🍌 | <a href=tg://user?id={}>{}</a> отсосал(-а) у <a href=tg://user?id={}>{}</a>",
          "отлизать": "👅 | <a href=tg://user?id={}>{}</a> отлизал(-а) у <a href=tg://user?id={}>{}</a>",
          "задушить": "😵 | <a href=tg://user?id={}>{}</a> задушил(-а) <a href=tg://user?id={}>{}</a>",
          "украсть": "👹 | <a href=tg://user?id={}>{}</a> украл(-а) <a href=tg://user?id={}>{}</a>",
          "погладить": "🤗 | <a href=tg://user?id={}>{}</a> погладил(-а) <a href=tg://user?id={}>{}</a>",
          "притянуть": "😏 | <a href=tg://user?id={}>{}</a> притянул(-а) <a href=tg://user?id={}>{}</a>",
          "изнасиловать": "🥵 | <a href=tg://user?id={}>{}</a> изнасиловал(-а) <a href=tg://user?id={}>{}</a>",
          "отпороть": "😨 | <a href=tg://user?id={}>{}</a> отпорол(-а) <a href=tg://user?id={}>{}</a>"}

@loader.tds
class RPMod(loader.Module):
    """Модуль RPMod"""
    strings = {"name": "RPMod"}

    async def client_ready(self, client, db):
        self.db = db
        self.db.set("RPMod", "status", True)

    async def rpmodcmd(self, message):
        """Используй: .rpmod чтобы включить/выключить RP режим."""
        status = self.db.get("RPMod", "status")
        if status:
            self.db.set("RPMod", "status", False)
            await message.edit("<b>RP режим <code>выключен</code></b>")
        else:
            self.db.set("RPMod", "status", True)
            await message.edit("<b>RP режим <code>включен</code></b>")

    async def rplistcmd(self, message):
        """Используй: .rplist чтобы посмотреть список рп команд."""
        listrp = ""
        for x in rplist:
            listrp += f"{x}, "
        await message.edit(f"{listrp[:-2]}.")

    async def watcher(self, message):
        try:
            status = self.db.get("RPMod", "status")
            reply = await message.get_reply_message()
            user = await message.client.get_entity(reply.sender_id)
            me = await message.client.get_me()
            if status:
                if message.sender_id == me.id:
                    if message.text.lower() in rplist:
                        getrp = rplist.get(message.text.lower())
                        await message.edit(getrp.format(me.id, me.first_name, user.id, user.first_name))
        except: pass