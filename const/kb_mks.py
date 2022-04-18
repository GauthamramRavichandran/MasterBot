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
                        "See me in Action",
                        url = "https://t.me/ys0seri0us_bots/19"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🍴 Fork me",
                        url="https://github.com/GauthamramRavichandran/MasterBot/",
                    )
                ]
            ]
        )
