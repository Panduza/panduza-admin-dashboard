from nicegui import ui

from .step_system_control import StepSystemControl
from .step_setup_panduza import StepSetupPanduza

class TabSetup:


    def __init__(self) -> None:
        
        with ui.stepper().props('vertical').classes('w-full') as stepper:
            
            StepSystemControl(stepper)
            StepSetupPanduza(stepper)


            with ui.step('Bake'):
                ui.label('Bake for 20 minutes')


# try:
#         panduza_platform_version = pkg_resources.get_distribution("panduza_platform").version
#         ui_log_area.push(panduza_platform_version)
    

