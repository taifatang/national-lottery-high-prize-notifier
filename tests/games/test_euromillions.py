from games.base import Weekday
from games.euromillions import EuroMillions

SAMPLE_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<draw-results>
  <game type="euromillions">
    <draw><draw-date>2026-05-29</draw-date></draw>
    <next-estimated-jackpot>122,000,000</next-estimated-jackpot>
    <next-draw-day>TUESDAY</next-draw-day>
  </game>
</draw-results>"""


def test_euromillions_attributes():
    game = EuroMillions()
    assert game.name == "EuroMillions"
    assert "euromillions" in game.url
    assert Weekday.TUESDAY in game.draw_days
    assert Weekday.FRIDAY in game.draw_days
    assert game.prize_threshold > 0


def test_euromillions_fetch_jackpot(requests_mock):
    game = EuroMillions()
    requests_mock.get(game.url, text=SAMPLE_XML)
    assert game.fetch_jackpot() == 122_000_000.0
