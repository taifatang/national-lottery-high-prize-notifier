import os

from notifiers.base import BaseNotifier


class GithubConsoleNotifier(BaseNotifier):
    def send(self, results):
        lines = [
            "## 🎰 High Prize Alert",
            "",
            "| Game | Jackpot | Threshold |",
            "|------|---------|-----------|",
        ]
        for game_name, jackpot, prize_threshold in results:
            lines.append(f"| {game_name} | £{jackpot:,.2f} | £{prize_threshold:,.2f} |")

        markdown = "\n".join(lines)

        summary_file = os.environ.get("GITHUB_STEP_SUMMARY")
        if summary_file:
            with open(summary_file, "a") as f:
                f.write(markdown + "\n")
        else:
            print(markdown)
