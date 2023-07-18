from nicegui import ui

from utils.tree import TreeFile
from utils.tree import TreeLibrary




class ItemDeviceEditor:

    def __init__(self, item) -> None:
        self.item = item

        self.container = ui.element('div').classes('m-4')

        with self.container:
            ui.input(label='Name', 
                     placeholder='device_name',
                     value=self.item.name,
                     on_change=self.on_name_update,
                     validation={'Input too long': lambda value: len(value) < 20})

            select1 = ui.select(["Hanmatek.Hm310t", "Panduza.FakePsu", "Panduza.FakeDioController"], value=1)

    # ---

    def on_name_update(self, e):
        self.item.name = e.value
        self.item.notify()





