
from nicegui import ui

from utils import execute_sys_cmd
from utils import get_service_activation_status
from utils.system.checker import get_service_mosquitto_activation_status

class ButtonStartStop:
    """
    """

    def __init__(self) -> None:

        # State Management
        self.previous_state = None
        self.service_state = get_service_activation_status()

        self.ui_button = ui.button(text="start", on_click=self.action)

        with ui.element('div').classes('flex mx-4 p-4') as status:
            self.ui_status = status
            self.ui_label = ui.label('inside a colored div')

        self.ui_timer = ui.timer(1.0, self.check_service_activation)

        self.update_button()

    # ---

    def change_state(self, new_state):
        # Check that new state is different from the current one
        if new_state == self.service_state:
            return

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
            self.ui_status.classes("bg-orange-500")

        elif self.service_state == "active":
            self.ui_button.text = "STOP"
            self.ui_button.props('color=red')
            self.ui_label.text = "Platform Active"
            self.ui_status.classes("bg-green-500")

        elif self.service_state == "failed":
            self.ui_button.text = "START"
            self.ui_button.props('color=green')
            self.ui_label.text = "Platform Failed"
            self.ui_status.classes("bg-red-500")

        else:
            print(f"- Unknown Service State: '{self.service_state}'")

    # ---

    def check_service_activation(self):
        new_status = get_service_activation_status()
        self.change_state(new_status)

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

    # ---

    def action_start(self):
        """Actions triggered when the start button is pressed
        """
        print("+ action_start")

        if get_service_mosquitto_activation_status() != "active":
            cmd = ['systemctl', 'start', "mosquitto.service"]
            text = execute_sys_cmd(cmd)

        cmd = ['systemctl', 'start', "panduza-py-platform.service"]
        text = execute_sys_cmd(cmd)

        print("- action_start")


    def action_stop(self):
        # print("---- stop")
        cmd = ['systemctl', 'stop', "panduza-py-platform.service"]
        text = execute_sys_cmd(cmd)



