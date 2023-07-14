
from nicegui import ui

from utils import execute_sys_cmd


class ButtonStartStop:
    """
    """

    def __init__(self) -> None:

        self.service_state = "inactive"

        self.ui_button = ui.button(text="start", on_click=self.start__)

        self.ui_button.text = "stop"

        self.ui_timer = ui.timer(1.0, self.check_service_activation)

        with self.ui_button:
            self.ui_badge = ui.badge('0', color='red').props('floating')


    # ---

    def check_service_activation(self):
        cmd = ['systemctl', 'is-active', "panduza-py-platform.service"]
        text = execute_sys_cmd(cmd)
        self.service_state = text
        print(f"- Service State: {self.service_state}")

        if self.service_state == "inactive":
            pass
        elif self.service_state == "failed":
            pass
        elif self.service_state == "failed":
            pass
        else:
            print(f"- Service State: {self.service_state}")


    # ---

    def start__(self):
        print("----")
        cmd = ['systemctl', 'start', "panduza-py-platform.service"]
        text = execute_sys_cmd(cmd)



