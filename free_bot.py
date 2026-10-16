"""
Free Trade Map bot - no TradingView alerts, no hosting, no paid plans.

It pulls free price candles from Kraken (no account or API key needed), runs the same
six-check signal system as the TradingView indicator, tracks a SIMULATED (paper) account,
and posts every trade and its profit to your Discord channel.

Install (once):   pip install requests
Run:              python free_bot.py

Set your Discord webhook first.
  Mac/Linux:   export DISCORD_WEBHOOK_URL="https://discord.com/api/webhooks/..."
  Windows PS:  $env:DISCORD_WEBHOOK_URL="https://discord.com/api/webhooks/..."

Optional settings (environment variables):
  PAIRS             Kraken pairs, comma separated.  Default: XBTUSD,ETHUSD   (Kraken calls Bitcoin XBT)
  INTERVAL_MIN      Candle size in minutes: 1, 5, 15, 30, 60, 240, 1440.  Default: 60
  PAPER_START_BALANCE (1000)   PAPER_RISK_PCT (1)   PAPER_FEE_PCT (0.05)   TP_R (2.0)

The bot only acts on candles that CLOSE while it is running, so leave it running.
Add  --once  to check for new candles one time and exit (used by the free GitHub Actions setup).
It does not place real trades. Paper results assume perfect fills, so real trading does worse.
"""
import csv
import json
import os
import sys
import time

import requests

# ── Settings ────────────────────────────────────────────

import os DISCORD_URL = os.environ.get("https://discordapp.com/api/webhooks/1560425839386955806/D5GwmkR24plktV6y04FpIZoYjCq0ON1otPpM9n60RaUNaQ-b9A-6R53_IzD-2n2Kv_sR", "")

PAIRS = [p.strip().upper() for p in os.environ.get("PAIRS", "XBTUSD,ETHUSD").split(",") if p.strip()]
