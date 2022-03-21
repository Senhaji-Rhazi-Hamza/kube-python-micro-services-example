import click

from app.cli.run_mul_cli import mul_cli_cmds
from app.cli.run_sum_cli import sum_cli_cmds
from app.cli.run_service import services_cmds

ALL_CHILD_CLI_CMDS = sum_cli_cmds + mul_cli_cmds + services_cmds

# Please see more refs on how click works  https://click.palletsprojects.com/en/7.x/
@click.group(chain=True)
def app():
    """Command line entry, choose from the commands listed below"""
    pass

def build_commands():
    for cmd in ALL_CHILD_CLI_CMDS:
        app.add_command(cmd)

if __name__ == "__main__":
    build_commands()
    app()