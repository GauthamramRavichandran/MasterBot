import psutil
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext

from common import get_full_info, kill_proc_tree, start_program, update_repo


class Restart:
	@staticmethod
	def command( update: Update, context: CallbackContext ):
		if context.args:
			alias = context.args[0]

		elif update.callback_query is not None:
			alias = update.callback_query.data.split("_", maxsplit=1)[-1]
			update.effective_message.delete()  # keep the chat clean
		else:
			return update.effective_message.reply_html(
				"<b>Format:</b> /restart alias "
				"\nUse /get to get all running py programs"
				)

		process = get_full_info(alias)
		status_msg = update.effective_message.reply_html(
			f"Trying to restart the process {alias}...", quote=False
			)
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

				if result["exit-code"]!= 0:
					status_msg = status_msg.edit_text(
					f"""{status_msg.text_html}
<pre>{result['output']}</pre>
❗️Failed to update the repo, restarting the bot as-is ...""",
					parse_mode="HTML")
				else:
					status_msg = status_msg.edit_text(
						f"""{status_msg.text_html}
	<pre>{result['output']}</pre>
	Trying to start the bot again...""",
						parse_mode="HTML",
						)
				start_program(path=path, arg=" ".join(arg for arg in args))
				status_msg.edit_text(
					f"{status_msg.text_html}\nStarted the bot",
					parse_mode="HTML",
					reply_markup=InlineKeyboardMarkup(
						[
							[
								InlineKeyboardButton(
									f"Restart {alias}", callback_data=f"restart_{alias}"
									)
								]
							]
						),
					)
			except psutil.NoSuchProcess:
				update.effective_message.reply_html(
					"Looks like someone already killed it!"
					)
		else:
			update.effective_message.reply_html(f"No process found under the alias {alias}",
			                                    quote=False)