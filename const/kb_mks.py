from telegram import InlineKeyboardButton, InlineKeyboardMarkup


class KeyboardMK:
    @staticmethod
    def refresh_stats() -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔁 Refresh", callback_data="refresh")]]
        )

    @staticmethod
    def repo() -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🍴 Fork me",
                        url="https://github.com/GauthamramRavichandran/MasterBot/",
                    )
                ]
            ]
        )
