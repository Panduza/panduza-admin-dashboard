from nicegui import app, ui
from components.element_installer import ElementInstaller

def create():
    """Create the install page
    """
    @ui.page('/install')
    def page_install() -> None:
        ElementInstaller()

