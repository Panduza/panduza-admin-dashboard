

from dashboard import Dashboard




dashboard = Dashboard()
dashboard.run()



# # install 

# # load/save trees
# # start/stop platform
# # configuration du tree



# from panduza import Client, Psu
# import json



# client = Client(url="localhost", port=1883)
# client.connect()

# interfaces = client.scan_interfaces()




# print(interfaces)




# class Row:

#     def __init__(self, name, info) -> None:
#         self.name = name
#         self.info = info
#         # print(json.loads(self.info).get("type", ""))

#     def test(self):
#         ui.notify(f'You clicked me!')
#         cmd = 'apt-get update'
#         process = subprocess.Popen(cmd, shell=True)
#         process.wait()




#     def run(self):
#         ui.label(self.name)
#         ui.label(str(self.info))
#         ui.button('Test !', on_click=self.test)



# class Page:


#     def run(self):

#         ui.label("pok")

#         with ui.grid(columns=3):

#             for name, info in interfaces.items():
#                 r = Row(name, info)
#                 r.run()


# p = Page()

# p.run()


# ui.run()


