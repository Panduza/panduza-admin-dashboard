from nicegui import ui

import os
import asyncio
import subprocess


def get_daemon_logs(service_name):

    command = ['journalctl', '-u', service_name, "-n", "100", "--no-pager"]
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





class TabPlatformLogs:

    def __init__(self) -> None:


        self.ui_md = ui.html()


        # self.ui_timer = ui.timer(0.5, self.refresh_content)


    def refresh_content(self):

        service_name = 'panduza-py-platform.service'
        logs = get_daemon_logs(service_name)
        for line in logs.splitlines():
            self.ui_md.content += f"{line}</br>"




