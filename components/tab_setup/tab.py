from nicegui import ui

from .step_system_control import StepSystemControl


class TabSetup:


    def jjjj(self, value):
        print("ppppp", value)


    def __init__(self) -> None:
        
        with ui.stepper().props('vertical').classes('w-full') as stepper:
            
            StepSystemControl(stepper)


            with ui.step('Bake'):
                ui.label('Bake for 20 minutes')
                with ui.stepper_navigation():
                    ui.button('Done', on_click=lambda: ui.notify('Yay!', type='positive'))
                    ui.button('Back', on_click=stepper.previous).props('flat')




