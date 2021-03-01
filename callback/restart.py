import psutil
from telegram import Update
from telegram.ext import CallbackContext

from common import get_full_info, kill_proc_tree, start_program, update_repo


class Restart:
    @staticmethod
    def command(update: Update, context: CallbackContext):
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
                        f"""{status_msg.text_html}
    <pre>{result}</pre>"
    Trying to start the bot again...""",
                        parse_mode="HTML",
                    )
                    start_program(path=path, arg=" ".join(arg for arg in args))
                    status_msg.edit_text(
                        f"{status_msg.text_html}\nStarted the bot", parse_mode="HTML"
                    )
                except psutil.NoSuchProcess:
                    update.effective_message.reply_html(
                        "Looks like someone already killed it!"
                    )
        else:
            update.effective_message.reply_html(
                "<b>Format:</b> /restart alias \nUse /get to get all running py programs"
            )
