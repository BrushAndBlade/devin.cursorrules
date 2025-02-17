import click
from dotenv import load_dotenv
import os

load_dotenv()

@click.group()
def cli():
    """AI Companion CLI"""
    pass

@cli.command()
@click.argument('task')
def start(task):
    """Start AI Companion with a task"""
    print(f"🚀 AI Companion Ready - Describe your task or goal: {task}")
    # Add your AI integration logic here

if __name__ == "__main__":
    cli()