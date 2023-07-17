from nicegui import app, ui
from fastapi.responses import RedirectResponse

from .page import PageControl


def create():
    """Create the home page
    """

    @ui.page('/control')
    def page_control() -> None:
        PageControl()
