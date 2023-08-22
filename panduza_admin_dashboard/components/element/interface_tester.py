from nicegui import ui

from panduza import Client, Bps, Dio



class DialogTestBps:
    
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

                    ui.label('state')
                    ui.button('Toggle', on_click=self.toggle)

                ui.button('Close', on_click=self.dialog.close)

    def toggle(self):
        value = self.bps.enable.value.get()
        if value:
            self.bps.enable.value.set(False)
        else:
            self.bps.enable.value.set(True)
        print(value)


    def open(self):
        self.dialog.open()



class Row:

    def __init__(self, name, info) -> None:
        self.name = name
        self.info = info
        # print(json.loads(self.info).get("type", ""))
        
        with ui.grid(columns=3):
            ui.label(self.name)
            ui.label(str(self.info))
            ui.button('Test Interface', on_click=self.open_test_interface)


    def open_test_interface(self):
        if str(self.info['type']) == str('bps'):

            print("oookkk ")
            dialog = DialogTestBps(self.name, self.info)
            dialog.open()
        else:
            print("oooo")


class InterfaceTester:

    def __init__(self) -> None:

        ui.button('Refresh', on_click=self.refresh_interfaces)

        self.container = ui.element('div')

    # ---

    def refresh_interfaces(self):
        
        c = Client(url="localhost", port=1883)
        c.connect()
        interfaces = c.scan_interfaces()

        for name, info in interfaces.items():
            r = Row(name, info)



