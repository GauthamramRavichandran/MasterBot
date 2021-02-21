import psutil
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, DispatcherHandlerStop

from common import (
    get_list_of_py,
    kill_proc_tree,
    get_full_info,
    start_program,
    update_repo,
)
from CONFIG import CONFIG


def block_access(update: Update, context: CallbackContext):
    if update.effective_user.id not in CONFIG.ADMINS:
        update.effective_message.reply_html(
            """
Hello there, non-admin Human!
    I'm the MasterBot. I help admin in managing bots/programs running in the server.

<b>What do you do?</b>
    For starters, I help in pulling the latest update of a repo to server and restarting that appropriate bot.
""",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "🍴 Fork me",
                            url="https://github.com/GauthamramRavichandran/MasterBot/",
                        )
                    ]
                ]
            ),
        )
        raise DispatcherHandlerStop


def start_command(update: Update, context: CallbackContext):
    update.effective_message.reply_html(
        """
Hello there, Admin!
    I'm the MasterBot. You already know what I do, hit /help for list of commands.
"""
    )


def get_all(update: Update, context: CallbackContext):
    to_send = """
<b>List of py processes running</b>
<pre>cmd     filename    alias</pre>
"""
    for p in get_list_of_py():
        to_send += "<pre>" + " ".join(arg for arg in p.cmdline()) + "</pre>\n"
    update.effective_message.reply_html(to_send)


def restart_command(update: Update, context: CallbackContext):
    if context.args:
        status_msg = update.effective_message.reply_html(
            "Trying to restart the process..."
        )
        alias = context.args[0]
        process = get_full_info(alias)
        if process:
            path = process.cwd()
            args = process.cmdline()
            try:
                kill_proc_tree(process.pid)
                status_msg = status_msg.edit_text(
                    f"{status_msg.text_html}"
                    f"\nBot killed successfully!"
                    f"\nTrying to pull the latest commit...",
                    parse_mode="HTML",
                )
                result = update_repo(path)
                status_msg = status_msg.edit_text(
                    f"{status_msg.text_html}"
                    f"\n<pre>{result}</pre>"
                    f"\nTrying to start the bot again...",
                    parse_mode="HTML",
                )
                start_program(path=path, arg=" ".join(arg for arg in args))
                status_msg.edit_text(
                    f"{status_msg.text_html}" f"\nStarted the bot", parse_mode="HTML"
                )
            except psutil.NoSuchProcess:
                update.effective_message.reply_html(
                    "Looks like someone already killed it!"
                )
    else:
        update.effective_message.reply_html(
            "<b>Format:</b> /restart alias" "\nUse /get to get all running py programs"
        )


def help_command(update: Update, context: CallbackContext):
    update.effective_message.reply_html(
        """
HELP

1. /get - Returns all the py programs running on server
2. /restart alias - Stops the program > Fetches the latest update from repo > Starts the program again

"""
    )
