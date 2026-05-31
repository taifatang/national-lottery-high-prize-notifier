from games.base import BaseGame, Weekday


class EuroMillions(BaseGame):
    name = "EuroMillions"
    url = "https://www.national-lottery.co.uk/results/euromillions/draw-history/xml"
    draw_days = [Weekday.TUESDAY, Weekday.FRIDAY]
    prize_threshold = 75_000_000.0
