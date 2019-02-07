# response.py - Bot Response
# ShiroFramework 1.0
import config
from functions import log, handlers, botFunc
from telegram.ext import dispatcher

def botActive():
    # Active Logging
    log.logActive(config.DEBUG)
    # Get Bot connection
    updater = config.botConnect()
    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    # Get Message handlers
    handlers.msgs(dp)
    # Start the Bot
    updater.start_polling()
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()