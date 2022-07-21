#!/usr/bin/env python

import requests
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler, CallbackQueryHandler
from data_prep import process_person

from constants import BOT_TOKEN, bot_chatID


def telegram_bot_sendtext(bot_message,path=None):

    # Sending Text Message Part
    send_text = 'https://api.telegram.org/bot' + BOT_TOKEN + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    
    if path != None:
        # Sending Image part
        url = "https://api.telegram.org/bot"+BOT_TOKEN+"/sendPhoto"
        files = {'photo': open(path, 'rb')}
        data = {'chat_id' : bot_chatID}
        res= requests.post(url, files=files, data=data)


def createEntry(update: Update, context: CallbackContext) -> None:
    details = update.message.text
    user = details.split(",")
    
    name, role, start_time, end_time = user[0], user[1], user[2], user[3]
    start_time = int(start_time)
    end_time = int(end_time)

    process_person(name, role,start_time,end_time)


def save(update: Update, context: CallbackContext) -> None:
    save = update.message.text
    if save == "Yes" or save =="yes":
        update.message.reply_text("If he is family member enter his details like\n Name,Family\n Else enter visitor details like\n Name,OneTime,12AM(time).")    
    
def permission(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    allow = update.message.text
    print(allow)
    if allow == "Allow" or allow == "allow":
        update.message.reply_text("Is he a frequent visitor?\n Should I save it: Yes / No .")
    else:
        update.message.reply_text("The user has been discarded from entry.")
	
def known_person_permission(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    allow = update.message.text
    print(allow)
    if allow == "Allow" or allow == "allow":
        update.message.reply_text("Letting him in")
    else:
        update.message.reply_text("The user has been discarded from entry.")
    
    #CallbackContext.stop()

def known_person_wrong_time(text):
    """Start the bot."""
    global updater
    updater = Updater(BOT_TOKEN)
    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    telegram_bot_sendtext(text)
    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.regex('^(Allow|allow|deny|Deny)$'), known_person_permission))
    # Start the Bot
    updater.start_polling()
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()
    
def messaging(text,image) :
    """Start the bot."""
# Create the Updater and pass it your bot's token.
    global updater
    updater = Updater(BOT_TOKEN)
# Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    telegram_bot_sendtext(text,image)
#dispatcher.add_handler(conversation_handler)


# on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.regex('^.*[,].*$'), createEntry))
    dispatcher.add_handler(MessageHandler(Filters.regex('^(yes|Yes|no|No)$'), save))
    dispatcher.add_handler(MessageHandler(Filters.regex('^(Allow|allow|deny|Deny)$'), permission))
#dispatcher.add_handler(conversation_handler)

# Start the Bot
    updater.start_polling()
# Run the bot until you press Ctrl-C or the process receives SIGINT,
# SIGTERM or SIGABRT. This should be used most of the time, since
# start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()
    


def main() :
    #telegram_bot_sendtext("Hieieieei")
    #messaging("yo", "image dataset/Sham/img0.jpg")
    #shiv('Sharanya','Family','12 00','13 00')
    known_person_wrong_time("someone recognized, but wrong time, shoo off?Allow/Deny??")
    print("Hii?")

if __name__ == "__main__":
    main()