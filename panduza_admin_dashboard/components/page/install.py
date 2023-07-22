from nicegui import app, ui
from components.element_installer import ElementInstaller

def create():
    """Create the install page
    """
    @ui.page('/install')
    def page_install() -> None:
        with ui.element('div').classes('flex flex-nowrap w-full place-content-center'):
            ElementInstaller()

