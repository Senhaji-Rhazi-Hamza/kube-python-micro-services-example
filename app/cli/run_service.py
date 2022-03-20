import os

import click

from app.server_monolithic import app as app_monolithic


@click.command(name="app_monolithic")
def run_app_monolithic():
    app_monolithic.run(
        debug=True,
        host="0.0.0.0",
        port=os.getenv('PORT', 8000)
    )

@click.command(name="app_master")
def run_app_monolithic():
    app_monolithic.run(
        debug=True,
        host="0.0.0.0",
        port=os.getenv('PORT', 8000)
    )
# import click
# import os
# from server import app
# from server_mul import app as app_mul
# from server_sum import app as app_sum
# from server_entry import app as app_entry



# @click.command(name="run_app")
# def run_app():
#     app.run(
#         debug=True, host="0.0.0.0", port=os.getenv('PORT', 8000)
#         )

# @click.command(name="run_app_mul")
# def run_app_mul():
#     app_mul.run(
#         debug=True, host="0.0.0.0", port=os.getenv('PORT', 8001)
#         )

# @click.command(name="run_app_sum")
# def run_app_sum():
#     app_sum.run(
#         debug=True, host="0.0.0.0", port=os.getenv('PORT', 8002)
#         )

# @click.command(name="run_app_entry")
# def run_app_entry():
#     app_entry.run(
#         debug=True, host="0.0.0.0", port=os.getenv('PORT', 8000)
#         )


# run_app_functions = [
#     run_app,
#     run_app_mul,
#     run_app_entry,
#     run_app_sum,
#     ]

services_cmds = [run_app_monolithic]