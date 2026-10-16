name: Trade Map bot

on:
  schedule:
    - cron: "3,13,23,33,43,53 * * * *"   # every 10 minutes (GitHub may run it late)
  workflow_dispatch:                      # lets you start it by hand from the Actions tab

permissions:
  contents: write                         # needed to save the paper account between runs

concurrency:
  group: tradebot
  cancel-in-progress: false

jobs:
  run:
    runs-on: ubuntu-latest
    timeout-minutes: 5
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - run: pip install requests

      - name: Check for new candles
        run: python free_bot.py --once
        env:
          DISCORD_WEBHOOK_URL: ${{ secrets.DISCORD_WEBHOOK_URL }}
          PAIRS: "XBTUSD,ETHUSD"
          INTERVAL_MIN: "60"

      - name: Save paper account
        run: |
          git config user.name "tradebot"
          git config user.email "tradebot@users.noreply.github.com"
          git add -A
          git diff --cached --quiet || (git commit -m "Update paper account" && git push)
