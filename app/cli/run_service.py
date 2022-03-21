import os

import click

from app.server_monolithic import app as app_monolithic
from app.micro_service_mul import app as app_ms_mul
from app.micro_service_sum import app as app_ms_sum


@click.command(name="service_monolithic")
def run_app_monolithic():
    app_monolithic.run(
        debug=True,
        host="0.0.0.0",
        port=os.getenv('PORT', 8000)
    )


@click.command(name="ms_service_master")
def run_ms_app_master():
    app_monolithic.run(
        debug=True,
        host="0.0.0.0",
        port=os.getenv('PORT', 8000)
    )


@click.command(name="ms_service_mul")
def run_ms_app_mul():
    app_ms_mul.run(
        debug=True, host="0.0.0.0", port=os.getenv('PORT', 8002)
    )


@click.command(name="ms_service_sum")
def run_ms_app_sum():
    app_ms_sum.run(
        debug=True, host="0.0.0.0", port=os.getenv('PORT', 8001)
    )


services_cmds = [
    run_app_monolithic,
    run_ms_app_master,
    run_ms_app_mul,
    run_ms_app_sum
]
