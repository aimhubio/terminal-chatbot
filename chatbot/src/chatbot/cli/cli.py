import click
import os
from dotenv import dotenv_values

from chatbot.chatbot import chatbot


@click.group()
def entrypoint():
    pass


@entrypoint.command
@click.option('--dev', is_flag=True, default=False)
@click.option('--repo', required=False,
              default='aim://0.0.0.0:53800',
              type=str)
def run(dev, repo):
    # Load config
    here = os.path.abspath(os.path.dirname(__file__))
    config_file_path = os.path.abspath(os.path.join(here, '..', '..', '..', '.env'))
    config = dotenv_values(config_file_path)

    # Run the bot
    chatbot(
        serpapi_key=config['serpapi_key'],
        openai_key=config['openai_key'],
        dev_mode=dev,
        repo_path=repo,
    )
