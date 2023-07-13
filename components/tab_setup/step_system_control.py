from nicegui import ui

import threading
import subprocess
import time 
import asyncio
import concurrent
import os
import platform




def execute_sys_cmd(cmd, ui_log_area):

    ui_log_area.push(f"---\n\t$> {cmd}")

    text = ""
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    alive = True
    while alive:
        # Poll the process to check if it has terminated
        poll = process.poll()
        if poll is not None:
            alive = False

        # Read stdout and stderr
        data_available = True
        while data_available:
            output = process.stdout.readline().decode().strip()
            if output:
                text += output
                ui_log_area.push(f"\t{output}")
            else:
                data_available = False
        

        data_available = True
        while data_available:
            error = process.stderr.readline().decode().strip()
            if error:
                text += error
                ui_log_area.push(f"\t{error}")
            else:
                data_available = False
                
    ui_log_area.push("---")

    return text


class StepSystemControl:

    def Name():
        return 'System Checks'

    # ---

    def __init__(self, stepper) -> None:
        # Parent Stepper
        self.ui_stepper = stepper

        # Build ui
        with ui.step(StepSystemControl.Name()) as step:
            self.ui_step = step
            ui.label('Need to check system requirements')

            with ui.stepper_navigation() as nav:
                self.ui_nav = nav
                ui.button("Check system", on_click=self.start_worker)
                # ui.button('Back', on_click=stepper.previous).props('flat')


    # ---

    def worker(self, ui_log_area):

        # Check distribution
        ui_log_area.push("Check Distribution")
        cmd = ["lsb_release", "-i"]
        text = execute_sys_cmd(cmd, ui_log_area)
        if text.startswith("Distributor ID:"):
            os = text[len("Distributor ID:\t"):]
            ui_log_area.push(os)

            if os != "Ubuntu":
                ui_log_area.push("not supported yet")
                return False

        # Check os
        ui_log_area.push("Check Release")
        cmd = ["lsb_release", "-r"]
        text = execute_sys_cmd(cmd, ui_log_area)
        if text.startswith("Release:"):
            release = text[len("Release:\t"):]
            ui_log_area.push(release)

            if release != "22.04":
                ui_log_area.push("not supported yet")
                return False

        return True

    # ---

    async def start_worker(self):

        # Create a log area
        ui_og = ui.log().classes('w-full h-96')
        ui_og.move(self.ui_step)

        # Run the worker
        success = False
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(self.worker, ui_og)
            while not future.done():
                await asyncio.sleep(0.5)
            success = future.result()

        if success:
            ui_icon = ui.button('Next', icon='check_circle', color='green', on_click=self.ui_stepper.next)
            ui_icon.move(self.ui_step)
            await asyncio.sleep(1)
            self.ui_stepper.next()

        else:
            ui_icon = ui.avatar('check_circle', color='red', text_color='grey-11', rounded=True)
            ui_icon.move(self.ui_step)


