# botFunc.py - Bot Response
# ShiroFramework 1.0
from functions import log
from termcolor import colored
from pprint import pformat

def alarm(bot, job):
    """Send the alarm message."""
    bot.send_message(job.context, text='Beep!')

def query(bot, update):
    content = senderFunc(bot, update, 'command')
    query = pformat(str(update.message))
    update.message.reply_text(query)

def set_timer(bot, update, args, job_queue, chat_data):
    content = senderFunc(bot, update, 'command')
    """Add a job to the queue."""
    chat_id = update.message.chat_id
    try:
        # args[0] should contain the time for the timer in seconds
        due = int(args[0])
        if due < 0:
            update.message.reply_text('Sorry we can not go back to future!')
            return

        # Add job to queue
        job = job_queue.run_once(alarm, due, context=chat_id)
        chat_data['job'] = job

        update.message.reply_text('Timer successfully set!')

    except (IndexError, ValueError):
        update.message.reply_text('Usage: /set <seconds>')

def unset(bot, update, chat_data):
    """Remove the job if the user changed their mind."""
    if 'job' not in chat_data:
        update.message.reply_text('You have no active timer')
        return

    job = chat_data['job']
    job.schedule_removal()
    del chat_data['job']

    update.message.reply_text('Timer successfully unset!')

def start(bot, update):
    content = senderFunc(bot, update, 'command')
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help(bot, update):
    content = senderFunc(bot, update, 'command')
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


# -------- Content Functions --------
def getCt(update):
    if update.message is not None:
        msg = update.message
        chatType = msg.chat.type
    elif update.message is None:
        msg = update.channel_post
        chatType = msg.chat.type
        '''
    else:
        log.handlerErr('Unknown Chat Type')
        pass'''
    return msg, chatType

def getCon(msg, con):
    if con == 'text' or con == 'command':
        content = msg.text
    elif con == 'sticker':
        content = msg['sticker']['file_id']
    elif con == 'photo':
        p = msg['photo']
        max = 0
        for i in range(1,len(p)):
            if p[i]['width'] > p[max]['width']:
                max = i
        maxFileId = p[max]['file_id']
        try:
            text = '%s %s%s' % (' [Message:',msg['caption'],']')
        except:
            text = ' [No Message]'
        content = maxFileId + text
    elif con == 'video':
        content = msg['video']['file_id']
    elif con == 'voice':
        content = msg['voice']['file_id']
    elif con == 'audio':
        content = msg['audio']['file_id']
    elif con == 'document':
        try:
            text = '%s %s%s' % (' [Message:',msg['caption'],']')
        except:
            text = ' [No Message]'
        content = msg['document']['file_id'] + text
    elif con == 'location':
        latitude = msg['location']['latitude']
        longitude = msg['location']['longitude']
        location = str(latitude) + ',' + str(longitude)
        content = 'https://www.google.com/maps/search/?api=1&query=' + location
    return content

def getFn(firstname, lastname):
    try:
        fullname = firstname + ' ' + lastname
    except TypeError:
        fullname = firstname
    return fullname

def senderFunc(bot, update, con):
    # Check chat type
    msg, chatType = getCt(update)
    content = getCon(msg, con)
    if chatType == 'channel':
        title = msg.chat.title
        chatId = msg.chat.id
        ccType = colored('[' + chatType + ']', 'white', 'on_blue') + colored(title + '(' + str(chatId) + '):', 'cyan', attrs=['underline'])
        log.msgLog(ccType, con, content)
    elif chatType == 'private':
        username = msg.chat.username
        userId = msg.chat.id
        fullname = getFn(msg.chat.first_name, msg.chat.last_name)
        ccType = colored('[' + chatType + ']', 'grey', 'on_white') + colored(fullname + '(' + str(userId) + '):', 'yellow', attrs=['underline'])
        log.msgLog(ccType, con, content)
    elif chatType is 'group' or 'supergroup':
        title = msg.chat.title
        chatId = msg.chat.id
        username = msg.from_user.username
        userId = msg.from_user.id
        fullname = getFn(msg.from_user.first_name, msg.from_user.last_name)
        ccType = colored('[' + chatType + ']', 'white', 'on_red') + colored(title + '(' + str(chatId) + ')', 'green', attrs=['underline']) + ' - ' + colored(fullname + '(' + str(userId) + '):', 'yellow', attrs=['underline'])
        log.msgLog(ccType, con, content)
    return content

# -------- Chat Functions --------
def textMsg(bot, update):
    content = senderFunc(bot, update, 'text')

def stickerMsg(bot, update):
    content = senderFunc(bot, update, 'sticker')

def photoMsg(bot, update):
    content = senderFunc(bot, update, 'photo')

def videoMsg(bot, update):
    content = senderFunc(bot, update, 'video')

def voiceMsg(bot, update):
    content = senderFunc(bot, update, 'voice')

def audioMsg(bot, update):
    content = senderFunc(bot, update, 'audio')

def documentMsg(bot, update):
    content = senderFunc(bot, update, 'document')

def locationMsg(bot, update):
    content = senderFunc(bot, update, 'location')