
from nicegui import app, ui
from fastapi.responses import RedirectResponse

from utils.system.checker import get_panduza_version
from utils.system.checker import get_panduza_platform_version


class RequirementsChecker:

    def __init__(self) -> None:

        with ui.card().tight():
            with ui.element('div').classes('p-4'):
                ui.label('System Requirement Check').classes("text-2xl")
                ui.separator().classes("mb-4")
                with ui.grid(columns=2):
                    ui.label('Panduza').classes("text-xl")
                    with ui.element('div') as self.panduza_div:
                        ui.spinner(size='2em')

                    ui.label('Panduza Platform').classes("text-xl")
                    with ui.element('div') as self.panduza_platform_div:
                        ui.spinner(size='2em')

                    ui.label('Mosquitto').classes("text-xl")
                    ui.spinner(size='2em')

                    ui.label('Systemd').classes("text-xl")
                    ui.spinner(size='2em')

                ui.button("installation page", on_click=lambda: ui.open("/install"))


        self.timer = ui.timer(0.1, self.check_panduza)

    # ---

    def check_panduza(self):
        self.timer.deactivate()

        version = get_panduza_version()
        self.panduza_div.clear()

        with self.panduza_div:
            ui.label(str(version))

        self.timer.callback = self.check_panduza_platform
        self.timer.activate()

    # ---

    def check_panduza_platform(self):
        self.timer.deactivate()

        version = get_panduza_platform_version()
        self.panduza_platform_div.clear()

        with self.panduza_platform_div:
            ui.label(str(version))

        self.timer.callback = self.next_step_2
        self.timer.activate()

    # ---

    def next_step_2(self):
        print("ok 2")
        # ui.label("oooo 222")
        self.timer.deactivate()

