import hikari
from Cogs import __Bot_Functions__

TOKEN = "ODkzODIyOTY3NTA5ODM5OTMy.G1199d.Ynquwq2skutSCNCsjDivsBwPrKAUYhvHZq3kb8"
bot = hikari.GatewayBot(token=TOKEN)

@bot.listen(hikari.GuildMessageCreateEvent)
async def Log_Message_Events(event:hikari.events.GuildMessageCreateEvent):
    message = event.content
    message_author = event.author
    message_channel_location = event.get_channel()
    Log_Text = f"[{message_author}] :> {message} | [Channel({message_channel_location})]"
    __Bot_Functions__.Log(Log_Text=Log_Text)

bot.run()
