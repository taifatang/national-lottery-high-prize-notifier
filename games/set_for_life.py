from games.base import BaseGame, Weekday


class SetForLife(BaseGame):
    name = "Set For Life"
    xml_url = "https://www.national-lottery.co.uk/results/set-for-life/draw-history/xml"
    draw_days = [Weekday.MONDAY, Weekday.THURSDAY]
    prize_threshold = 3_600_000.0

    def fetch_jackpot(self) -> float | None:
        # Fixed prize: £10,000/month for 30 years — XML returns text, not a number
        return 3_600_000.0
