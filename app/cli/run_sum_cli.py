import click

from app.lib.arithmetic.sum import my_sum


@click.command(name="sum_cmd",  help="Sum multiple numbers and print the result")
@click.option(
    "--element", "-e", required=True, help="element to perform op for", type=click.FLOAT, multiple=True
)
def sum_cmd(element):
    click.echo(f"the result sum of elements : {element} is {my_sum(*element)}")

if __name__ == "__main__":
    sum_cmd()

sum_cli_cmds = [sum_cmd]
