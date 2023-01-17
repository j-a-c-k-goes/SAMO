# main.py
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import random
import datetime
import phrase
import word

# Setup to go-to Server
load_dotenv()
BOT_NAME = os.getenv( 'BOT_NAME' )
SERVER_NAME = os.getenv( 'SERVER_NAME' )
TOKEN = os.getenv( 'BOT_TOKEN' )
SERVER = os.getenv( 'SERVER_ID' )
LIVE_CHANNEL = os.getenv( 'GENERAL_CHANNEL' )
TEST_CHANNEL = os.getenv( 'TEST_CHANNEL' )
PERMISSION = os.getenv( 'PERMISSIONS' )

# Create Client Instance
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client( intents=intents ) 

# Handle Connect
@client.event
async def on_ready( ):
	''' SAMO® Bot has connected '''
	print( f'{ BOT_NAME } live @ { SERVER_NAME }' )

# Acknowledge Typing
@client.event
async def on_typing( channel, user, when ):
    message_author = user
    message_channel = channel
    print( f'{ user } typing is { channel } — { when } ' )

# Handle Message
@client.event
async def on_message( message ):
	import time
	import random
	minute = datetime.datetime.today().minute
	if minute % 2 == 0:
		responses = [ 
		    phrase.tag( phrase.random_chars(random.randint(2,3) ) ),
		    phrase.tag( phrase.increasing_word_length(2, random.randint(3,14) ) )
		]
	elif minute % 2 == 1:
		responses = [
		    phrase.tag( phrase.reverse(phrase.random_chars(random.randint(2,3) ) )),
		    phrase.tag( phrase.decreasing_word_length(2, random.randint(3,14) ) )
		]
	triggers = ( message.content ==  'SAMO'.upper() ) or ( message.content ==  'SAMO'.lower() )
	if triggers:
		await message.channel.send( random.choice(responses) )

# Handle Disconnect
@client.event
async def on_disconnect():
   ''' SAMO® Bot has disconnected. '''
   print( f'{ BOT_NAME } booting down. see you next time.' )

# Run Bot.
client.run( TOKEN )