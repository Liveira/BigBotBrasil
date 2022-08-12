from io import BytesIO
from math import trunc
import math
from operator import truediv
from discord import file
from discord.ext.commands.converter import _Greedy
from discord.flags import Intents
import requests
import typing
from PIL import Image as img, ImageDraw
from PIL import ImageFont as imgfont
from PIL import ImageDraw as imgdraw
from PIL import ImageOps
import discord,json,asyncio,random,textwrap
from discord.ext import commands,tasks
config = json.loads(open("config.json",'r').read())
def one(url,text):
    a = img.new("RGBA",(1280,720))
    _ = img.open("./imgs/1o.png")
    _ = _.copy()
    draw = imgdraw.Draw(a)
    a.paste(_,(0,0))
    #282²
    b = img.open(BytesIO(requests.get(url[0]).content))
    b = b.resize((282,282))
    b.copy()
    a.paste(b,(505,97))
    font = imgfont.truetype("COMIC.TTF",49)
    draw.text((1280/2,503),textwrap.fill(text,35),fill=(255,255,255),font=font,anchor='mm',align='center')
    a.save("fodase.png")
    return discord.File("fodase.png")
def two(url,text):
    a = img.new("RGBA",(1280,720))
    _ = img.open("./imgs/2o.png")
    _ = _.copy()
    draw = imgdraw.Draw(a)
    a.paste(_,(0,0))
    #282²
    b = img.open(BytesIO(requests.get(url[0]).content))
    c = img.open(BytesIO(requests.get(url[1]).content))
    b = b.resize((282,282))
    b = b.copy()
    a.paste(b,(360,97))
    c = c.resize((282,282))
    c = c.copy()
    a.paste(c,(655,97))
    font = imgfont.truetype("COMIC.TTF",49)
    draw.text((1280/2,503),textwrap.fill(text,35),fill=(255,255,255),font=font,anchor='mm',align='center')
    a.save("fodase.png")
    return discord.File("fodase.png")
def three(url,text):
    a = img.new("RGBA",(1280,720))
    _ = img.open("./imgs/2o.png")
    _ = _.copy()
    draw = imgdraw.Draw(a)
    a.paste(_,(0,0))
    #282²
    b = img.open(BytesIO(requests.get(url[0]).content))
    c = img.open(BytesIO(requests.get(url[1]).content))
    d = img.open(BytesIO(requests.get(url[2]).content))
    b = b.resize((282,282))
    b = b.copy()
    a.paste(b,(210,97))
    c = c.resize((282,282))
    c = c.copy()
    a.paste(c,(505,97))
    d = d.resize((282,282))
    d = d.copy()
    a.paste(d,(805,97))
    font = imgfont.truetype("COMIC.TTF",49)
    draw.text((1280/2,503),textwrap.fill(text,35),fill=(255,255,255),font=font,anchor='mm',align='center')
    a.save("fodase.png")
    return discord.File("fodase.png")
def paredao(url):
    a = img.new("RGBA",(1280,720))
    _ = img.open("./imgs/paredao.png")
    _ = _.copy()
    draw = imgdraw.Draw(a)
    a.paste(_,(0,0))
    print(url)
    b = img.open(BytesIO(requests.get(url[0]).content))
    print("foi? kk")
    c = img.open(BytesIO(requests.get(url[1]).content))
    print("foi? kk 2")
    b = b.resize((282,282))
    b = b.copy()
    a.paste(b,(247,171))
    c = c.resize((282,282))
    c = c.copy()
    a.paste(c,(763,171))
    a.save("fodase.png")
    return discord.File("fodase.png")
def lider(url,text):
    a = img.new("RGBA",(1280,720))
    _ = img.open("./imgs/lider.png")
    _ = _.copy()
    draw = imgdraw.Draw(a)
    a.paste(_,(0,0))
    #282²
    b = img.open(BytesIO(requests.get(url).content))
    b = b.resize((282,282))
    b.copy()
    a.paste(b,(134,194))
    font = imgfont.truetype("COMIC.TTF",44)
    draw.text((448,193),text[0],fill=(255,255,255),font=font,align='left')
    draw.text((448,269),text[1],fill=(255,255,255),font=font,align='left')
    draw.text((448,341),text[2],fill=(255,255,255),font=font,align='left')
    draw.text((448,420),text[3],fill=(255,255,255),font=font,align='left')
    a.save("lider.png")
    return discord.File("lider.png")
