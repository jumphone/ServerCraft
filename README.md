# servercraft
ServerCraft

#For python2.7 and django1.8.7)
             
Feng Zhang (jumphone@163.com)
             
#demo.py:
             
from servercraft import *
             
server_dir = "./"
             
server_name = "server_center"
             
app_name = 'app1'
            
build_server(server_dir, server_name)
             
add_app(server_dir ,app_name, server_name)
