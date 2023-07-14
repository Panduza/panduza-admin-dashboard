
import asyncio
from nicegui import ui

from components.tab_setup import TabSetup
from components.tab_control import TabControl

from utils import execute_sys_cmd

class Dashboard:
    """Main Entry Point
    """

    def __init__(self) -> None:
        pass

    def test(self):
        cmd = ['systemctl', 'is-active', "panduza-py-platform.service"]
        text = execute_sys_cmd(cmd)
        print(">>>>>>>>>>>>>> ", text)

    def start___(self):
        cmd = ['systemctl', 'start', "panduza-py-platform.service"]
        text = execute_sys_cmd(cmd)

    def run(self):
        # HEADER
        with ui.header().classes() as header:

            with ui.splitter(horizontal=False, reverse=False, value=60, on_change=lambda e: ui.notify(e.value)).classes("w-full") as splitter:

                with splitter.before:
                    ui.button(on_click = lambda: self.ui_left_drawer.toggle()).props('flat color=white icon=menu')
                    ui.label("Test dashboard")

                with splitter.after:
                    ui.button(text="start", on_click = lambda: self.start___())

        # 
        with ui.left_drawer() as left_drawer:
            self.ui_left_drawer = left_drawer
            with ui.tabs().classes('w-full').props("vertical") as tabs:
                one = ui.tab('Setup')
                two = ui.tab('Control')

        # 
        with ui.tab_panels(tabs, value=two).classes('w-full'):
            with ui.tab_panel(one):
                tab = TabSetup()
            with ui.tab_panel(two):
                t = TabControl()


        # with ui.footer() as footer:

        #     status_label = ui.markdown()

        #     ui.element("q-space")

        #     # TODO # Indicators
        #     ui.icon("circle", color="red")
        #     ui.label("Status 1")

        #     ui.icon("circle", color="green")
        #     ui.label("Status 2")

        #     self.footer = footer
        #     self.status_label = status_label


        # loop = asyncio.get_running_loop()
        # loop.create_task()

        ui.timer(1.0, lambda: self.test())

        ui.run(title="Panduza Admin Dashboard")

