import click

# Please see more refs on how click works  https://click.palletsprojects.com/en/7.x/
@click.group(chain=True)
def app():
    """Command line entry, choose from the commands listed below"""
    pass


if __name__ == "__main__":
    #build_commands()
    app()