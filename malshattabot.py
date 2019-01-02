#!/usr/bin/env python3
# Based on: https://www.devdungeon.com/content/make-discord-bot-python


import discord 
import urllib.request
import urllib.parse



# USER SET VARIABLES
TOKEN = 'INSERT_YOUR_TOKEN' # Token for the Bot itself
call_bot = "!malshattur" # What to say to call the bot to action


# Program Variables
client = discord.Client()
url = "http://malshaettir.gbit.is"



# Call the API
def get_response():
	f = urllib.request.urlopen(url)
	response = f.read().decode('utf-8')
	return response



@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith(call_bot):
		msg = get_response() 
		msg = ' {0.author.mention}: ' + msg # Comment out this line to skip user mention
		msg = msg.format(message)
		await client.send_message(message.channel, msg)



@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

client.run(TOKEN)
