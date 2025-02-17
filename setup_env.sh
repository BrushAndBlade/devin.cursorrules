#!/bin/zsh

# Show commands being run
set -x

# Initialize environment
if [ ! -d "venv" ]; then
    $(brew --prefix python@3.9)/bin/python3 -m venv venv --prompt "AI_Companion" --clear
    source venv/bin/activate
    chmod +x venv/bin/activate
    pip install -U pip setuptools wheel
    pip install "click<9.0" "python-dotenv<2.0" "requests<3.0" "playwright<1.45" "yfinance<0.3" "matplotlib<3.8" "seaborn<0.14"
    python -m playwright install chromium
    
    # Patch activate script
    echo 'export PATH="/opt/homebrew/opt/python@3.9/bin:$PATH"' >> venv/bin/activate
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

# Disable debug output
set +x 