
from nicegui import app, ui
from fastapi.responses import RedirectResponse

from utils.system.checker import get_osv
from utils.system.checker import get_panduza_version
from utils.system.checker import get_panduza_platform_version


class RequirementsChecker:

    def __init__(self) -> None:

        with ui.card().tight():
            with ui.element('div').classes('p-4'):
                ui.label('System Requirement Check').classes("text-2xl")
                ui.separator().classes("mb-4")
                with ui.grid(columns=2):
                    
                    ui.label('System').classes("text-xl")
                    with ui.element('div') as self.div_system:
                        ui.spinner(size='2em')

                    ui.label('Panduza').classes("text-xl")
                    with ui.element('div') as self.div_panduza:
                        ui.spinner(size='2em')

                    ui.label('Panduza Platform').classes("text-xl")
                    with ui.element('div') as self.div_panduza_platform:
                        ui.spinner(size='2em')

                    ui.label('Mosquitto').classes("text-xl")
                    ui.spinner(size='2em')

                    ui.label('Systemd').classes("text-xl")
                    ui.spinner(size='2em')

                ui.button("installation page", on_click=lambda: ui.open("/install"))


        self.timer = ui.timer(0.1, self.check_system)

    # ---

    def check_system(self):
        self.timer.deactivate()
        osv = get_osv()
        self.div_system.clear()
        with self.div_system:
            ui.label(str(osv))
        self.timer.callback = self.check_panduza
        self.timer.activate()

    # ---

    def check_panduza(self):
        self.timer.deactivate()
        version = get_panduza_version()
        self.div_panduza.clear()
        with self.div_panduza:
            ui.label(str(version))
        self.timer.callback = self.check_panduza_platform
        self.timer.activate()

    # ---

    def check_panduza_platform(self):
        self.timer.deactivate()
        version = get_panduza_platform_version()
        self.div_panduza_platform.clear()
        with self.div_panduza_platform:
            ui.label(str(version))
        self.timer.callback = self.next_step_2
        self.timer.activate()

    # ---

    def next_step_2(self):
        print("ok 2")
        # ui.label("oooo 222")
        self.timer.deactivate()

