from datetime import timedelta
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, TypeHandler, CallbackQueryHandler

from callback import Jobs, Misc, Restart, Stats
from const.CONFIG import CONFIG

logging.basicConfig(format='%(asctime)s - %(name)s - %(message)s',
                    level=logging.INFO, filename="logs.log")

logger = logging.getLogger(__name__)


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
