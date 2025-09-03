import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv(detenv_path = ".env/config")

bot = commands.Bot(command_prefix="!")

# activer la reconnaissance de l'évênement onMemberJoin
# default_intents = discord.Intents.default()
# default_intents.members = True # activeer members
# client = discord.Client(intents=default_intents)

# async car c'est une coroutine, et on ready pour que ça fonctionne
# @bot.event # reconnaît le fonction ci-dessous
# async def on_ready():
#     print("Le bot est prêt")

class DocBot(commands.Bot)
    def__init__(self): # initialiser les instances de la classe
        super().__init__(command_prefix = "/") # appeler la fonction init de commands.bot


    async def on_ready(self):
        print(f"{self.user.dislpay_name} est connecté au serveur.") # récupère l'utilisateur du bot est affiche le nom


# intéragir
# @client.event
# async def on_member_join(member):
#     general_channel: discord.TextChannel = client.get_channel(1126973686444998819)
#     await general_channel.send(content=f"Bienvenue au seerveur {member.display_name} !")


# @client.event
# async def on_message(message):
#     if message.content.startswitch("!del"):
#         number = int(message.content.split()[1])
#         messages = await message.channel.history(limit = number + 1).flatten()

#         for each_message in messages:
#             await each_message.delete()


@bot.comand(name='del')
async def delete(ctx, number_of_messages: int): # ctx = contexte dans lequel est posté la commande
    messages = await ctx.channel.history(limit = number_of_messages + 1).flatten()

    for each_message in messages:
        await each_message.delete()

doc_bot = DocBot()
doc_bot.run(os.getenv("TOKEN"))