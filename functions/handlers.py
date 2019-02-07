# handlers.py - Bot Handler list
# ShiroFramework 1.0
from functions import botFunc, log
from telegram.ext import Filters, CommandHandler, MessageHandler

def msgs(dp):
    # on different commands
    dp.add_handler(CommandHandler("start", botFunc.start))
    dp.add_handler(CommandHandler("help", botFunc.help))
    dp.add_handler(CommandHandler("set", botFunc.set_timer,
                                  pass_args=True,
                                  pass_job_queue=True,
                                  pass_chat_data=True))
    dp.add_handler(CommandHandler("unset", botFunc.unset, pass_chat_data=True))
    # on noncommand i.e message
    dp.add_handler(MessageHandler(Filters.text, botFunc.getTextMsg))
    # log all errors
    dp.add_error_handler(log.error)