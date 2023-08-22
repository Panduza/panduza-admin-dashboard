from nicegui import ui


from panduza import Client, Bps, Dio



class TesterBps:
    
    def __init__(self, name, info) -> None:
        self.name = name
        self.info = info

        self.bps = Bps(addr="localhost", port=1883, topic=self.name)

        with ui.dialog() as self.dialog:
            with ui.card():
                
                with ui.grid(columns=2):
                    ui.number(label='Voltage', value=3.1415927, format='%.2f')
                    ui.button('Apply', on_click=self.dialog.close).disable()

                    ui.number(label='Current', value=3.1415927, format='%.2f')
                        # on_change=lambda e: result.set_text(f'you entered: {e.value}'))
                    ui.button('Apply', on_click=self.dialog.close).disable()

                    self.ui_state_value_label = ui.label('state')
                    ui.button('Toggle', on_click=self.toggle)

                ui.button('Close', on_click=self.dialog.close)

    def toggle(self):
        value = self.bps.enable.value.get()
        if value:
            self.bps.enable.value.set(False)
        else:
            self.bps.enable.value.set(True)
            
        self.ui_state_value_label.set_text(str(self.bps.enable.value.get()))


    def open(self):
        self.dialog.open()


