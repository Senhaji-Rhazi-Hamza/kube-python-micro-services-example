import click
import ipdb; ipdb.set_trace()
from app.lib.arithmetic.mul import my_mul 

@click.command(name="mul_cmd")
@click.option(
    "--element", "-e", required=True, help="element to perform op for", type=click.FLOAT,multiple=True
)
def mul_cmd(element):
    click.echo(f"the result product of elements : {element} is {my_mul(*element)}")


if __name__ == "__main__":
    mul_cmd()

mul_cli_cmds = [mul_cmd]