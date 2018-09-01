#!/usr/bin/env python
# -*- coding: utf-8 -*-


from telegram.ext import Updater, CommandHandler
import telegram
import logging
import datetime

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Date magic and parsing functions

def make_date_time(date_string):
    date_components = [ int(date_component) for date_component in date_string.split("-") ]
    date = datetime.date(date_components[0],date_components[1],date_components[2])
    return date

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.

def start(bot, update):
    update.message.reply_text('Use /<conference name> to fetch the deadline, for example try /CVPR or /NIPS. For all conferences, use /list.')


# def start(bot, update):
#     kb = [[telegram.KeyboardButton('/CVPR')],
#           [telegram.KeyboardButton('/NIPS')],
#           [telegram.KeyboardButton('/AISTATS')],
#           [telegram.KeyboardButton('/AAAI')],
#           [telegram.KeyboardButton('/ICLR')],
#           [telegram.KeyboardButton('/ICML')],]                                  
#     kb_markup = telegram.ReplyKeyboardMarkup(kb)
#     bot.send_message(chat_id=update.message.chat_id,
#                      text="Start",
#                      reply_markup=kb_markup)


# def alarm(bot, job):
#     """Send the alarm message."""
#     bot.send_message(job.context, text='Time is up!')


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

# =====================================================================
# Helper Functions

def helpf(bot,update):
    update.message.reply_text(
        "This bot gives you the deadline for various conferences. Currently, it's set for CVPR, NIPS, CVPR, AAAI, AISTATS, ICLR and ICML. More will be added soon.")



def list(bot,update):
    update.message.reply_text(
        "/CVPR: Conference on Computer Vision and Pattern Recognition, \n /NIPS: Conference on Neural Information Processing Systems, \n /ICML: International Conference on Machine Learning, \n /ICMR: International Conference on Learning Representations, \n /AAAI: Association for the Advancement of Artificial Intelligence Conference, \n /AISTATS: nternational Conference on Artificial Intelligence and Statistics")  

# =====================================================================
# Conference Descriptions


# ================================== CVPR =================================
def cvpr_conf(bot,update):

    """CVPR Deadline Date, harcoded"""
    deadline = "2018-11-17"

    today = datetime.date.today()
    time_remaining = make_date_time(deadline) - today

    if time_remaining == abs(time_remaining):
        update.message.reply_text(
            "Time Remaining for CVPR Paper Submission Deadline is " + str(time_remaining.days) + " days or " + str(time_remaining.days * 24) + " hours, go submit!")

    else:
        update.message.reply_text("Deadline has passed, try next year!")

# ================================== NIPS =================================

def nips_conf(bot,update):

    """Deadline Dates, harcoded """
    deadline = "2018-05-18"

    today = datetime.date.today()
    time_remaining = make_date_time(deadline) - today

    if time_remaining == abs(time_remaining):
        update.message.reply_text(
            "Time Remaining for NIPS Paper Submission Deadline is " + str(time_remaining.days) + " days or " + str(time_remaining.days * 24) + " hours, go submit!")

    else:
        update.message.reply_text("Deadline has passed, try next year!")


# ================================== AISTATS =================================

def aistats_conf(bot,update):

    """Deadline Dates, harcoded """
    deadline = "2018-10-04"

    today = datetime.date.today()
    time_remaining = make_date_time(deadline) - today

    if time_remaining == abs(time_remaining):
        update.message.reply_text(
            "Time Remaining for AISTATS Paper Submission Deadline is " + str(time_remaining.days) + " days or " + str(time_remaining.days * 24) + " hours, go submit!")

    else:
        update.message.reply_text("Deadline has passed, try next year!")


# ================================== AAAI =================================

def aaai_conf(bot,update):

    """Deadline Dates, harcoded """
    deadline = "2018-09-05"

    today = datetime.date.today()
    time_remaining = make_date_time(deadline) - today

    if time_remaining == abs(time_remaining):
        update.message.reply_text(
            "Time Remaining for AAAI Paper Submission Deadline is " + str(time_remaining.days) + " days or " + str(time_remaining.days * 24) + " hours, go submit!")

    else:
        update.message.reply_text("Deadline has passed, try next year!")

# ================================== AAAI =================================

def iclr_conf(bot,update):

    """Deadline Dates, harcoded """
    deadline = "2018-09-27"

    today = datetime.date.today()
    time_remaining = make_date_time(deadline) - today

    if time_remaining == abs(time_remaining):
        update.message.reply_text(
            "Time Remaining for ICLR Paper Submission Deadline is " + str(time_remaining.days) + " days or " + str(time_remaining.days * 24) + " hours, go submit!")

    else:
        update.message.reply_text("Deadline has passed, try next year!")


# ================================== AAAI =================================

def icml_conf(bot,update):

    """Deadline Dates, harcoded """
    deadline = "TBA"

    if(deadline == "TBA"):
        update.message.reply_text(
            "To Be Announced, Stay Tuned!")
    else:    
        today = datetime.date.today()
        time_remaining = make_date_time(deadline) - today

        if time_remaining == abs(time_remaining):
            update.message.reply_text(
                "Time Remaining for ICML Paper Submission Deadline is " + str(time_remaining.days) + " days or " + str(time_remaining.days * 24) + " hours, go submit!")

        else:
            update.message.reply_text("Deadline has passed, try next year!")



# End of conference functions

# ================================== Error Logs  =================================

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    """Run bot."""
    updater = Updater("Your-ID") # I'm not giving this bot's ID here for obvious security reasons.

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", helpf))

    # conferences
    dp.add_handler(CommandHandler("CVPR",cvpr_conf))
    dp.add_handler(CommandHandler("NIPS",nips_conf))
    dp.add_handler(CommandHandler("AISTATS",aistats_conf))
    dp.add_handler(CommandHandler("AAAI",aaai_conf))
    dp.add_handler(CommandHandler("ICLR",iclr_conf))
    dp.add_handler(CommandHandler("ICML",icml_conf))

    dp.add_handler(CommandHandler("list",list))

    dp.add_error_handler(error)


    updater.start_polling()


    updater.idle()


if __name__ == '__main__':
    main()