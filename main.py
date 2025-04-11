import discord
import colorama
import asyncio
from discord.ext import commands, tasks
from datetime import datetime
from colorama import init, Fore

colorama.init()

LGREEN = Fore.LIGHTGREEN_EX
LMAGENTA = Fore.LIGHTMAGENTA_EX
LBLUE = Fore.LIGHTBLUE_EX
WHITE = Fore.WHITE
LYELLOW = Fore.LIGHTYELLOW_EX

if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

target_role_id = YOUR_TARGET_ROLE_ID
bot_role_id = YOUR_BOT_ROLE_ID

def current_time() -> str:
    return datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

@bot.event
async def on_ready():
    print(f"{current_time()} {LGREEN}Logged in as {LMAGENTA}{bot.user}{WHITE}")
    check_roles.start()

@bot.event
async def on_member_join(member):
    if not any(role.id == bot_role_id for role in member.roles):
        role = discord.utils.get(member.guild.roles, id=target_role_id)
        if role and role not in member.roles:
            await member.add_roles(role)
            print(f"{current_time()} Assigned role {LBLUE}{role.name} {WHITE}to {LYELLOW}{member.name}{WHITE}")

@tasks.loop(seconds=300)
async def check_roles():
    for guild in bot.guilds:
        for member in guild.members:
            if not any(role.id == bot_role_id for role in member.roles):
                role = discord.utils.get(guild.roles, id=target_role_id)
                if role and role not in member.roles:
                    await member.add_roles(role)
                    print(f"{current_time()} Assigned role {LBLUE}{role.name} {WHITE}to {LYELLOW}{member.name}{WHITE}")

bot.run("BOT TOKEN")
