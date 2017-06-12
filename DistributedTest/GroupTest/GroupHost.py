from pyactor.context import set_context, create_host, serve_forever
from Group import *

if __name__ == "__main__":
    set_context()
    host = create_host('http://127.0.0.1:2220/')
    group = host.spawn('group', Group)
    group.init_start()
    serve_forever()
