
from nicegui import ui

from utils.trees import TreeLibrary


class ElementTreeLibrary:


    def __init__(self) -> None:
        
        # ui.upload(on_upload=self.store_new_tree).props('accept=.json').classes('max-w-full')


        trees = TreeLibrary.get_list()
        print(trees)

        columns = [
            {'name': 'name', 'label': 'Name', 'field': 'name', 'required': True, 'align': 'left'},
            {'name': 'age', 'label': 'Age', 'field': 'age', 'sortable': True},
        ]
        rows = [
            {'name': 'Alice', 'age': 18},
            {'name': 'Bob', 'age': 21},
            {'name': 'Carol'},
        ]
        ui.table(columns=columns, rows=rows, row_key='name')

        ui.button("New Tree", on_click=self.create_new_tree)


    def create_new_tree(self):
        TreeLibrary.create_new_tree()



