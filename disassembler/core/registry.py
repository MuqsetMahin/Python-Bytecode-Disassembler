_Handler_Registry={}

def register(opcode_name):
    def wrapper(handler_cls):
        _Handler_Registry[opcode_name]=handler_cls
        return handler_cls
    return wrapper


def get_handler(opcode_name):
    return _Handler_Registry.get(opcode_name)




