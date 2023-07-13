from nicegui import ui

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


    def start_platform(self):




        # # Usage example
        # service_name = 'panduza-py-platform.service'
        # logs = get_daemon_logs(service_name)
        # print(logs)



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

        print("==================")

        # cmd = ['systemctl', 'status', "panduza-py-platform.service"]        
        # text = execute_sys_cmd(cmd)
        # print(text)



        # execute_sys_cmd(cmd, ui_log_area)


        # systemctl  application.service

        # auto start
        # sudo systemctl enable application.service
        # sudo systemctl disable application.service

        # start/stop
        # sudo systemctl  application
        # sudo systemctl stop application.service
