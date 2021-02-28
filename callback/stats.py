from datetime import datetime
from time import time

import psutil
from telegram import Update
from telegram.ext import CallbackContext

from common import convert_to_GB, str_uptime
from const import KeyboardMK


class Stats:
    @staticmethod
    def command(update: Update, context: CallbackContext):
        stat_msg = f"""
<u>Server Stats</u>

    <b>CPU Percent</b>: {psutil.cpu_percent(interval=0.1)}%
    <b>RAM</b>: {psutil.virtual_memory().percent}%
    <b>DISK</b>: {convert_to_GB(psutil.disk_usage('/').used)}GB of {convert_to_GB(psutil.disk_usage('/').total)}GB used
    <b>Uptime</b>: {str_uptime(time() - psutil.boot_time())}
    <b>Booted on</b>: {datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")}

    <b>Stats as of</b> {datetime.fromtimestamp(time()).strftime("%Y-%m-%d %H:%M:%S")}
"""
        if update.callback_query:
            try:
                update.callback_query.edit_message_text(
                    stat_msg, parse_mode="HTML", reply_markup=KeyboardMK.refresh_stats()
                )
            except:  # raises "BadRequest:Message not modified" if there's no change in stats
                pass
        else:
            update.effective_message.reply_text(
                stat_msg, parse_mode="HTML", reply_markup=KeyboardMK.refresh_stats()
            )
