from email import message
import hikari
from Cogs import __Bot_Functions__

TOKEN = "Token"
bot = hikari.GatewayBot(token=TOKEN)

@bot.listen(hikari.GuildMessageCreateEvent)
async def Log_Events(event:hikari.events.GuildMessageCreateEvent):
    message = event.content
    message_author = event.author
    message_channel_location = event.get_channel()

    # Log the text
    Log_Text = f"[{message_author}] :> {message} | [Channel({message_channel_location})]"
    __Bot_Functions__.Log(Log_Text=Log_Text)

@bot.listen(hikari.GuildChannelCreateEvent)
async def Bot_Command(event:hikari.events.GuildMessageCreateEvent):
    message = event.content
    message_author = event.author
    message_channel_location = event.get_channel()
    message_channel_location_id = event.channel_id

    # Bot Commands
    Bot_Command = __Bot_Functions__.Command(message, message_author, message_channel_location)
    await bot.rest.create_message(content=Bot_Command, channel=message_channel_location_id)    



bot.run()