def eliminado(url,text):
    #416
    #406
    a = img.new("RGBA",(1280,720))
    _ = img.open("./imgs/eliminado.png")
    _ = _.copy()
    draw = imgdraw.Draw(a)
    a.paste(_,(0,0))
    #282²
    b = img.open(BytesIO(requests.get(url).content))
    b = b.resize((282,282))
    b.copy()
    a.paste(b,(505,97))
    font = imgfont.truetype("COMIC.TTF",49)
    draw.text((1280/2,416),textwrap.fill(text+" foi eliminado!",35),fill=(255,255,255),font=font,anchor='mm',align='center')
    a.save("fodase.png")
    return discord.File("fodase.png")
def win(url,text):
    #416
    #406
    a = img.new("RGBA",(1280,720))
    _ = img.open("./imgs/WIN.png")
    _ = _.copy()
    draw = imgdraw.Draw(a)
    a.paste(_,(0,0))
    #282²
    b = img.open(BytesIO(requests.get(url).content))
    b = b.resize((282,282))
    b.copy()
    a.paste(b,(505,169))
    font = imgfont.truetype("COMIC.TTF",60)
    draw.text((1280/2,475),textwrap.fill(text+" Ganhou o BBBot!",35),fill=(255,255,255),font=font,anchor='mm',align='center')
    a.save("fodase.png")
    return discord.File("fodase.png")
def get():
    return json.load(open("database.json",'r',encoding="utf8"))
def addDev(id):
    try:_ = json.load(open("config.json","r"));_["DEVS"].append(id.id);json.dump(_,open("config.json","w"));return True
    except Exception as ex: return False

locais = ["na sala de estar","no porão","na piscina","no quarto","na cozinha","no sótão","no banheiro","em uma sala escondida"]
def checkMS(author,messagecheck,channel):
    def inner_check(message):
        if message.author == author:
            if message.channel == channel:
                if message.content.lower() == messagecheck or message.content.lower() in messagecheck: return True
                else: return False
jogos = {}
bot = commands.Bot(command_prefix="bbb?",intents=Intents.all())
bot.remove_command("help")
def random_(lista: list,quant:int,blacklist = None) -> list:
    _ = []
    for i in range(quant):
        a = random.choice(lista)
        while a in _ or a == blacklist:
            a = random.choice(lista)
        _.append(a) 
    return _       
