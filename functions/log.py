# log.py - Bot Logs
# ShiroFramework 1.0
import logging, colorlog
from termcolor import colored

# Chat Log
def msgLog(fm, msgType, content):
    # Colored msg
    if msgType == 'text':
        cmt = colored('(' + msgType + ')', 'white', attrs=['underline']) + ' '
    elif msgType == 'sticker':
        cmt = colored('(' + msgType + ')', 'red', attrs=['underline']) + ' '
    elif msgType == 'location':
        cmt = colored('(' + msgType + ')', 'green', attrs=['underline']) + ' '
    elif msgType == 'voice' or msgType == 'audio':
        cmt = colored('(' + msgType + ')', 'magenta', attrs=['underline']) + ' '
    else:
        cmt = colored('(' + msgType + ')', 'cyan', attrs=['underline']) + ' '

    chatLogger.info(fm + enter + cmt + colored(content, 'white'))

# Error log
def error(bot, update, error):
    """Log Errors caused by Updates."""
    botLogger.warning('Update "%s" caused error "%s"', update, error)

def handlerErr(errMsg):
	botLogger.error(colored('Handler: ', 'red') + errMsg)

# Enable logging
def logActive(DEBUG):
    global botLogger, apiLogger, chatLogger
    # Loggers init
    botLogger = logging.getLogger('BOT')
    apiLogger = logging.getLogger('telegram.ext')
    chatLogger = logging.getLogger('[CHAT]')

    # Set Format
    runTime = '%(bg_white)s%(asctime)s%(reset)s '
    lvName = '%(log_color)s[%(levelname)s]%(reset)s '
    logName = '%(cyan)s%(name)s%(reset)s' + enter
    logMsg = '%(white)s%(message)s'
    fmName = '%(thin_yellow)s%(name)s%(reset)s '
    sysfmt = colorlog.ColoredFormatter(runTime + lvName + logName + logMsg,
                                        datefmt="%Y-%m-%d %H:%M:%S",
                                        reset=True,
                                        log_colors={
                                            'DEBUG':    'bold_cyan',
                                            'INFO':     'bold_white',
                                            'WARNING':  'bold_yellow',
                                            'ERROR':    'bold_red',
                                            'CRITICAL': 'bold_red,bg_white',
                                        },
                                        secondary_log_colors={},
                                        style='%'
                                        )
    logMsg = '%(white)s%(message)s'
    chatfmt = colorlog.ColoredFormatter(runTime + fmName + logMsg,
                                        datefmt="%Y-%m-%d %H:%M:%S",
                                        reset=True,
                                        secondary_log_colors={},
                                        style='%'
                                        )

    # Set handler
    console = logging.StreamHandler()
    console.setFormatter(sysfmt)
    chatConsole = logging.StreamHandler()
    chatConsole.setFormatter(chatfmt)
    # Logger Level
    # Check Debug mode is on
    if DEBUG == True:
        file = logging.FileHandler(filename='debug.log')
        file.setFormatter(logging.Formatter('[%(asctime)s]%(name)s - %(levelname)s - %(message)s'))
        apiLogger.setLevel(logging.INFO)
        debugStatus = colored(' ON ', 'red', attrs=['reverse'])
    elif DEBUG == False:
        file = logging.FileHandler(filename='system.log')
        file.setFormatter(logging.Formatter('[%(asctime)s]%(name)s - %(levelname)s - %(message)s'))
        apiLogger.setLevel(logging.INFO)
        debugStatus = colored(' OFF ', 'white', attrs=['reverse'])
    botLogger.setLevel(logging.INFO)
    chatLogger.setLevel(logging.INFO)

    # Handler
    apiLogger.addHandler(console)
    apiLogger.addHandler(file)
    botLogger.addHandler(console)
    botLogger.addHandler(file)
    chatLogger.addHandler(chatConsole)

    botLogger.info(colored('', 'green') + 
                    colored('DEBUG MODE:',
                            attrs=['concealed', 'underline']
                            ) + '  ' + debugStatus + 
                    enter +
                    colored('Listening ...',
                            attrs=['concealed', 'underline']
                            ))
enter = '\n                    '