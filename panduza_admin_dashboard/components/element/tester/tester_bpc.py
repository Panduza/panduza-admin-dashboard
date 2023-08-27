from nicegui import ui
from panduza import Bpc


class TesterBpc:
    
    def __init__(self, name, info) -> None:
        self.name = name
        self.info = info

        self.bpc = Bpc(addr="localhost", port=1883, topic=self.name)

        self.bpc.enable.attach_event_listener(self.on_enable_event)
        self.bpc.voltage.attach_event_listener(self.on_voltage_event)
        self.bpc.current.attach_event_listener(self.on_current_event)


        with ui.dialog() as self.dialog:
            with ui.card():
                
                with ui.grid(columns=2):
                    ui.number(label='Voltage', value=self.bpc.voltage.value.get(), format='%.2f', on_change=self.on_voltage_change)
                    self.ui_voltage_apply = ui.button('Apply', on_click=self.apply_voltage_change)
                    self.ui_voltage_apply.disable()

                    ui.number(label='Current', value=self.bpc.current.value.get(), format='%.2f', on_change=self.on_current_change)
                    self.ui_current_apply = ui.button('Apply', on_click=self.apply_current_change)
                    self.ui_current_apply.disable()

                    state = self.bpc.enable.value.get()
                    self.ui_state_value_label = ui.label(str(state))
                    ui.button('Toggle', on_click=self.toggle)

                ui.button('Close', on_click=self.dialog.close)



    def on_enable_event(self, update):
        print(update)

    def on_voltage_event(self, update):
        print(update)

    def on_current_event(self, update):
        print(update)

    # ---

    def on_voltage_change(self, e):
        self.ui_voltage_apply.enable()
        self.voltage_change = e.value

    def apply_voltage_change(self):
    #     self.bpc.volts.value.set(self.voltage_change)
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
        value = self.bpc.enable.value.get()
        if value:
            self.bpc.enable.value.set(False)
        else:
            self.bpc.enable.value.set(True)
            
        self.ui_state_value_label.set_text(str(self.bpc.enable.value.get()))


    def open(self):
        self.dialog.open()


