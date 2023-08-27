from nicegui import ui

from panduza import Client, Bpc, Dio

from .tester import TesterBpc
from .tester import TesterAmmeter




class Row:

    def __init__(self, name, info) -> None:
        self.name = name
        self.info = info
        # print(json.loads(self.info).get("type", ""))
        
        with ui.grid(columns=4):
            ui.label(self.name)
            ui.label(str(self.info['type']))
            ui.label(str(self.info['version']))
            ui.button('Test Interface', on_click=self.open_test_interface)


    def open_test_interface(self):
        if str(self.info['type']) == str('Bpc'):
            dialog = TesterBpc(self.name, self.info)
            dialog.open()
        elif str(self.info['type']) == str('ammeter'):
            dialog = TesterAmmeter(self.name, self.info)
            dialog.open()
        else:
            print("not supported")


class InterfaceTester:

    def __init__(self) -> None:

        # ui.button('Refresh', on_click=self.refresh_interfaces)

        self.container = ui.element('div')

    # ---

    def refresh_interfaces(self):

        c = Client(url="localhost", port=1883)
        c.connect()
        interfaces = c.scan_interfaces()

        self.container.clear()
        with self.container:
            for name, info in interfaces.items():
                r = Row(name, info)



