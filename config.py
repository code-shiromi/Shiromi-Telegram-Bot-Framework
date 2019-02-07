# config.py - Bot Config
# ShiroFramework 1.0
from configparser import SafeConfigParser
from telegram.ext import Updater
import json
#import gettext

# Get Bot informations
def GetBotUsername():
	botUsername = botcfg['botUsername']
	botName = botcfg['botName']
	return botUsername, botName

def botCredit():
	botId = int(botcfg['botId'])
	ownId = int(botcfg['ownerId'])
	return botId, ownId

# Connect Telegram Notify Channel
def botNotify():
	notiId = int(botcfg['notifyChannelId'])
	return notiId

# Connenet Telegram Media Save Channel
def botMediaBox():
	mbId = int(botcfg['MediaBoxId'])
	return mbId

# Connect Telegram bot with bot token
def botConnect():
	token = botcfg['token']
	updater = Updater(token)
	# Get the dispatcher to register handlers
	return updater

# Connect MySQL Database
def dbConnect():
	pass

# Getting Bot Config Data
def getBotOption():
	with open('config.json','r') as botConfig:
		global debug, version, date, botcfg, dbcfg
		settings = json.load(botConfig)
		debug = settings['DEBUG']
		version = settings['VERSION']
		date = settings['DATE']
		botcfg = settings['BOTDATA']
		dbcfg = settings['DBCONFIG']
		return debug, version, date, botcfg, dbcfg

# Load Bot Data
DEBUG = getBotOption()[0]
VERSION = version
DATE = date
BOT_USERNAME = GetBotUsername()[0]
BOT_NAME = GetBotUsername()[1]
BOT_ID = botCredit()[0]
OWNER_ID = botCredit()[1]
NOTIFY_ID = botNotify()
MEDIA_BOX_ID = botMediaBox()