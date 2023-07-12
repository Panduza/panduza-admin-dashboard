from nicegui import ui

import threading
import subprocess
import time 
import asyncio
import concurrent
import os
import platform


# f platform.system() == “Linux”:
#      print(“Linux”)




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


class StepSystemControl:

    # ---

    def __init__(self, stepper) -> None:
        # Parent Stepper
        self.ui_stepper = stepper

        # Build ui
        with ui.step('System check') as step:

            # step.on_enabled_change = self.__on_enabled_change
            self.ui_step = step
            ui.button("Check system", on_click=self.__start_worker)

    # ---

    def worker(self, ui_log_area):

        # Check distribution
        ui_log_area.push("Check Distribution")
        cmd = ["lsb_release", "-i"]
        text = execute_sys_cmd(cmd, ui_log_area)
        if text.startswith("Distributor ID:"):
            os = text[len("Distributor ID:\t"):]
            ui_log_area.push(os)

            if os != "ubuntu":
                return False

        # Check os
        ui_log_area.push("Check Release")
        cmd = ["lsb_release", "-r"]
        text = execute_sys_cmd(cmd, ui_log_area)
        if text.startswith("Release:"):
            release = text[len("Release:\t"):]
            ui_log_area.push(release)

            if release != "22.04":
                return False

        return True

    # ---

    async def __start_worker(self):
        # Create a log area
        ui_og = ui.log().classes('w-full h-96')
        
        # Run the worker
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(self.worker, ui_og)
            while not future.done():
                await asyncio.sleep(0.5)
            result = future.result()

        
        ui_icon = ui.avatar('check_circle', color='green', text_color='grey-11', rounded=True)

        await asyncio.sleep(2)
        self.ui_step.remove(ui_og)
        self.ui_step.remove(ui_icon)
        
        # self.ui_stepper.next() 



        # # Create a thread object
        # thread = threading.Thread(target=self.my_thread)

        # # Start the thread
        # thread.start()

        # log.push("start !!!!")

        # # Check if the thread is alive in a loop
        # while thread.is_alive():
        #     # Do other work here, or simply wait
            
        #     await asyncio.sleep(0.2)
        #     log.push("wait !!!!")


        # log.push("endd !!!!")

        # # self.step.remove(0)
            

        # cmd = ["apt-get", "update"]
        # process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # # Read the output and error streams
        # while True:
        #     # Poll the process to check if it has terminated
        #     poll = process.poll()
        #     if poll is not None:
        #         break

        #     # Read stdout and stderr
        #     output = process.stdout.readline().decode().strip()
        #     error = process.stderr.readline().decode().strip()

        #     # Print the output and error
        #     if output:
        #         print("Output:", output)
        #     if error:
        #         print("Error:", error)

        # # Check if there is any remaining output or error
        # remaining_output = process.stdout.read().decode().strip()
        # remaining_error = process.stderr.read().decode().strip()
        # if remaining_output:
        #     print("Remaining Output:", remaining_output)
        # if remaining_error:
        #     print("Remaining Error:", remaining_error)

        # # Get the return code of the process
        # return_code = process.returncode
        # print("Return Code:", return_code)


        # # for line in process.stdout:
        # #     log.push(line)

        


