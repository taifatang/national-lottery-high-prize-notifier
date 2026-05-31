import pytest
from games.base import BaseGame, GameData, Weekday


class FakeGame(BaseGame):
    name = "FakeGame"
    url = "https://example.com/xml"
    draw_days = [Weekday.WEDNESDAY]
    prize_threshold = 1_000_000.0

    def parse(self, xml_text: str) -> GameData:
        return GameData(jackpot=5_000_000.0, is_roll_down=None)


@pytest.fixture
def game():
    return FakeGame()


def test_qualifies_on_jackpot():
    assert GameData(jackpot=5_000_000.0).is_high_prized(prize_threshold=4_000_000.0) is True


def test_qualifies_on_must_be_won():
    assert GameData(jackpot=None, is_roll_down=True).is_high_prized(prize_threshold=10_000_000.0) is True


def test_does_not_qualify_below_threshold():
    assert GameData(jackpot=3_000_000.0).is_high_prized(prize_threshold=5_000_000.0) is False


def test_does_not_qualify_on_failed_fetch():
    assert GameData(jackpot=None).is_high_prized(prize_threshold=1_000_000.0) is False


def test_fetch_draw_data_calls_parse_on_success(game, requests_mock):
    requests_mock.get(game.url, text="<xml/>")
    data = game.fetch_draw_data()
    assert data == GameData(jackpot=5_000_000.0, is_roll_down=None)


def test_fetch_draw_data_returns_empty_on_http_error(game, requests_mock):
    requests_mock.get(game.url, status_code=403)
    assert game.fetch_draw_data() == GameData(jackpot=None)
