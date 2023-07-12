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



def execute_sys_cmd(cmd, ui_log_area):

    ui_log_area.push(f"---\n\t$> {cmd}")

    text = ""
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    while True:
        # Poll the process to check if it has terminated
        poll = process.poll()
        if poll is not None:
            break

        # Read stdout and stderr
        output = process.stdout.readline().decode().strip()
        error = process.stderr.readline().decode().strip()
        if output:
            text += output
            ui_log_area.push(f"\t{output}")
        if error:
            text += error
            ui_log_area.push(f"\t{error}")

    ui_log_area.push("---")

    return text


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

            cmd = [sys.executable, '-m', 'pip', 'install', "git+https://github.com/Panduza/panduza-py.git@main#egg=panduza&subdirectory=platform"]
            execute_sys_cmd(cmd, ui_log_area)

            # import subprocess
            # # implement pip as a subprocess:
            # subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
            # '<packagename>'])


        
    #     if text.startswith("Distributor ID:"):
    #         os = text[len("Distributor ID:\t"):]
    #         ui_log_area.push(os)

    #         if os != "Ubuntu":
    #             ui_log_area.push("not supported yet")
    #             return False

    #     # Check os
    #     ui_log_area.push("Check Release")
    #     cmd = ["lsb_release", "-r"]
    #     text = execute_sys_cmd(cmd, ui_log_area)
    #     if text.startswith("Release:"):
    #         release = text[len("Release:\t"):]
    #         ui_log_area.push(release)

    #         if release != "22.04":
    #             ui_log_area.push("not supported yet")
    #             return False

    #     return True

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