async def go(guild: int):
    game = jogos[str(guild)]
    a = bot.get_channel(game['channel_id'])
    if game['dia'] == 7:
        EMPATE = False
        if jogos[str(guild)]['paredao'] != []:
            if jogos[str(guild)]['manual']:
                x = 0
                z = 0
                M = await a.fetch_message(jogos[str(guild)]['posvote'].id)
                async for i in M.reactions[0].users():
                    x += 1
                async for i in M.reactions[1].users():
                    z += 1
                if x > z:
                    perdedor = jogos[str(guild)]['paredao'][0]
                elif z > x:
                    perdedor = jogos[str(guild)]['paredao'][1]
                else:
                    perdedor = random.choice(jogos[str(guild)]['paredao'])
                    EMPATE = True
                if EMPATE:
                    embed = discord.Embed(title='Paredão Big Bot Brasil',description=f"> **Houve um empate nos votos! Os dois estavam com a mesma quantidade de votos, então vai ser aleatório!**\n\nInfelizmente (Ou felizmente) **{perdedor}** saiu do Big Bot Brasil :sob:...",color=discord.Color.random())
                    eliminado(game["participantes"][perdedor]["user"].avatar_url,perdedor)
                else:
                    embed = discord.Embed(title='Paredão Big Bot Brasil',description=f"> **{jogos[str(guild)]['paredao'][0]}** Teve {x} votos\n> **{jogos[str(guild)]['paredao'][1]}** Teve {z} votos\n\nInfelizmente (Ou felizmente) **{perdedor}** saiu do Big Bot Brasil :sob:...",color=discord.Color.random())    
                    eliminado(game["participantes"][perdedor]["user"].avatar_url,perdedor)
            
            else:
                perdedor = random.choice(jogos[str(guild)]['paredao'])
                #embed = discord.Embed(title='Paredão Big Bot Brasil',description=f"Infelizmente (Ou felizmente) **{perdedor}** saiu do Big Bot Brasil :sob:...",color=discord.Color.random())
                el = eliminado(game["participantes"][perdedor]["user"].avatar_url,perdedor)
            await a.send(file = el) 
            jogos[str(guild)]['paredao'] = []
            del jogos[str(guild)]['participantes'][perdedor]
            if len(jogos[str(guild)]['participantes']) == 1:
                #await a.send(embed = discord.Embed(title="FINAL!",description=f"> E o ganhador é... **{list(jogos[str(guild)]['participantes'].keys())[0]}**!\n\nObrigado por jogarem o BBB Bot brasil! Espero vocês na proxima...\n\n> A partida durou {int((((15 * 7) * jogos[str(guild)]['part_count']) / 60) / 60) } Horas e {int(((15 * 7) * jogos[str(guild)]['part_count']) / 60)} minutos!"))
                w = win(game["participantes"][list(jogos[str(guild)]['participantes'].keys())[0]]["user"].avatar_url,list(jogos[str(guild)]['participantes'].keys())[0])
                await a.send(file=w)
                jogos[str(guild)]["END"] = True
                return
        if len(jogos[str(guild)]['participantes']) <= 2:
            for i in jogos[str(guild)]['participantes']:
                jogos[str(guild)]['paredao'].append(i)
            if jogos[str(guild)]['voting']:
                print("sua pica ae")
                x = 0
                z = 0
                M = await a.fetch_message(jogos[str(guild)]['posvote'].id)
                async for i in M.reactions[0].users():
                    x += 1
                async for i in M.reactions[1].users():
                    z += 1
                if x > z:
                    perdedor = jogos[str(guild)]['paredao'][0]
                    ganhador = jogos[str(guild)]['paredao'][1]
                elif z > x:
                    perdedor = jogos[str(guild)]['paredao'][1]
                    ganhador = jogos[str(guild)]['paredao'][0]
                else:
                    perdedor = random.choice(jogos[str(guild)]['paredao'])
                    EMPATE = True
                if EMPATE:
                    embed = discord.Embed(title='Paredão Big Bot Brasil',description=f"> **Houve um empate nos votos! Os dois estavam com a mesma quantidade de votos, então vai ser aleatório!**\n\nInfelizmente (Ou felizmente) **{perdedor}** saiu do Big Bot Brasil :sob:...",color=discord.Color.random())
                    el = eliminado(game["participantes"][perdedor]["user"].avatar_url,perdedor)
                    await a.send(file = el)
                else:
                    embed = discord.Embed(title='Paredão Big Bot Brasil',description=f"> **{jogos[str(guild)]['paredao'][0]}** Teve {x} votos\n> **{jogos[str(guild)]['paredao'][1]}** Teve {z} votos\n\nInfelizmente (Ou felizmente) **{perdedor}** saiu do Big Bot Brasil :sob:...\n\n E o ganhador é... **{ganhador}**!\nObrigado por jogarem o BBB Bot brasil! Espero vocês na proxima...\n\n> A partida durou {int((((15 * 7) * jogos[str(guild)]['part_count']) / 60) / 60) } Horas e {int(((15 * 7) * jogos[str(guild)]['part_count']) / 60)} minutos!",color=discord.Color.random())    
                    el = eliminado(game["participantes"][perdedor]["user"].avatar_url,perdedor)
                    await a.send(file = el)
                    w = win(game["participantes"][ganhador]["user"].avatar_url,ganhador)
                    await a.send(file=w)
            if jogos[str(guild)]['manual']:
                _ = await a.send(embed=discord.Embed(title="Hora da votação!",description=f"Quem sairás? O {jogos[str(guild)]['paredao'][0]} ou o {jogos[str(guild)]['paredao'][1]}? **Só saberemos na próxima semana...**\n\n Enquanto isso... Votem na pessoa que você quer que saia! 1️⃣ Para o {jogos[str(guild)]['paredao'][0]} | 2️⃣ Para o {jogos[str(guild)]['paredao'][1]}"))
                jogos[str(guild)]['voting'] = True
                print(jogos[str(guild)]['voting'])
                await _.add_reaction("1️⃣")
                await _.add_reaction("2️⃣") 
                jogos[str(guild)]['posvote'] = _ 
                jogos[str(guild)]['dia'] = 1
                jogos[str(guild)]['semana'] += 1
                return
            else:
                #await a.send(embed=discord.Embed(title="Fim...",description=f"{random.choice(list(jogos[str(guild)]['participantes'].keys()))} ganhou o BBB! E a partida se finaliza por aqui...\n> A partida durou {int((((15 * 7) * jogos[str(guild)]['part_count']) / 60) / 60) } Horas e {int(((15 * 7) * jogos[str(guild)]['part_count']) / 60)} minutos!",color=discord.Color.random()))
                w = win(game["participantes"][list(jogos[str(guild)]['participantes'].keys())[0]]["user"].avatar_url,list(jogos[str(guild)]['participantes'].keys())[0])
                await a.send(file=w)
                jogos[str(guild)]['END'] = True
                return
        
        jogos[str(guild)]['lider'] = random.choice(list(game['participantes'].keys()))
        a_ = random_(get()["req"],4)
        b_ = random_(list(game['participantes'].keys()),2,jogos[str(guild)]['lider'])
        jogos[str(guild)]['paredao'] = b_
        jogos[str(guild)]['dia'] = 1
        jogos[str(guild)]['semana'] += 1
        #await a.send(embed=discord.Embed(title="Paredão Big Bot Brasil",description=f"{jogos[str(guild)]['semana']}º Semana... Falta {len(jogos[str(guild)]['participantes'])} participantes!\n\nLider do paredão: **{jogos[str(guild)]['lider']}**\n\nrequisitos:\n**{a_[0]}**\n**{a_[1]}**\n**{a_[2]}**\n**{a_[3]}**\n\nE quem está no paredão é... **{b_[0]}** e **{b_[1]}**! Um deles vai sair... Mas quem? ",color=discord.Color.random()))
        ld = lider(game["participantes"][jogos[str(guild)]['lider']]["user"].avatar_url, a_)
        pr = paredao([game["participantes"][b_[0]]["user"].avatar_url,game["participantes"][b_[1]]["user"].avatar_url])
        await a.send(file = ld)
        await a.send(file = pr)
        if jogos[str(guild)]["manual"]:
            _ = await a.send(embed=discord.Embed(title="Hora da votação!",description=f"Quem sairás? O {jogos[str(guild)]['paredao'][0]} ou o {jogos[str(guild)]['paredao'][1]}? **Só saberemos na próxima semana...**\n\n Enquanto isso... Votem na pessoa que você quer que saia! 1️⃣ Para o {jogos[str(guild)]['paredao'][0]} | 2️⃣ Para o {jogos[str(guild)]['paredao'][1]}"))  
            await _.add_reaction("1️⃣")
            await _.add_reaction("2️⃣")  
            jogos[str(guild)]['posvote'] = _
    else:
        fala = random.choice(list(get()["falas"].keys()))
        while get()["falas"][fala]['quant'] > len(game['participantes']) or get()["falas"][fala]['fala'] == jogos[str(guild)]['ultimafrase']:
            fala = random.choice(list(get()["falas"].keys())) 
        jogos[str(guild)]['ultimafrase'] = fala
        p = random_(list(game['participantes'].keys()),get()["falas"][fala]['quant'])
        sort = p
        if(get()["falas"][fala]['local']):
            sort.append(random.choice(locais))
        if get()["falas"][fala]['quant'] == 1:
             _a = one([game['participantes'][sort[0]]["user"].avatar_url],get()["falas"][fala]["fala"] % tuple(sort))
        elif get()["falas"][fala]['quant'] == 2:
            players = []
            for i in p:
                try:
                    players.append(game['participantes'][i]["user"].avatar_url)
                except:pass
            try:
                _a = two(players,get()["falas"][fala]["fala"] % tuple(sort))
            except TypeError:
                print(get()["falas"][fala]["fala"],sort)
        elif get()["falas"][fala]['quant'] == 3:
            players = []
            for i in p:
                try:
                    players.append(game['participantes'][i]["user"].avatar_url)
                except:pass
            try:
                _a = three(players,get()["falas"][fala]["fala"] % tuple(sort))
            except TypeError:
                print(get()["falas"][fala]["fala"],sort)
        #await a.send(embed=discord.Embed(title=f"Semana: {jogos[str(guild)]['semana']} | Dia: {jogos[str(guild)]['dia']}",description=get()["falas"][fala]['fala'] % tuple(sort),color=discord.Color.random()))
        await a.send(file=_a)
        jogos[str(guild)]['dia'] += 1
