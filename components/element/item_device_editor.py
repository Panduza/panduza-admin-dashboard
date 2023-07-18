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
                     on_change=self.change_name,
                     validation={'Input too long': lambda value: len(value) < 20})

            choices = ["Hanmatek.Hm310t", "Panduza.FakePsu", "Panduza.FakeDioController"]
            select1 = ui.select(choices, value=self.item.model, on_change=self.change_model)

    # ---

    def change_name(self, e):
        self.item.name = e.value
        self.item.notify()
    # ---

    def change_model(self, e):
        print(e.value)
        self.item.model = e.value
        self.item.notify()


