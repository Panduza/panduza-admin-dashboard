from nicegui import app, ui

import components.page_home as PageHome
import components.page_install as PageInstall



PageHome.create()
PageInstall.create()

ui.run( title="Panduza Admin Dashboard",
        storage_secret='THIS_NEEDS_TO_BE_CHANGED')





# from dashboard import Dashboard




# #!/usr/bin/env python3
# """This is just a very simple authentication example.

# Please see the `OAuth2 example at FastAPI <https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/>`_  or
# use the great `Authlib package <https://docs.authlib.org/en/v0.13/client/starlette.html#using-fastapi>`_ to implement a classing real authentication system.
# Here we just demonstrate the NiceGUI integration.
# """
# from fastapi.responses import RedirectResponse


# # in reality users passwords would obviously need to be hashed
# passwords = {'user1': 'pass1', 'user2': 'pass2'}



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




# @ui.page('/control')
# def login() -> None:
#     dashboard = Dashboard()


