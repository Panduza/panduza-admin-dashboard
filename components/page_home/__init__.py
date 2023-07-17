from nicegui import app, ui
from fastapi.responses import RedirectResponse

def create():
    """Create the home page
    """

    @ui.page('/')
    def page_home() -> None:
        pass
        # ui.label(f'Hello {app.storage.user["username"]}!').classes('text-2xl')
        
        # if not app.storage.user.get('authenticated', False):
        return RedirectResponse('/control')
        # with ui.column().classes('absolute-center items-center'):
        #     ui.label(f'Hello {app.storage.user["username"]}!').classes('text-2xl')
        #     ui.button(on_click=lambda: (app.storage.user.clear(), ui.open('/login')), icon='logout').props('outline round')

