
from nicegui import ui

from utils.trees import TreeLibrary


class ElementTreeLibrary:


    def __init__(self) -> None:
        

        ui.button("New", on_click=self.create_new_tree)
        ui.button("Import", on_click=self.import_tree)


        self.trees = TreeLibrary.get_list()
        # print(trees)


        # columns = [
        #     {'name': 'name', 'label': 'Name', 'field': 'name', 'required': True, 'align': 'left'},
        # ]
        # self.rows = []
        # for tree in trees:
        #     self.rows.append({'name': tree})

        self.ui_trees_radio = ui.radio(self.trees).props('color=green')


        # self.ui_trees_table = ui.table(columns=columns, rows=self.rows, row_key='name')

        with ui.dialog() as self.dialog, ui.card():
            ui.label('Hello world!')
            ui.button('Close', on_click=self.dialog.close)
            ui.upload().props('accept=.json').classes('max-w-full')
            # on_upload=self.store_new_tree

        
    def create_new_tree(self):
        TreeLibrary.create_new_tree()
        self.trees = TreeLibrary.get_list()
        self.ui_trees_radio.clear()
        self.ui_trees_radio = ui.radio(self.trees)

    def import_tree(self):
        self.dialog.open()
