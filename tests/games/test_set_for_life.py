from games.base import Weekday
from games.set_for_life import SetForLife


def test_set_for_life_attributes():
    game = SetForLife()
    assert game.name == "Set For Life"
    assert "set-for-life" in game.xml_url
    assert Weekday.MONDAY in game.draw_days
    assert Weekday.THURSDAY in game.draw_days
    assert game.prize_threshold > 0


def test_set_for_life_fetch_jackpot_returns_fixed_prize():
    # Fixed prize: £10,000/month for 30 years = £3,600,000 — no HTTP call
    assert SetForLife().fetch_jackpot() == 3_600_000.0
