#ServerCraft

For python2.7 and django1.8.7
             
Feng Zhang (jumphone@163.com)
             
#Step1: Write a python file: demo.py.
             
from servercraft import *

server_dir = "./"

server_name = "server_center"

app_name = 'app1'

build_server(server_dir, server_name)

add_app(server_dir ,app_name, server_name)

#Step2: Type commands.

python demo.py

cd ./server_center

sh run_server.sh

#Step3: Check it! 

http://127.0.0.1:8000/app1/
