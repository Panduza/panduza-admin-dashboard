from nicegui import ui


from panduza import Ammeter



class TesterAmmeter:
    
    def __init__(self, name, info) -> None:
        self.name = name
        self.info = info

        self.ammeter = Ammeter(addr="localhost", port=1883, topic=self.name)

        self.ammeter.measure.attach_event_listener(self.on_measure_event)

        with ui.dialog() as self.dialog:
            with ui.card():

                with ui.grid(columns=2):

                    self.ui_measure_value = ui.label('0')
                    ui.label('A') 

                    self.ui_measure_polling = ui.number(label='Polling Interval', value=1, step=0.1, format='%.2f', on_change=self.on_polling_change)
                    self.ui_measure_polling_apply = ui.button('Apply', on_click=self.apply_polling_change)
                    self.ui_measure_polling_apply.disable()


                ui.button('Close', on_click=self.dialog.close)

    # ---

    def on_polling_change(self, e):
        # print(e)
        self.ui_measure_polling_apply.enable()
        self.polling_change = e.value

    def apply_polling_change(self):
        self.ammeter.measure.polling_cycle.set(self.polling_change)

    # ---

    def on_measure_event(self, update):
        
        value = update.get("value", None)
        if value:
            self.ui_measure_value.set_text(str(value))

        # polling_cycle = update.get("polling_cycle", None)
        # if polling_cycle:
        #     self.ui_measure_polling.set_value(polling_cycle)



    def open(self):
        self.dialog.open()

    def close(self):
        # self.ammeter.measure.detach_event_listener(self.process_ammeter_events)
        # self.ammeter.
        pass
