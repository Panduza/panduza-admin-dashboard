

from nicegui import ui

from components.tab_setup import TabSetup

class Dashboard:
    """Main Entry Point
    """


    def __init__(self) -> None:
        pass


    def run(self):

        # HEADER
        with ui.header().classes(replace="row items-center") as header:
            # ui.button(on_click = lambda: uiobjs.left_drawer.toggle()).props('flat color=white icon=menu')
            ui.label("Test dashboard")


        tab = TabSetup()


        with ui.footer() as footer:

            status_label = ui.markdown()

            ui.element("q-space")

            # TODO # Indicators
            ui.icon("circle", color="red")
            ui.label("Status 1")

            ui.icon("circle", color="green")
            ui.label("Status 2")

            self.footer = footer
            self.status_label = status_label


        ui.run()
