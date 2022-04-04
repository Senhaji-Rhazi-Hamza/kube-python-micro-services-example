import click
from app.lib.arithmetic.mul import my_mul 

@click.command(name="mul_cmd", help="Multiply multiple numbers and print the result")
@click.option(
    "--element", "-e", required=True, help="element to perform op for", type=click.FLOAT,multiple=True
)
def mul_cmd(element):
    click.echo(f"the result product of elements : {element} is {my_mul(*element)}")


if __name__ == "__main__":
    mul_cmd()

mul_cli_cmds = [mul_cmd]