from nicegui import ui

from utils.tree import TreeFile
from utils.tree import TreeLibrary




class ElementItemDeviceEditor:

    def __init__(self, item) -> None:


        self.container = ui.element('div').classes('m-4')

        with self.container:
            ui.input(label='Name', 
                     placeholder='start typing',
                     value=item["name"],
                     on_change=lambda e: print(e),
                     validation={'Input too long': lambda value: len(value) < 20})

            select1 = ui.select(["Hanmatek.Hm310t", "Panduza.FakePsu", "Panduza.FakeDioController"], value=1)

    #         ui.separator()




