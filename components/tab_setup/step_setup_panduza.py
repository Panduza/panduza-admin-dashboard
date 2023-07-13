from nicegui import ui

import threading
import subprocess
import time 
import asyncio
import concurrent
import os
import platform
import importlib.util
import sys


from .step_system_control import execute_sys_cmd

class StepSetupPanduza:

    # ---

    def __init__(self, stepper) -> None:
        # Parent Stepper
        self.ui_stepper = stepper

        # Build ui
        with ui.step('Install Panduza') as step:
            self.ui_step = step
            ui.label('Need to install panduza')

            with ui.stepper_navigation():
                ui.button("Install Panduza", on_click=self.start_worker)
                ui.button('Back', on_click=stepper.previous).props('flat')

    # ---

    def worker(self, ui_log_area):

        # Check distribution
        ui_log_area.push("Check that platform is installed")



        name = 'panduza_platform'
        if name in sys.modules:
            ui_log_area.push(f"{name!r} already in sys.modules")
        elif (spec := importlib.util.find_spec(name)) is not None:
            ui_log_area.push("found !")
        else:
            ui_log_area.push("NOT found !")


        reqs = [
            "aardvark-py==5.40",
            "colorama==0.4.6",
            "paho-mqtt==1.6.1",
            "pyftdi==0.54.0",
            "pymodbus==3.3.2",
            "pyserial==3.5",
            "pyudev==0.24.0",
            "pyusb==1.2.1",
            "PyHamcrest==2.0.4",
        ]

        for r in reqs:       
            cmd = ['pip', 'install', r]
            execute_sys_cmd(cmd, ui_log_area)

        cmd = ['pip', 'install', "git+https://github.com/Panduza/panduza-py.git@pico_dio_integration#egg=panduza_platform&subdirectory=platform/", "--no-color"]
        execute_sys_cmd(cmd, ui_log_area)

        
        filename="/usr/local/bin/pza-py-platform-run.py"
        ui_log_area.push(f"Write file: {filename}")
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as f:
            f.write("""
import sys
import pathlib
import argparse
from panduza_platform import Platform

import logging

# Initialize log file
pathlib.Path("/etc/panduza/log").mkdir(parents=True, exist_ok=True)
logging.basicConfig(filename="/etc/panduza/log/py.log", 
					format='%(asctime)s | %(name)s | %(message)s', 
					filemode='w') 


parser = argparse.ArgumentParser()
parser.add_argument('tree', nargs='?', default=None)
args = parser.parse_args()


srv = Platform()
if args.tree != None:
    srv.load_tree_overide(args.tree)
srv.run()
logging.warning("Platform stopped !")
            """)


        filename="/etc/systemd/system/panduza-py-platform.service"
        ui_log_area.push(f"Write file: {filename}")
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as f:
            f.write("""
[Unit]
Description=Platform Python to support Panduza Meta Drivers
After=network.target

[Service]
User=root
ExecStart=/usr/bin/python3 /usr/local/bin/pza-py-platform-run.py

[Install]
WantedBy=multi-user.target
            """)



        cmd = ['systemctl', 'is-active', "panduza-py-platform.service"]
        execute_sys_cmd(cmd, ui_log_area)


        # systemctl status application.service

        # auto start
        # sudo systemctl enable application.service
        # sudo systemctl disable application.service

        # start/stop
        # sudo systemctl start application
        # sudo systemctl stop application.service

        return True
        

    # ---

    async def start_worker(self):
        # Create a log area
        ui_og = ui.log().classes('w-full h-96')

        # Run the worker
        success = False
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(self.worker, ui_og)
            while not future.done():
                await asyncio.sleep(0.5)
            success = future.result()

        if success:
            ui_icon = ui.avatar('check_circle', color='green', text_color='grey-11', rounded=True)
            await asyncio.sleep(2)
            # self.ui_step.remove(ui_og)
            # self.ui_step.remove(ui_icon)
            self.ui_stepper.next()

        else:
            ui_icon = ui.avatar('check_circle', color='red', text_color='grey-11', rounded=True)


