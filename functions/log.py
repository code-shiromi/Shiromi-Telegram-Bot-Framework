# log.py - Bot Logs
# ShiroFramework 1.0
import logging, colorlog
from termcolor import colored

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
    chatLogger = logging.getLogger('CHAT')

    # Set Format
    runTime = '%(bg_white)s%(asctime)s%(reset)s '
    lvName = '%(log_color)s[%(levelname)s]%(reset)s '
    logName = '%(cyan)s%(name)s%(reset)s\n                    '
    logMsg = '%(white)s%(message)s'
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

    # Set handler
    console = logging.StreamHandler()
    console.setFormatter(sysfmt)
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

    # Handler
    apiLogger.addHandler(console)
    apiLogger.addHandler(file)
    botLogger.addHandler(console)
    botLogger.addHandler(file)

    botLogger.info(colored('', 'green') + 
                    colored('DEBUG MODE:',
                            attrs=['concealed', 'underline']
                            ) + '  ' + debugStatus + 
                    '\n                    ' +
                    colored('Listening ...',
                            attrs=['concealed', 'underline']
                            ))