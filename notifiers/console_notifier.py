import unicodedata

from games.base import Weekday
from notifiers.base import BaseNotifier


def _display_width(s: str) -> int:
    return sum(2 if unicodedata.east_asian_width(c) in ("W", "F") else 1 for c in s)


def _pad(s: str, width: int) -> str:
    return s + " " * (width - _display_width(s))


# Output format:
# ┌──────────────────┬─────────────────┬────────────────┬──────────────────┬─────────────┐
# │ Game             │ Jackpot         │ Threshold      │ Notify Day       │ Must Be Won │
# ├──────────────────┼─────────────────┼────────────────┼──────────────────┼─────────────┤
# │ 🌟 EuroMillions  │ £122,000,000.00 │ £75,000,000.00 │ Monday, Thursday │ —           │
# │ 🎱 Lotto         │ £5,013,960.00   │ £5,000,000.00  │ Tuesday, Friday  │ N           │
# └──────────────────┴─────────────────┴────────────────┴──────────────────┴─────────────┘
class ConsoleNotifier(BaseNotifier):
    def send(self, results):
        rows = []
        for game_name, jackpot, prize_threshold, draw_days, is_roll_down in results:
            notify_day = ", ".join(Weekday((d - 1) % 7).name.capitalize() for d in draw_days)
            jackpot_str = f"£{jackpot:,.2f}" if jackpot is not None else "N/A"
            roll_down_str = "Y" if is_roll_down is True else ("N" if is_roll_down is False else "—")
            rows.append((game_name, jackpot_str, f"£{prize_threshold:,.2f}", notify_day, roll_down_str))

        headers = ("Game", "Jackpot", "Threshold", "Notify Day", "Must Be Won")
        col_widths = tuple(
            max(_display_width(headers[i]), max(_display_width(r[i]) for r in rows))
            for i in range(len(headers))
        )

        def row(*cols, sep="│"):
            return " ".join(
                f"{sep} {_pad(c, col_widths[i])}" for i, c in enumerate(cols)
            ) + f" {sep}"

        def divider(left, mid, right, fill="─"):
            return left + mid.join(fill * (w + 2) for w in col_widths) + right

        print("=== High Prize Alert ===")
        print(divider("┌", "┬", "┐"))
        print(row(*headers))
        print(divider("├", "┼", "┤"))
        for r in rows:
            print(row(*r))
        print(divider("└", "┴", "┘"))
