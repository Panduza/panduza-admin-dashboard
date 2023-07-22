from nicegui import ui

from .step_system_control import StepSystemControl
from .step_setup_panduza import StepSetupPanduza



class ElementInstaller:


    def __init__(self) -> None:


        with ui.stepper().props('vertical').classes('w-full') as stepper:

            StepSystemControl(stepper)
            StepSetupPanduza(stepper)


            with ui.step("Installation ok !") as step:
                ui.label('You can now use the platform')
                with ui.stepper_navigation() as nav:
                    ui.button('Back', on_click=stepper.previous).props('flat')
