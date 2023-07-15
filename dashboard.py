
import asyncio
from nicegui import ui

from components.tab_setup import TabSetup
from components.tab_control import TabControl
from components.tab_platform_logs import TabPlatformLogs
from components.tab_test import TabTests

from components.button_start_stop import ButtonStartStop



from utils import execute_sys_cmd


from fastapi.responses import RedirectResponse

from nicegui import app, ui

# # in reality users passwords would obviously need to be hashed
# passwords = {'user1': 'pass1', 'user2': 'pass2'}



# @ui.page('/')
# def main_page() -> None:
#     if not app.storage.user.get('authenticated', False):
#         return RedirectResponse('/login')
#     with ui.column().classes('absolute-center items-center'):
#         ui.label(f'Hello {app.storage.user["username"]}!').classes('text-2xl')
#         ui.button(on_click=lambda: (app.storage.user.clear(), ui.open('/login')), icon='logout').props('outline round')


# @ui.page('/login')
# def login() -> None:
#     def try_login() -> None:  # local function to avoid passing username and password as arguments
#         if passwords.get(username.value) == password.value:
#             app.storage.user.update({'username': username.value, 'authenticated': True})
#             ui.open('/')
#         else:
#             ui.notify('Wrong username or password', color='negative')

#     if app.storage.user.get('authenticated', False):
#         return RedirectResponse('/')
#     with ui.card().classes('absolute-center'):
#         username = ui.input('Username').on('keydown.enter', try_login)
#         password = ui.input('Password', password=True, password_toggle_button=True).on('keydown.enter', try_login)
#         ui.button('Log in', on_click=try_login)


class Dashboard:
    """Main Entry Point
    """

    def __init__(self) -> None:
        pass


    def start___(self):
        print("----")
        cmd = ['systemctl', 'start', "panduza-py-platform.service"]
        text = execute_sys_cmd(cmd)

    def run(self):
        # HEADER
        with ui.header().classes() as header:


            with ui.element('div').classes('flex w-full'):

            # with ui.splitter(horizontal=False, reverse=False, value=60, on_change=lambda e: ui.notify(e.value)).classes("w-full") as splitter:


                ui.button(on_click = lambda: self.ui_left_drawer.toggle()).props('flat color=white icon=menu')


                ui.element('div').classes('grow')


                ButtonStartStop()

        # 
        with ui.left_drawer() as left_drawer:
            self.ui_left_drawer = left_drawer
            with ui.tabs().classes('w-full').props("vertical") as tabs:
                one = ui.tab('Setup')
                two = ui.tab('Control')
                three = ui.tab('Logs')
                aaa = ui.tab('Test')

        # 
        with ui.tab_panels(tabs, value=two).classes('w-full'):
            with ui.tab_panel(one):
                tab = TabSetup()
            with ui.tab_panel(two):
                t = TabControl()
            with ui.tab_panel(two):
                t = TabControl()
            with ui.tab_panel(three).classes("h-full"):
                TabPlatformLogs()
            with ui.tab_panel(aaa):
                TabTests()

        # with ui.footer() as footer:

        #     status_label = ui.markdown()

        #     ui.element("q-space")

        #     # TODO # Indicators
        #     ui.icon("circle", color="red")
        #     ui.label("Status 1")

        #     ui.icon("circle", color="green")
        #     ui.label("Status 2")

        #     self.footer = footer
        #     self.status_label = status_label


        # loop = asyncio.get_running_loop()
        # loop.create_task()


        ui.run(title="Panduza Admin Dashboard")
            #    storage_secret='THIS_NEEDS_TO_BE_CHANGED')

