import requests
import json
import time
import discord

start_time = time.time()

def get_meme():
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']

def get_joke():
    response = requests.get('https://v2.jokeapi.dev/joke/Any')
    json_data = json.loads(response.text)
    if json_data['type'] == 'single':
        return json_data['joke']
    else:
        return f"{json_data['setup']} ... {json_data['delivery']}"
    
def get_quote():
    response = requests.get('https://api.quotable.io/random')
    json_data = json.loads(response.text)
    return f"{json_data['content']} — {json_data['author']}"
    
def get_uptime():
    current_time = time.time()
    uptime = current_time - start_time
    minutes, seconds = divmod(uptime, 60)
    hours, minutes = divmod(uptime, 60)
    return f"Bot has been for {int(hours)} hours, {int(minutes)} minutes, and {int(seconds)} seconds."

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
    
    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Hello World!')
        
        if message.content.startswith('$meme'):
            await message.channel.send(get_meme())
        
        if message.content.startswith('$joke'):
            await message.channel.send(get_joke())

        if message.content.startswith('$uptime'):
            await message.channel.send(get_uptime())
        
        if message.content.startswith('$quote'):
            await message.channel.send(get_quote())

        

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('')

