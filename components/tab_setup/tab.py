from nicegui import ui

from .step_system_control import StepSystemControl
from .step_setup_panduza import StepSetupPanduza

class TabSetup:


    def __init__(self) -> None:

        self.steps = {}

        with ui.stepper().props('vertical').classes('w-full') as stepper:

            StepSystemControl(stepper)
            StepSetupPanduza(stepper)

