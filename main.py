mytitle = "Discord Sunucu Kopyalam -Client"
from os import system
system("title "+mytitle)
import psutil
from pypresence import Presence
import time
import sys
client_id = 'Your Account ID'
import discord
import asyncio
import colorama
from colorama import Fore, init, Style
import platform
from serverclone import Clone

client = discord.Client(intents=discord.Intents.default())
os = platform.system()
if os == "Windows":
    system("cls")
else:
    system("clear")
    print(chr(27) + "[2J")
print(f"""{Fore.GREEN}
   ____ _ _            _   
  / ___| (_) ___ _ __ | |_ 
 | |   | | |/ _ \ '_ \| __|
 | |___| | |  __/ | | | |_ 
  \____|_|_|\___|_| |_|\__|
                                                                      
{Style.RESET_ALL}
{Fore.YELLOW}> Discord{Style.RESET_ALL}
{Fore.YELLOW}> https://discord.gg/3Zu6RQCyk8 - https://discord.gg/rK9KvTYnfS{Style.RESET_ALL}
        """)


token = input(f'Token Giriniz:\n >')
guild_s = input('Kopyalanmasını istediğiniz sunucunun ID''si:\n >')
guild = input('Kopyalamanın aktarılacağı sunucunun ID''si:\n >')
input_guild_id = guild_s  # <-- input guild id
output_guild_id = guild  # <-- output guild id
token = token  # <-- your Account token


print("  ")
print("  ")

@client.event
async def on_ready():
    extrem_map = {}
    print(f"Giriş Yapılan Hesap: {client.user}")
    print("Sunucu Kopyalanıyor")
    guild_from = client.get_guild(int(input_guild_id))
    guild_to = client.get_guild(int(output_guild_id))
    await Clone.guild_edit(guild_to, guild_from)
    await Clone.roles_delete(guild_to)
    await Clone.channels_delete(guild_to)
    await Clone.roles_create(guild_to, guild_from)
    await Clone.categories_create(guild_to, guild_from)
    await Clone.channels_create(guild_to, guild_from)
    print(f"""{Fore.GREEN}


  _  _____  ______   __ _    _        _    _   _ ____ ___ 
 | |/ / _ \|  _ \ \ / // \  | |      / \  | \ | |  _ \_ _|
 | ' / | | | |_) \ V // _ \ | |     / _ \ |  \| | | | | | 
 | . \ |_| |  __/ | |/ ___ \| |___ / ___ \| |\  | |_| | | 
 |_|\_\___/|_|    |_/_/   \_\_____/_/   \_\_| \_|____/___|
                                                                               


    {Style.RESET_ALL}""")
    await asyncio.sleep(5)
    client.close()


client.run(token, bot=False)