@tasks.loop(seconds=15)
async def loop():
    end = []
    for key in jogos:
        if not jogos[key]['END']:
            await go(key)
                
        else: end.append(key)
    for i in end:
        del jogos[i]
    end = [] 
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(jogos)} partidas de Big Bot Brasil! Use bbb?start para começar."))
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(jogos)} partidas de Big Bot Brasil! Use bbb?start para começar."))
    print("Estou ligado")
    loop.start()
@bot.command()
async def start(ctx,var: typing.Optional[str]="normal",parti: commands.Greedy[discord.User]=None):
    if not ctx.author.guild_permissions.manage_messages:
        if discord.utils.get(ctx.author.roles,name = "BBB Mod") == None: 
            await ctx.send("Você não tem permissão de gerenciar mensagens ou você não tem o cargo de \"BBB Mod\".")
            return
        else:
            pass
    if var == "all":
        parti = []
        for i in ctx.guild.members:
            if i.bot:continue
            parti.append(i)
    if parti == None and var == "normal":
        await ctx.send("Você precisa informar os jogadores... Você pode usar 'all' para todos os membros do servidor, ou marcando as pessoas!")
    if len(parti) <= 2:
        await ctx.send("Você precisa informar mais de 2 membros")
        return
    if str(ctx.guild.id) in jogos:
        await ctx.send("Uma partida está em andamento, encerre usando bbb?stop!")
    text = ""
    cont = 0
    for i in parti:
        cont += 1    
        text += f'**{i.name}**{", " if not parti[len(parti)-1] == i else ""}'
        if cont == 15:
            text += "**etc...**"
            break
    await ctx.send(f"Participantes: {text}... Você deseja continuar?")
    try:
        alt = ["sim","mas é claro","claro","s",'obvio caralho','ss','sss','ssim']
        msg = await bot.wait_for('message', check=lambda message: message.author == ctx.author and message.content.lower() in alt and message.channel == ctx.channel,timeout=15)
        await ctx.send(f"Votos manuais ou aleatórios? **Sim para manual, e não para aleatório**")
        msg = await bot.wait_for('message', check=lambda message: message.author == ctx.author and message.content.lower() in ["sim","não"] and message.channel == ctx.channel,timeout=15)

        await ctx.send(f"Jogo iniciado com {len(parti)} participantes!")
        jogos[str(ctx.guild.id)] = {
            "participantes":{
                x.name : {
                    "amigos":{},
                    "inimigos":{},
                    "relacao":{},
                    "user": x
                } for x in parti  
            },
            "semana":1,
            "dia":1,
            "paredao":[],
            "manual": True if msg.content == "sim" else False,
            "part_count":len(parti),
            'voting':False,
            'passagem':0,
            'posvote':False,
            'END':False,
            'channel_id':ctx.channel.id,
            'ultimafrase':""
        }
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(jogos)} partidas de Big Bot Brasil! Use bbb?start para começar."))
    except asyncio.TimeoutError:    
        await ctx.send("Tempo excedido...")
