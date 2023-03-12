from datetime import timedelta
import logging
from logging.handlers import RotatingFileHandler
from telegram import Update, BotCommand
from telegram.ext import Updater, CommandHandler, TypeHandler, CallbackQueryHandler

from callback import Jobs, Misc, Restart, Stats
from const.CONFIG import CONFIG

logging.basicConfig(handlers=[RotatingFileHandler("./logs.log", maxBytes=10000, backupCount=4)],
                    level=logging.ERROR,
                    format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
                    datefmt="%Y-%m-%dT%H:%M:%S", )

logger = logging.getLogger(__name__)

aps_logger = logging.getLogger('apscheduler')
aps_logger.setLevel(logging.ERROR)


def main():
	updater = Updater(CONFIG.BOTTOKEN)
	dispatcher = updater.dispatcher
	job_q = updater.job_queue
	job_q.run_repeating(
		callback=Jobs.supervisor, interval=timedelta(minutes=5), first=5
		)
	dispatcher.add_handler(
		TypeHandler(type=Update, callback=Misc.block_access), group=0
		)
	dispatcher.add_handler(CommandHandler("start", Misc.start_command), group=1)
	dispatcher.add_handler(CommandHandler("restart", Restart.command), group=1)
	dispatcher.add_handler(
		CallbackQueryHandler(Restart.command, pattern="^restart"), group=1
		)
	dispatcher.add_handler(CommandHandler("get", Misc.get_all), group=1)
	dispatcher.add_handler(CommandHandler("help", Misc.help_command), group=1)
	dispatcher.add_handler(CommandHandler("stats", Stats.command), group=1)
	dispatcher.add_handler(
		CommandHandler("detail_stats", Stats.detail_command), group=1
		)
	dispatcher.add_handler(
		CallbackQueryHandler(Stats.command, pattern="refresh"), group=1
		)
	updater.bot.set_my_commands(
		[
			BotCommand("start", "start the bot"),
			BotCommand("restart", "restart a bot/script using alias"),
			BotCommand("get", "get all running py processes"),
			BotCommand("stats", "stats of the server"),
			BotCommand("detail_stats", "stats of the processes"),
			BotCommand("help", "help message"),
			]
		)
	if CONFIG.PORT_NUM != 0:
		updater.start_webhook(
			listen="127.0.0.1", port=CONFIG.PORT_NUM, url_path=CONFIG.BOTTOKEN
			)
		updater.bot.set_webhook(
			url=f"https://{CONFIG.IP_ADDR}:443/{CONFIG.BOTTOKEN}",
			certificate=open("cert.pem", "rb"),
			)
	else:
		updater.start_polling()
		updater.idle()


if __name__ == "__main__":
	main()
