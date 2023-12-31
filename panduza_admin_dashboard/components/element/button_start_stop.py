
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

        with ui.element('div').classes("flex items-stretch"):
            with ui.element('div').classes("m-2") as self.ui_div_button:
                self.ui_button = ui.button(text="start", on_click=self.action)

            with ui.element('div') as self.ui_status:
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
            self.ui_div_button.clear()
            with self.ui_div_button:
                self.ui_button = ui.button(text="START", on_click=self.action)
                self.ui_button.props('color=green')
            self.ui_label.text = "Platform Inactive"
            self.ui_status.classes(replace="bg-orange-500 p-4")

        elif self.service_state == "active":
            self.ui_div_button.clear()
            with self.ui_div_button:
                self.ui_button = ui.button(text="STOP", on_click=self.action)
                self.ui_button.props('color=red')
            self.ui_label.text = "Platform Active"
            self.ui_status.classes(replace="bg-green-500 p-4")

        elif self.service_state == "failed":
            self.ui_div_button.clear()
            with self.ui_div_button:
                self.ui_button = ui.button(text="START", on_click=self.action)
                self.ui_button.props('color=green')
            self.ui_label.text = "Platform Failed"
            self.ui_status.classes(replace="bg-red-500 p-4")

        # Use just click the button
        # Remove the button and show a spinner
        elif self.service_state == "busy":
            self.ui_div_button.clear()
            with self.ui_div_button:
                ui.spinner('dots', size='lg', color='red')

        else:
            print(f"- Unknown Service State: '{self.service_state}'")

    # ---

    def check_service_activation(self):
        new_status = get_service_activation_status()
        self.change_state(new_status)

    # ---

    def action(self):
        """Execute the action matching the state
        """
        
        # Turn the button as busy before executing the action
        state_before_action = self.service_state
        self.change_state("busy")
    
        # Execute the action
        if state_before_action == "inactive":
            self.action_start()
        elif state_before_action == "active":
            self.action_stop()
        elif state_before_action == "failed":
            self.action_start()
        else:
            print(f"- Error Service State: {state_before_action}")

    # ---

    def action_start(self):
        """Actions triggered when the start button is pressed
        """
        print("+ action_start")

        if get_service_mosquitto_activation_status() != "active":
            cmd = ['systemctl', 'start', "mosquitto.service"]
            text = execute_sys_cmd(cmd)

        cmd = ['systemctl', 'enable', "panduza-py-platform.service"]
        text = execute_sys_cmd(cmd)

        cmd = ['systemctl', 'start', "panduza-py-platform.service"]
        text = execute_sys_cmd(cmd)

        print("- action_start")


    def action_stop(self):
        cmd = ['systemctl', 'disable', "panduza-py-platform.service"]
        text = execute_sys_cmd(cmd)

        cmd = ['systemctl', 'stop', "panduza-py-platform.service"]
        text = execute_sys_cmd(cmd)



