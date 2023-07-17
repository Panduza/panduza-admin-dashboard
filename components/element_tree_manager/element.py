from nicegui import ui

from components.element_tree_library import ElementTreeLibrary


class ElementTreeManager:


    def __init__(self) -> None:
        

        with ui.element('div').classes('flex w-full'):

            with ui.element('div').classes(''):
                ElementTreeLibrary()

            with ui.element('div').classes(''):
                ui.label('Tree')        
                self.data = [
                    {'id': 'device', 'label': "pokkkk", 'children': [{'id': '1'}, {'id': '2'}]},
                    {'id': 'letters', 'label': "pweshk", 'children': [{'id': 'A'}, {'id': 'B'}]},
                ]
                self.ui_tree = ui.tree(
                    self.data, on_select=self.select)


                self.ui_button = ui.button(text="start", on_click=self.up)





    async def store_new_tree(self, e):
        print(f"pok !! {e.name}")

        text = e.content.read().decode('utf-8')
        print(text)

        # filename="/etc/panduza/tree.json"
        # print(f"Write file: {filename}")
        # os.makedirs(os.path.dirname(filename), exist_ok=True)
        # with open(filename, "w") as f:
        #     f.write(text)



    def select(self, e):
        print(e)

    def up(self):
        self.data[0]['children'].append({'id': 'new_dev'})
        self.ui_tree.update()