@bot.command()
async def stop(ctx):
    if not ctx.author.guild_permissions.manage_messages:
        if discord.utils.get(ctx.author.roles,name = "BBB Mod") == None: 
            await ctx.send("Você não tem permissão de gerenciar mensagens ou você não tem o cargo de \"BBB Mod\".")
            return
        else:
            pass
        
    if str(ctx.guild.id) not in jogos:
        await ctx.send("Não tem como encerrar um jogo que nunca começou")
        return
    else:
        jogos[str(ctx.guild.id)]["END"] = True
        await ctx.send("OK! Jogo encerrado.")
@bot.command()
async def help(ctx):
    await ctx.send(embed=discord.Embed(title='Ajuda',description='Use bbb?start <membro 1> <membro 2> <membro 3> | Só é permitido mais de 2 membros e menor que 32!\nUse bbb?stop para parar uma partida de BBB!\n\nA ideia principal do bot veio de um site de simulação de BBB! https://virgula.itch.io/irmao-grande'))
@bot.command()
async def sylveongostosa(ctx,dev: discord.User):
    if ctx.author.id in json.load(open("config.json","r"))["DEVS"]:
        if dev.id in json.load(open("config.json","r"))["DEVS"]: await ctx.send("Ele já é dev esquizofrenico do caralho")
        else: await dev.send("Você entrou na whitelist de devs!") if addDev(dev) else await ctx.send("deu ruim") 
    else: 
        await ctx.send("https://cdn.discordapp.com/attachments/882281519064952922/903778870078087198/FB_IMG_1635474410768.jpg")
