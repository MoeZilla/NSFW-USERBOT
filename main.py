import os
from pyrogram import Client, filters
import rapidjson as json
import requests
import time

StartTime = time.time()


API_ID = os.environ.get("API_ID", None) 
API_HASH = os.environ.get("API_HASH", None) 
SESSION = os.environ.get("SESSION", None) 
PREFIX = os.environ.get("PREFIX", None) 


app = Client(
      session_name=SESSION,
      api_id=API_ID,
      api_hash=API_HASH,
)

REPOLINK = """ Source code: [Github](https://github.com/Moezilla/vc-userbot)
License: [ GPL-3.0 License](https://github.com/moezilla/vc-userbot/blob/master/LICENSE.md)"""

@app.on_message(filters.command("repo", PREFIX))
async def repo(_, message):
    await message.reply_text(REPOLINK)


@app.on_message(filters.command("smug", PREFIX))
def smug(_, message):
    smug = requests.get("https://nekos.life/api/v2/img/smug").json()
    smug = url.get("smug")
    message.reply_video(smug)

@app.on_message(filters.command("solog", PREFIX))
def solog(_, message):
    solog = requests.get("https://nekos.life/api/v2/img/solog").json()
    solog = url.get("solog")
    message.reply_video(solog)

@app.on_message(filters.command("neko", PREFIX))
def neko(_, message):
    neko = requests.get("https://nekos.life/api/v2/img/neko").json()
    neko = url.get("neko")
    message.reply_photo(neko)

@app.on_message(filters.command("feet", PREFIX))
def feet(_, message):
    feet = requests.get("https://nekos.life/api/v2/img/feet").json()
    feet = url.get("feet")
    message.reply_photo(feet)


@app.on_message(filters.command("yuri", PREFIX))
def yuri(_, message):
    yuri = requests.get("https://nekos.life/api/v2/img/yuri").json()
    yuri = url.get("yuri")
    message.reply_photo(yuri)

@app.on_message(filters.command("trap", PREFIX))
def trap(_, message):
    trap = requests.get("https://nekos.life/api/v2/img/trap").json()
    trap = url.get("trap")
    message.reply_photo(trap)

@app.on_message(filters.command("futanari", PREFIX))
def futanari(_, message):
    futanari = requests.get("https://nekos.life/api/v2/img/futanari").json()
    futanari = url.get("futanari")
    message.reply_photo(futanari)

@app.on_message(filters.command("hololewd", PREFIX))
def hololewd(_, message):
    hololewd = requests.get("https://nekos.life/api/v2/img/hololewd").json()
    hololewd = url.get("hololewd")
    message.reply_photo(hololewd)

@app.on_message(filters.command("lewdkemo", PREFIX))
def lewdkemo(_, message):
    lewdkemo = requests.get("https://nekos.life/api/v2/img/lewdkemo").json()
    lewdkemo = url.get("lewdkemo")
    message.reply_photo(lewdkemo)

@app.on_message(filters.command("sologif", PREFIX))
def solog(_, message):
    solog = requests.get("https://nekos.life/api/v2/img/solog").json()
    solog = url.get("solog")
    message.reply_video(solog)

@app.on_message(filters.command("feetgif", PREFIX))
def feetg(_, message):
    feetg = requests.get("https://nekos.life/api/v2/img/feetg").json()
    feetg = url.get("feetg")
    message.reply_video(feetg)
