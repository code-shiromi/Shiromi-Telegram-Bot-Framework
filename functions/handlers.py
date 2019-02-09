# handlers.py - Bot Handler list
# ShiroFramework 1.0
from functions import botFunc, log
from telegram.ext import Filters, CommandHandler, MessageHandler

def msgs(dp):
    # on different commands
    dp.add_handler(CommandHandler("start", botFunc.start))
    dp.add_handler(CommandHandler("help", botFunc.help))
    dp.add_handler(CommandHandler("query", botFunc.query))
    dp.add_handler(CommandHandler("set", botFunc.set_timer,
                                  pass_args=True,
                                  pass_job_queue=True,
                                  pass_chat_data=True))
    dp.add_handler(CommandHandler("unset", botFunc.unset, pass_chat_data=True))
    # on noncommand i.e. text, photo, video, location, forwarded, entity, MessageEntity
    dp.add_handler(MessageHandler(Filters.text, botFunc.textMsg))
    dp.add_handler(MessageHandler(Filters.sticker, botFunc.stickerMsg))
    dp.add_handler(MessageHandler(Filters.photo, botFunc.photoMsg))
    dp.add_handler(MessageHandler(Filters.video, botFunc.videoMsg))
    dp.add_handler(MessageHandler(Filters.voice, botFunc.voiceMsg))
    dp.add_handler(MessageHandler(Filters.audio, botFunc.audioMsg))
    dp.add_handler(MessageHandler(Filters.document, botFunc.documentMsg))
    dp.add_handler(MessageHandler(Filters.location, botFunc.locationMsg))
    # log all errors
    dp.add_error_handler(log.error)