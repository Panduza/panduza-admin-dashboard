
from nicegui import ui

from utils.trees import TreeLibrary


class ElementTreeLibrary:


    def __init__(self, on_tree_change = None) -> None:
        self.on_tree_change = on_tree_change

        ui.button("New", on_click=self.create_new_tree)
        # ui.button("Import", on_click=self.import_tree)


        self.trees = TreeLibrary.get_list()
        # print(trees)


        # columns = [
        #     {'name': 'name', 'label': 'Name', 'field': 'name', 'required': True, 'align': 'left'},
        # ]
        # self.rows = []
        # for tree in trees:
        #     self.rows.append({'name': tree})

        with ui.element('div').classes('') as self.radio_container:
            self.ui_trees_radio = ui.radio(self.trees, on_change=self.change_selected_tree).props('color=green')


        # self.ui_trees_table = ui.table(columns=columns, rows=self.rows, row_key='name')

        with ui.dialog() as self.dialog, ui.card():
            ui.label('Hello world!')
            ui.button('Close', on_click=self.dialog.close)
            ui.upload().props('accept=.json').classes('max-w-full')
            # on_upload=self.store_new_tree


    def change_selected_tree(self, e):
        if self.on_tree_change:
            self.on_tree_change(e.value)


    def create_new_tree(self):
        TreeLibrary.create_new_tree()
        self.radio_container.remove(self.ui_trees_radio)
        self.trees = TreeLibrary.get_list()
        self.ui_trees_radio = ui.radio(self.trees)
        self.ui_trees_radio.move(self.radio_container)

    def import_tree(self):
        self.dialog.open()
