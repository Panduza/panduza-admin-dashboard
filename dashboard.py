
import asyncio
from nicegui import ui

# from components.element_installer import TabSetup
from components.tab_control import TabControl
from components.tab_platform_logs import TabPlatformLogs
from components.tab_test import TabTests

from components.button_start_stop import ButtonStartStop



from utils import execute_sys_cmd


from fastapi.responses import RedirectResponse

from nicegui import app, ui



class Dashboard:
    """Main Entry Point
    """

    def __init__(self) -> None:
        # HEADER
        with ui.header().classes() as header:


            with ui.element('div').classes('flex w-full'):

            # with ui.splitter(horizontal=False, reverse=False, value=60, on_change=lambda e: ui.notify(e.value)).classes("w-full") as splitter:


                ui.button(on_click = lambda: self.ui_left_drawer.toggle()).props('flat color=white icon=menu')


                ui.element('div').classes('grow')


                ButtonStartStop()

        # 
        with ui.left_drawer() as left_drawer:
            self.ui_left_drawer = left_drawer
            with ui.tabs().classes('w-full').props("vertical") as tabs:
                one = ui.tab('Setup')
                two = ui.tab('Control')
                three = ui.tab('Logs')
                aaa = ui.tab('Test')

        # 
        with ui.tab_panels(tabs, value=two).classes('w-full'):
            # with ui.tab_panel(one):
                # tab = TabSetup()
            with ui.tab_panel(two):
                t = TabControl()
            with ui.tab_panel(two):
                t = TabControl()
            with ui.tab_panel(three).classes("h-full"):
                TabPlatformLogs()
            with ui.tab_panel(aaa):
                TabTests()

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


    def start___(self):
        print("----")
        cmd = ['systemctl', 'start', "panduza-py-platform.service"]
        text = execute_sys_cmd(cmd)
