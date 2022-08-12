import discord
from discord.ext import commands
from ..main import *

class Reality(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
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


        @commands.command(name = "",
                        usage="<usage>",
                        description = "description")
        @commands.guild_only()
        @commands.has_permissions()
        @commands.cooldown(1, 2, commands.BucketType.member)
        async def commandName(self, ctx:commands.Context):
            await ctx.send("template command")


def setup(bot:commands.Bot):
    bot.add_cog(Reality(bot))