@bot.command()
async def addf(ctx):
    if ctx.author.id in json.load(open("config.json","r"))["DEVS"]:
        def check_(author,message,messr):
            def inner_check(reaction, author):
                return message.author == author and messr == reaction.message and reaction.emoji == "✅"
            return inner_check
        def check(author):
            def inner_check(message):
                return message.author == author 
            return inner_check
        embed = discord.Embed(title='Adicionar frase ao BBB BOT')
        embed.add_field(name="Regras",value="**1** - Certifique-se que a frase que você colocou está sem nenhum erro (*slk mo trampo pra tirar dps kk*)\n**2** - Sem shitpost... (*sim sem shitpost kkk, tenta colocar algo na zueira mas calma la ne amigao*)\n**3** - Sem NSFW explícito kkk (*sylveon transando n vai cair mt bem n*)")
        embed.add_field(name="Observações Importantes",value="> **Você só poderar colocar no máximo 3 nomes**\n\n> **No lugar do nome você usa '\%s' por exemplo (\%s fez uma baderna)**\n\n> **Caso sua frase tenha um local tu usa o '\%s' também, pois, só pode ser usado no ultimo '\%s' por exemplo... '\%s bateu uma \%s' (Obs: não precisa colocar 'no' 'na' 'em' e etc... Ele já coloca sozinho xD )**\n\n> **Tu só pode citar o nome de uma pessoa 1 vez, não pode repetir o mesmo nome na mesma frase... por exemplo, Matsuky comeu um bolo, mas Matsuky passou mal**")
        embed.set_author(name='Caso concorde com as regras reaja ✅')
        a = await ctx.send(embed=embed)
        await a.add_reaction("✅")
        a = await bot.wait_for('reaction_add',check=check_(ctx.author,ctx.message,a), timeout=60)
        await ctx.send("> Quantas pessoas vão aparecer? (Máximo de 3)")
        qnt_pessoas = await bot.wait_for('message',check=check(ctx.author), timeout=60)
        if int(qnt_pessoas.content) > 3:
            await ctx.send("tu é cego ou oq?")
            return
        await ctx.send(f"Quantidade de pessoas: **{qnt_pessoas.content}**\n\n> Digite sua frase")
        frase = await bot.wait_for('message',check=check(ctx.author), timeout=60)
        await ctx.send(f"Quantidade de pessoas: **{qnt_pessoas.content}**\nFrase: **{frase.content.replace('%s','pessoa')}**\n\n> Sua frase tem sistema de locais? Se sim digite tem, se não, digite não.")
        h = await bot.wait_for('message',check=check(ctx.author), timeout=60)
        if h.content.lower() == "tem": h = True
        elif h.content.lower() == "não": h = False
        else: await ctx.send("O ARROMBADO, É TEM OU NÃO. SIFUDE MN")
        a = get()
        import random
        a["falas"][f"{random.randrange(0,100000)}"] = {
            "fala":frase.content,
            "quant":int(qnt_pessoas.content),
            "local":h
        }
        json.dump(a,open("database.json","w"),indent=4)
        await ctx.send(f"A frase foi colocada com sucesso na database | Index: **{len(get()['falas'])}**")
    else: 
        await ctx.send("https://cdn.discordapp.com/attachments/882281519064952922/903778870078087198/FB_IMG_1635474410768.jpg")
@bot.command()
async def listarfrases(ctx,pag=1):
    a = "```"
    c = (pag * 10) - 10
    _ = []
    __ = get()["falas"]
    for i in get()["falas"]:
        _.append(i)
    for i in range(10):
        try:
            a += f"\n{c+1} - {__[_[c]]['fala']}"
            c += 1
        except IndexError: break
    a += "\n```"
    a = discord.Embed(title='Todas as frases do BBB Bot.',description=a)
    a.set_footer(text=f"Pagina {pag}/{math.ceil(len(__)/10)}")
    await ctx.send(embed=a)
@bot.command()
async def addr(ctx,*,frase):
    a = get()
    a["req"].append(frase)
    await ctx.send(f"Frase adicionada! Index: **{len(a['req'])}**")
    json.dump(a,open("database.json","w"))
@bot.command()
async def listarreq(ctx,pag=1):
    a = "```"
    c = (pag * 10) - 10
    __ = get()["req"]
    for i in range(10):
        try:
            a += f"\n{c+1} - {__[c]}"
            c += 1
        except IndexError: break
    a += "\n```"
    a = discord.Embed(title='Todas os requisitos do BBB Bot.',description=a)

    a.set_footer(text=f"Pagina {pag}/{math.ceil(len(__)/10)}")
    await ctx.send(embed=a)
@bot.command()
async def cu(ctx):
    await start(ctx,bot.get_user(297153970613387264),bot.get_user(715637208140218390),bot.get_user(798687278263304254))
bot.run(config['TOKEN'])
