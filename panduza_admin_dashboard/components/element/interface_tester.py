from nicegui import ui

from panduza import Client, Bps, Dio

from .tester import TesterBps




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
            dialog = TesterBps(self.name, self.info)
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



