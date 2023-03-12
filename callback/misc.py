from telegram import Update
from telegram.ext import CallbackContext, DispatcherHandlerStop, Filters

from common import get_list_of_py
from const import CONFIG, KeyboardMK


class Misc:
    @staticmethod
    def block_access(update: Update, context: CallbackContext):
        # ignore service messages/where there is no effective_message
        if update.effective_message is None or Filters.status_update(update):
            raise DispatcherHandlerStop
        if update.effective_user.id not in CONFIG.ADMINS:
            update.effective_message.reply_html(
                """
Hello there, non-admin Human!
    I'm the MasterBot. I help admin in managing bots/programs in your server.

<b>What can I do?</b>
    1. Pull the latest update of a repo to server and restart appropriate bot
    2. Monitor the server statistics
    3. Notify about the failed/stopped bots
    """,
                reply_markup=KeyboardMK.repo(),
            )
            raise DispatcherHandlerStop

    @staticmethod
    def start_command(update: Update, context: CallbackContext):
        update.effective_message.reply_html(
            """
Hello there, Admin!
    I'm the MasterBot. You already know what I do, hit /help for list of commands.
    """
        )

    @staticmethod
    def help_command(update: Update, context: CallbackContext):
        update.effective_message.reply_html(
            """
<b>HELP</b>
    
    1. /get - Returns all the py programs running on server
    2. /restart alias - Stops the program > Fetches the latest update from repo > Starts the program again
    3. /stats - Gets statistics of CPU/Memory usages
    4. /detail_stats - Gets detailed statistics of all processes
    """
        )

    @staticmethod
    def get_all(update: Update, context: CallbackContext):
        to_send = """
<b>List of py processes running</b>
<pre>cmd     filename    alias</pre>

"""
        for p in get_list_of_py():
            to_send += "<pre>" + " ".join(arg for arg in p.cmdline()) + "</pre>\n"
        update.effective_message.reply_html(to_send)
