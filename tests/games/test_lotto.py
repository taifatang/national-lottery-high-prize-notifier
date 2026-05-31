from games.base import DrawData
from games.lotto import Lotto

SAMPLE_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<draw-results>
  <game type="lotto">
    <draw><draw-date>2026-05-30</draw-date></draw>
    <next-estimated-jackpot>12,500,000</next-estimated-jackpot>
    <rollover-count>3</rollover-count>
  </game>
</draw-results>"""

MUST_BE_WON_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<draw-results>
  <game type="lotto">
    <next-estimated-jackpot>20,000,000</next-estimated-jackpot>
    <rollover-count>5</rollover-count>
  </game>
</draw-results>"""

NO_ROLLOVER_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<draw-results>
  <game type="lotto">
    <next-estimated-jackpot>2,000,000</next-estimated-jackpot>
  </game>
</draw-results>"""


def test_parse_jackpot_and_rollover_count():
    data = Lotto().parse(SAMPLE_XML)
    assert data == DrawData(jackpot=12_500_000.0, is_must_be_won=False)


def test_parse_sets_must_be_won_at_max_rollovers():
    data = Lotto().parse(MUST_BE_WON_XML)
    assert data == DrawData(jackpot=20_000_000.0, is_must_be_won=True)


def test_parse_returns_none_rollover_when_missing():
    data = Lotto().parse(NO_ROLLOVER_XML)
    assert data == DrawData(jackpot=2_000_000.0, is_must_be_won=False)
