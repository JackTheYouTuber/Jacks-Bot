import hikari
from Cogs import __Bot_Functions__

TOKEN = "Token"
bot = hikari.GatewayBot(token=TOKEN)

@bot.listen(hikari.GuildMessageCreateEvent)
async def Message_Events(event:hikari.events.GuildMessageCreateEvent):
    message = event.content
    message_author = event.author
    message_channel_location = event.get_channel()

    # Log the text
    Log_Text = f"[{message_author}] :> {message} | [Channel({message_channel_location})]"
    __Bot_Functions__.Log(Log_Text=Log_Text)

    # Bot Commands

bot.run()
