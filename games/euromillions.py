from games.base import BaseGame, Weekday


class EuroMillions(BaseGame):
    name = "EuroMillions"
    xml_url = "https://www.national-lottery.co.uk/results/euromillions/draw-history/xml"
    draw_days = [Weekday.TUESDAY, Weekday.FRIDAY]
    prize_threshold = 50_000_000.0
