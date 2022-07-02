import discord
from discord.ext import commands, tasks
from py1337x import py1337x
import json
import requests

intents = discord.Intents().all()
client = commands.Bot(command_prefix='!', intents=intents)

torrent = py1337x(proxy='1337x.to', cache='imp\cache', cacheTime=500)




@client.event
async def on_ready():
    print("up")



# print(jsondata['items'][1]['torrentId'])
@client.command()
async def get(ctx,*,torrentx):
    data = torrent.search(torrentx)
    print(data)
    if IndexError:
        await ctx.send("No torrents found")
    else:
        name = data['items'][0]['name']
        id = data['items'][0]['torrentId']
        info = torrent.info(f'https://www.1337xx.to/torrent/{id}/h9/')
        magnet = info['magnetLink']
        image = info['images'][0]
        link = data['items'][0]['link']
        seeders = data['items'][0]['seeders']
        leechers = data['items'][0]['leechers']
        size = data['items'][0]['size']
        time = data['items'][0]['time']
        uploader = data['items'][0]['uploader']
        uploaderlink = data['items'][0]['uploaderLink']
        if data['items']:
            r = requests.post("https://hastebin.com/documents", data=f"Copy And Paste this link below in new tab to start the download, Note: You must have a torrent downloader \n\n{magnet}").json()
            magnetlink = f"https://hastebin.com/raw/{r['key']}"
            embed = discord.Embed(title=f"1# {name}", url=link, description=f'Seeders: {seeders} | Leechers: {leechers} | Size: {size} | Time: {time} | Uploader: {uploader} | Uploader Link: {uploaderlink} \n [Magnet Link]({magnetlink})', color=0x00ff00)
            if image:
                embed.set_image(url=image)
            else:
                pass
            await ctx.send(embed=embed)
            print(magnet)
        else:
            await ctx.send('No torrent found')
        

client.run("token")