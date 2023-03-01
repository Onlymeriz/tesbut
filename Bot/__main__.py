import telegram
import os

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.error import (
    BadRequest,
    ChatMigrated,
    NetworkError,
    TelegramError,
    TimedOut,
    Unauthorized,
)
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,
)
from telegram.ext.dispatcher import DispatcherHandlerStop, run_async
from telegram.utils.helpers import escape_markdown
from Bot import TOKEN, updater



def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi! Welcome to the .env bot. To create a new .env file, please enter the name of the file.')

def create_env_file(update, context):
    """Create a new .env file and ask for the session string."""
    env_file_name = context.args[0]
    open(env_file_name, "a").close()  # create a new file

    # ask for the session string
    update.message.reply_text(f"Please enter the session string to be added to {env_file_name}:")
    return "GET_SESSION_STRING"

def get_session_string(update, context):
    """Add the session string to the .env file."""
    session_string = update.message.text
    env_file_name = context.args[0]
    with open(env_file_name, "a") as f:
        f.write(f"SESSION_STRING='{session_string}'\n")

    update.message.reply_text(f"Session string added to {env_file_name}.")
    return -1

def cancel(update, context):
    """Cancel the current conversation."""
    update.message.reply_text('Operation cancelled.')
    return -1

def main():
    """Start the bot."""

    # Define the conversation flow using callbacks
    conv_handler = telegram.ext.ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            "CREATE_ENV_FILE": [CommandHandler("create", create_env_file)],
            "GET_SESSION_STRING": [MessageHandler(telegram.ext.filters.Filters.text, get_session_string)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    updater.dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
