# botFunc.py - Bot Response
# ShiroFramework 1.0
from functions import log

def alarm(bot, job):
    """Send the alarm message."""
    bot.send_message(job.context, text='Beep!')

def set_timer(bot, update, args, job_queue, chat_data):
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
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def echo(bot, update):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

# -------- Chat Functions --------
def getTextMsg(bot, update):
    # Check chat type
    chatType = update.message.chat.type
    if chatType == 'private':
        pass
    elif chatType == 'group':
        pass
    elif chatType == 'supergroup':
        pass
    elif chatType == 'channel':
        pass
    else:
        log.handlerErr('Unknown Chat Type')
    #print(update.message.chat.type)
    #print('---'+__name__)
    #msg = (test, echo)