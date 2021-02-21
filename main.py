from telegram import Update
from telegram.ext import Updater, CommandHandler, TypeHandler

from callback import start, restart, get_all, block_access, help
from CONFIG import CONFIG


def main():
    updater = Updater(CONFIG.BOTTOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(TypeHandler(type=Update, callback=block_access), group=0)
    dispatcher.add_handler(CommandHandler("start", start), group=1)
    dispatcher.add_handler(CommandHandler("restart", restart), group=1)
    dispatcher.add_handler(CommandHandler("get", get_all), group=1)
    dispatcher.add_handler(CommandHandler("help", help), group=1)

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
