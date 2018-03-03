from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import os

#https://docs.python.org/2/library/simplexmlrpcserver.html

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

server = SimpleXMLRPCServer(("localhost", 8000),
                            requestHandler=RequestHandler,
                allow_none=True)

server.register_introspection_functions()

def shellquote(s):
    return "'" + s.replace("'", "'\\''") + "'"

def add_user_func(name, password):
    os.system("./add-user.sh " + shellquote(name) + " " + shellquote(password))
    
def change_user_func(name, password):
    os.system("./change-user-pass.sh " + shellquote(name) + " " + shellquote(password))

server.register_function(add_user_func, 'add_user')
server.register_function(change_user_func, 'change_user')

server.serve_forever()

