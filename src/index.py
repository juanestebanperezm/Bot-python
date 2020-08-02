import discord
from discord.ext import commands
import datetime
from urllib import parse,request
import re

#COMANDO DE RESPUESTA EN ESTE CASO USAMOS ">" escribimos PING y el devolvera PONG
bot=commands.Bot(command_prefix='>',description="Helper bot")

@bot.command()

async def ping(ctx):
    await ctx.send('pong')

""" 
SUMA EN ESTE CASO USAMOS ">" y solo texteamos los 2 numeros que 
queremos que sean sumados en el servidor de discord """


@bot.command()

async def sum (ctx,num1:int,num2:int):
    await ctx.send(num1+num2)


#ESTADISTICAS DEL BOT y envio de mensajes

@bot.command()

async def info(ctx):
    embed=discord.Embed(title=f"{ctx.guild.name}", description="Este es un servidor de testeo",timestamp=datetime.datetime.utcnow(),color=discord.Color.blue())
    embed.add_field(name="Fecha de creacion",value=f"{ctx.guild.created_at}")
    embed.add_field(name="Dueño del servidor",value=f"{ctx.guild.owner}")
    embed.add_field(name="Region del servidor",value=f"{ctx.guild.region}")
    embed.add_field(name="ID",value=f"{ctx.guild.id}")
    embed.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftutorialedge.net%2Fimages%2Flogo-python.png&f=1&nofb=1")
    await ctx.send(embed=embed)


#CONSULTAS EN YOUTUBE

@bot.command()

async def youtube(ctx,*,search):
    query_string=parse.urlencode({'search_query':search})
    html_content=request.urlopen('http://www.youtube.com/results?' + query_string)
    resultado=re.findall('href=\"\\/watch\\?v=(.{11})',html_content.read().decode())
    #print(resultado)
    await ctx.send('https://youtube.com/watch?v='+resultado[0])


#Evento
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name='GTA 5',url="http://www.twitch.tv/accountname"))
    print("Bot listo")


bot.run('NzA3Mjg5ODE4MDU2NjIyMTMz.XrGo_g.BObFeSgH9WrCf5iSGhqGV-hMnfA')
