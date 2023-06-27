from javascript import require, On, Once

import sys

import json

mineflayer = require('mineflayer')

data = json.loads(open("config.json", "r").read())

file_paths = sys.argv[1]

bot = mineflayer.createBot({i: data[i] for i in data.keys() if data[i]})

@Once(bot, "spawn")
def spawn(*garbage):
    data = json.loads(open(file_paths, "r").read())
    block = "minecraft:glowstone"
    @On(bot, 'chat')
    def onChat(this, user, message, *rest):
        for x, z in data["coords"]:
            bot.chat(f"/setblock ~{x} ~ ~{z} {block}")