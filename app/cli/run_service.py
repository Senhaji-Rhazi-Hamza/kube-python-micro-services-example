import os

import click

from app.server_monolithic import app as app_monolithic
from app.micro_service_mul import app as app_ms_mul
from app.micro_service_sum import app as app_ms_sum
from app.micro_service_master import app as app_ms_master
from app import config

@click.command(name="service_monolithic",  help="Start the monolithic service (summing, multuplying)")
def run_app_monolithic():
    app_monolithic.run(
        debug=True,
        host="0.0.0.0",
        port=os.getenv('PORT', 8000)
    )


@click.command(name="ms_service_master", help="Start the microservice master (proxy for other ms)")
def run_ms_app_master():
    app_ms_master.run(
        debug=True,
        host="0.0.0.0",
        port=os.getenv('PORT', 8000)
    )


@click.command(name="ms_service_mul", help="Start the micro service multuplying")
def run_ms_app_mul():
    app_ms_mul.run(
        debug=True, host="0.0.0.0", port=os.getenv('PORT', config.MUL_PORT)
    )


@click.command(name="ms_service_sum",  help="Start the micro service summing")
def run_ms_app_sum():
    app_ms_sum.run(
        debug=True, host="0.0.0.0", port=os.getenv('PORT', config.SUM_PORT)
    )


services_cmds = [
    run_app_monolithic,
    run_ms_app_master,
    run_ms_app_mul,
    run_ms_app_sum
]
