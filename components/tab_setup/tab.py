
from nicegui import ui

import threading
import subprocess
import time 
import asyncio


class StepSystemControl:

    def __init__(self) -> None:
        
        with ui.step('System check') as step_1:

            # step_1.on_enabled_change = self.__on_enabled_change
            self.step_1 = step_1
            ui.button("Check system", on_click=self.__on_enabled_change)


    def my_thread(self):
        # Code to be executed in the thread
        print("Thread started")
        # Do some work...
        time.sleep(3)
        print("Thread finished")


    async def __on_enabled_change(self):
        print("llll")
        # self.step_1.clear()
        # ui.button('Click me!', on_click=lambda: ui.notify(f'You clicked me!'))

        log = ui.log().classes('w-full h-20')
        


        # Create a thread object
        thread = threading.Thread(target=self.my_thread)

        # Start the thread
        thread.start()

        log.push("start !!!!")

        # Check if the thread is alive in a loop
        while thread.is_alive():
            # Do other work here, or simply wait
            
            await asyncio.sleep(0.2)
            log.push("wait !!!!")


        log.push("endd !!!!")


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

        




class TabSetup:


    def jjjj(self, value):
        print("ppppp", value)


    def __init__(self) -> None:
        
        with ui.stepper().props('vertical').classes('w-full') as stepper:
            
            StepSystemControl()


            with ui.step('Bake'):
                ui.label('Bake for 20 minutes')
                with ui.stepper_navigation():
                    ui.button('Done', on_click=lambda: ui.notify('Yay!', type='positive'))
                    ui.button('Back', on_click=stepper.previous).props('flat')




