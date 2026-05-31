# LottoWatch

A simple repository for those of us wishing to win a life changing sum. Since lotto doesn't support playing only when the prizes are high, this will help remind you. A Telegram channel has been made available at https://t.me/lottowatch

<!-- Screenshot -->

## Schedule

Runs automatically Monday to Thursday at 6pm BST (5pm UTC) via GitHub Actions. Can also be triggered manually from the Actions tab at any time.

## Games

| Game | Draw Days | Notifying Condition |
|------|-----------|---------------------|
| EuroMillions | Tuesday, Friday | <ul><li>Jackpot ≥ £75,000,000</li></ul> |
| Lotto | Wednesday, Saturday | <ul><li>Jackpot ≥ £5,000,000</li><li>Rollovers ≥ 5 (must-be-won draw)</li></ul> |

## How to Run Locally

Install dependencies:

```bash
pip install -e .
```

Run in test mode — skips the day check and prints results to the console regardless of draw schedule:

```bash
python main.py --test
```
