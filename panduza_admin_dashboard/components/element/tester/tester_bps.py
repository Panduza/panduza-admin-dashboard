from nicegui import ui
from panduza import Bps


class TesterBps:
    
    def __init__(self, name, info) -> None:
        self.name = name
        self.info = info

        self.bps = Bps(addr="localhost", port=1883, topic=self.name)

        with ui.dialog() as self.dialog:
            with ui.card():
                
                with ui.grid(columns=2):
                    ui.number(label='Voltage', value=3.1415927, format='%.2f', on_change=self.on_voltage_change)
                    self.ui_voltage_apply = ui.button('Apply', on_click=self.apply_voltage_change)
                    self.ui_voltage_apply.disable()

                    ui.number(label='Current', value=3.1415927, format='%.2f', on_change=self.on_current_change)
                    self.ui_current_apply = ui.button('Apply', on_click=self.apply_current_change)
                    self.ui_current_apply.disable()

                    self.ui_state_value_label = ui.label('state')
                    ui.button('Toggle', on_click=self.toggle)

                ui.button('Close', on_click=self.dialog.close)

    # ---

    def on_voltage_change(self, e):
        self.ui_voltage_apply.enable()
        self.voltage_change = e.value

    def apply_voltage_change(self):
    #     self.bps.volts.value.set(self.voltage_change)
        pass

    # ---

    def on_current_change(self, e):
        self.ui_current_apply.enable()
        self.current_change = e.value

    def apply_current_change(self):
    #     self.ammeter.measure.current_cycle.set(self.current_change)
        pass

    # ---

    def toggle(self):
        value = self.bps.enable.value.get()
        if value:
            self.bps.enable.value.set(False)
        else:
            self.bps.enable.value.set(True)
            
        self.ui_state_value_label.set_text(str(self.bps.enable.value.get()))


    def open(self):
        self.dialog.open()


