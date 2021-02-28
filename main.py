from telegram import Update
from telegram.ext import Updater, CommandHandler, TypeHandler, CallbackQueryHandler

from callback import Misc, Restart, Stats
from const.CONFIG import CONFIG


def main():
    updater = Updater(CONFIG.BOTTOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(
        TypeHandler(type=Update, callback=Misc.block_access), group=0
    )
    dispatcher.add_handler(CommandHandler("start", Misc.start_command), group=1)
    dispatcher.add_handler(CommandHandler("restart", Restart.command), group=1)
    dispatcher.add_handler(CommandHandler("get", Misc.get_all), group=1)
    dispatcher.add_handler(CommandHandler("help", Misc.help_command), group=1)
    dispatcher.add_handler(CommandHandler("stats", Stats.command), group=1)
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
