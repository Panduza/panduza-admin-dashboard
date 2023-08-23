from nicegui import app, ui
from fastapi.responses import RedirectResponse

from components.tab_platform_logs import TabPlatformLogs


from components.element import StatusAera
from components.element import TreeManager
from components.element import InterfaceTester
from components.element.button_start_stop import ButtonStartStop


from utils.system.checker import get_service_activation_status

# -----------------------------------------------------------------------------

class PageControl:

    def __init__(self) -> None:

        # State Management
        self.previous_state = None
        self.service_state = None

        # HEADER
        with ui.header().classes():
            with ui.element('div').classes('flex w-full'):
        
                # Tab navigation
                with ui.tabs().props("horizontal") as self.tabs:
                    self.tab_tree = ui.tab('Tree')
                    self.tab_status = ui.tab('Status')
                    self.tab_control = ui.tab('Control')

                # Middle separator
                ui.element('div').classes('grow')

                # Start/Stop button
                ButtonStartStop()

        # BODY
        with ui.tab_panels(self.tabs, value=self.tab_tree).classes('w-full') as self.tab_panels:
        
            with ui.tab_panel(self.tab_status).classes("h-full"):
                self.status_area = StatusAera()
            with ui.tab_panel(self.tab_control):
                self.tester = InterfaceTester()
            with ui.tab_panel(self.tab_tree):
                TreeManager()

        # Start checks
        self.ui_timer = ui.timer(0.5, self.check_platform_activation_status)

    # ---

    def check_platform_activation_status(self):
        new_status = get_service_activation_status()
        self.change_state(new_status)

    # ---

    def change_state(self, new_state):
        # Check that new state is different from the current one
        if new_state == self.service_state:
            return

        self.previous_state = self.service_state
        self.service_state = new_state

        if self.service_state == "inactive":
            self.status_area.update_content()
            self.tab_tree.enable()
            self.tab_status.enable()
            self.tab_control.disable()
            self.tab_panels.value = self.tab_tree
            self.tab_panels.update()

        elif self.service_state == "active":
            self.tab_tree.disable()
            self.tab_status.disable()
            self.tab_control.enable()
            self.tab_panels.value = self.tab_control
            self.tester.refresh_interfaces()
            self.tab_panels.update()

        elif self.service_state == "failed":

            self.status_area.update_content()
            self.tab_tree.enable()
            self.tab_status.enable()
            self.tab_control.disable()
            self.tab_panels.value = self.tab_status
            self.tab_panels.update()

        else:
            print(f"- Unknown Service State: '{self.service_state}'")


# -----------------------------------------------------------------------------

def create():
    """Create the home page
    """

    @ui.page('/control')
    def page_control() -> None:
        PageControl()

