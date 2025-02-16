#!/bin/zsh

# Initialize environment
if [ ! -d "venv" ]; then
    python3 -m venv venv
    source venv/bin/activate
    pip install -U pip setuptools wheel
    pip install click python-dotenv requests playwright
    python -m playwright install chromium
else
    source venv/bin/activate
fi

# Configure AI mode
export AI_MODE="FULL_ASSIST"
alias ai="python ai_assistant.py"

# Verify core packages
pip check yfinance matplotlib seaborn || pip install -r requirements.txt

# Set AI configuration
export AI_ASSISTANT_NAME="Matthew's Best Friend" 