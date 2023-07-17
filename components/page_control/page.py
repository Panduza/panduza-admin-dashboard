
from nicegui import app, ui


from components.tab_platform_logs import TabPlatformLogs
from components.tab_test import TabTests

from components.button_start_stop import ButtonStartStop


from components.element_tree_manager import ElementTreeManager


class PageControl:

    def __init__(self) -> None:

        # HEADER
        with ui.header().classes() as header:

            with ui.element('div').classes('flex w-full'):
                ui.button(on_click = lambda: self.ui_left_drawer.toggle()).props('flat color=white icon=menu')
                
                
                with ui.tabs().props("horizontal") as tabs:
                        # .classes('w-full')
                    three = ui.tab('Logs')
                    aaa = ui.tab('Test')
                    self.tab_tree = ui.tab('Tree')

                ui.element('div').classes('grow')
                ButtonStartStop()

        # 
        with ui.left_drawer() as left_drawer:
            self.ui_left_drawer = left_drawer


        # 
        with ui.tab_panels(tabs, value=self.tab_tree).classes('w-full'):
        
            with ui.tab_panel(three).classes("h-full"):
                TabPlatformLogs()
            with ui.tab_panel(aaa):
                TabTests()
            with ui.tab_panel(self.tab_tree):
                ElementTreeManager()

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


