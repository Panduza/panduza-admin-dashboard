from nicegui import ui

import os
import asyncio
import subprocess


def get_daemon_logs(service_name):
    command = ['journalctl', '-u', service_name]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    
    if process.returncode == 0:
        # Logs were retrieved successfully
        logs = output.decode('utf-8')
        return logs
    else:
        # There was an error retrieving the logs
        error_message = error.decode('utf-8')
        return f"Error retrieving logs: {error_message}"



def execute_sys_cmd(cmd):

    # ui_log_area.push(f"---\n\t$> {cmd}")

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
                # ui_log_area.push(f"\t{output}")
            else:
                data_available = False
        

        data_available = True
        while data_available:
            error = process.stderr.readline().decode().strip()
            if error:
                text += error
                # ui_log_area.push(f"\t{error}")
            else:
                data_available = False
                
    # ui_log_area.push("---")

    return text



class TabControl:



    def __init__(self) -> None:

        ui.button('Start', on_click=self.start_platform)

        ui.upload(on_upload=self.store_new_tree).props('accept=.json').classes('max-w-full')

        with ui.scroll_area():
            md = ui.html("pppp </br>")

        for i in range (1,300):
            md.content += "<b>pok</b></br>"


    async def store_new_tree(self, e):
        print(f"pok !! {e.name}")

        text = e.content.read().decode('utf-8')
        print(text)

        filename="/etc/panduza/tree.json"
        print(f"Write file: {filename}")
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as f:
            f.write(text)



    async def start_platform(self):

        # cmd = ['systemctl', 'is-active', "panduza-py-platform.service"]        
        # text = execute_sys_cmd(cmd)
        # print(">>>>>>>>>>>>>> ", text)

        # print("==================")

        # cmd = ['systemctl', 'status', "panduza-py-platform.service"]        
        # text = execute_sys_cmd(cmd)
        # print(text)

        print("==================")

        cmd = ['systemctl', 'start', "panduza-py-platform.service"]
        text = execute_sys_cmd(cmd)
        print(text)

        # print("==================")

        # await asyncio.sleep(2)

        # cmd = ['systemctl', 'status', "panduza-py-platform.service"]        
        # text = execute_sys_cmd(cmd)
        # print(text)


        # # Usage example
        # service_name = 'panduza-py-platform.service'
        # logs = get_daemon_logs(service_name)
        # print(logs)


        # execute_sys_cmd(cmd, ui_log_area)


        # systemctl  application.service

        # auto start
        # sudo systemctl enable application.service
        # sudo systemctl disable application.service

        # start/stop
        # sudo systemctl  application
        # sudo systemctl stop application.service
