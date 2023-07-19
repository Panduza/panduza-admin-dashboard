from nicegui import ui

from utils.tree import TreeFile
from utils.tree import TreeLibrary



model_database = {
    "Hanmatek.Hm310t": {
        "img": "hm310t.jpg",
        "settings": {}
    },
    "Panduza.FakePsu": {
        "img": "fake_psu.jpg",
        "settings": [
            {
                'name': 'number_of_channel',
                'type': 'int'
            }
        ]
    },
    "Panduza.FakeDioController": {
        "img": "fake_dio.jpg",
        "settings": {

        }
    }
}



class ItemDeviceEditor:

    def __init__(self, item) -> None:
        self.item = item

        with ui.element('div').classes('m-4 min-w-full max-w-xl'):
            with ui.card().tight():
                self.ui_image = ui.image('images/none.jpg')
                with ui.element('div').classes('p-4'):
                    ui.input(label='Name', 
                                placeholder='device_name',
                                value=self.item.name,
                                on_change=self.change_name,
                                validation={'Input too long': lambda value: len(value) < 20})

                    choices = ["Hanmatek.Hm310t", "Panduza.FakePsu", "Panduza.FakeDioController"]
                    ui.select(choices, value=self.item.model, on_change=self.change_model)
                    
                    self.ui_settings_container = ui.element('div')


        self.update_model_specifics()

    # ---

    def change_name(self, e):
        self.item.name = e.value
        self.item.notify()
    # ---

    def change_model(self, e):
        # print(e.value)
        self.item.model = e.value
        self.item.notify()

        self.update_model_specifics()

    # ---

    def change_setting(self, name, value):
        # print("change ", name, " ", value)
        self.item.settings[name] = value
        self.item.notify()

    # ---

    def update_model_specifics(self):
        
        params = model_database.get(self.item.model, None)
        if params:
            self.ui_image.source = f'images/{params["img"]}'
            # print(self.ui_image.source)
            self.ui_image.update()

            self.ui_settings_container.clear()

            with self.ui_settings_container:
                
                ui.label("Settings").classes("text-xl mt-2")

                for setting in params["settings"]:

                    if setting['type'] == 'int':
                        default_value = self.item.settings.get(setting['name'], 1)
                        ui.number(label=setting['name'], value=default_value, format='%d',
                            on_change=lambda e: self.change_setting(setting['name'], e.value))


        else:
            self.ui_image.source = 'images/none.jpg'
            self.ui_image.update()

