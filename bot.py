import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix = ">")

trigger_words = [
                    "i love u", 
                    "i love you",
                    "i lobe u",
                    "i lobe you"
                ]

images = {
            "First time I got really emotional for you" : "https://imgur.com/4A3CBod.jpg",
            "Your first time sharing a photo of yours" : "https://imgur.com/zoj0piK.jpg",
            "Guessed that your voice is cute" : "https://imgur.com/LpEonOm.jpg",
            "Finally asking you the most important question of my life" : "https://imgur.com/ZKH1pqZ.jpg",
            "One of the cutest moments of ours" : "https://imgur.com/OegdmsD.jpg",
            "The only time we didn't made a 'top' joke XD" : "https://imgur.com/fiF1hqS.jpg",
            "First time we told eachother our names" : "https://imgur.com/07i6pJi.jpg",
            "YOU SAID YES" : "https://imgur.com/7YxvTYY.jpg",
            "Someone complimented me for the first time" : "https://imgur.com/BTLs5A0.jpg",
            "One of the cutest thing anyone ever said to me" : "https://imgur.com/nR7aUS2.jpg",
            "Typical you being a badass" : "https://imgur.com/Fh4fxca.jpg",
            "You perfectly described me even tho we met 2 days ago": "https://imgur.com/3BEaeQK.jpg",
            "You melted my heart in seconds" : "https://imgur.com/SgSIrKh.jpg",
            "You trusted me and shared ur feelings with me" : "https://imgur.com/w3A03M7.jpg"
         }

@client.event
async def on_ready():
    print("bot is ready")

@client.event
async def on_message(msg):
    message = msg.content
    for words in trigger_words:
        if words in message.lower():
            title = random.choice(list(images))
            embed = discord.Embed(title = title, color = discord.Colour.purple())
            embed.set_image(url = images[title])
            await msg.channel.send(embed = embed)

    await client.process_commands(msg)

@client.command()
async def love(ctx):
    title = random.choice(list(images))
    embed = discord.Embed(title = title, color = discord.Colour.purple())
    embed.set_image(url = images[title])
    await ctx.send(embed = embed)

client.run("Nzk4MDM5ODMxOTEyOTA2NzYz.X_vOgg.GlzZM_Dq73lb3zZBSlHl3yQM9Kg")
