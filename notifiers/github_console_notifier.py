from notifiers.base import BaseNotifier


class GithubConsoleNotifier(BaseNotifier):
    def send(self, results):
        print("=== High Prize Alert ===")
        for game_name, jackpot, prize_threshold in results:
            print(f"{game_name}: £{jackpot:,.2f} (threshold: £{prize_threshold:,.2f})")
