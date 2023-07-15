
from nicegui import ui

from utils import execute_sys_cmd


class ButtonStartStop:
    """
    """

    def __init__(self) -> None:

        # State Management
        self.previous_state = None
        self.service_state = "inactive"

        self.ui_button = ui.button(text="start", on_click=self.action)

        with ui.element('div').classes('flex bg-cyan-500 items-stretch'):
            self.ui_label = ui.label('inside a colored div').classes("self-auto")
            self.ui_icon  = ui.icon('thumb_up').classes("self-auto")

        self.ui_timer = ui.timer(1.0, self.check_service_activation)

        self.update_button()

    # ---

    def change_state(self, new_state):
        self.previous_state = self.service_state
        self.service_state = new_state
        self.update_button()

    # ---

    def update_button(self):
        """
        """
        if self.service_state == "inactive":
            self.ui_button.text = "START"
            self.ui_button.props('color=green')
            self.ui_label.text = "Platform Inactive"

        elif self.service_state == "active":
            self.ui_button.text = "STOP"
            self.ui_button.props('color=red')
            self.ui_label.text = "Platform Active"

        elif self.service_state == "failed":
            self.ui_button.text = "START"
            self.ui_button.props('color=green')
            self.ui_label.text = "Platform Failed"

        else:
            print(f"- Service State: {self.service_state}")

    # ---

    def check_service_activation(self):
        cmd = ['systemctl', 'is-active', "panduza-py-platform.service"]
        text = execute_sys_cmd(cmd)
        print(f"- Service State: {self.service_state}")
        self.change_state(text)

    # ---

    def action(self):
        if self.service_state == "inactive":
            self.action_start()
        elif self.service_state == "active":
            self.action_stop()
        elif self.service_state == "failed":
            self.action_start()
        else:
            print(f"- Error Service State: {self.service_state}")


    def action_start(self):
        # print("---- start")
        cmd = ['systemctl', 'start', "panduza-py-platform.service"]
        text = execute_sys_cmd(cmd)

    def action_stop(self):
        # print("---- stop")
        cmd = ['systemctl', 'stop', "panduza-py-platform.service"]
        text = execute_sys_cmd(cmd)



