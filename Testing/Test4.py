from disassembler.handlers.base import BaseHandler
from disassembler.core.registry import register,get_handler

@register("LOAD_FAST")
class LoadFastHandler(BaseHandler):
    def handle(self):
        return f"Loading Fast:{self._instruction}"


@register("RETURN_VALUE")  
class ReturnValueHandler(BaseHandler):
    def handle(self):
        return f"Returned"
    

handler_cls=get_handler("LOAD_FAST")

print(handler_cls)

obj=handler_cls("Hello Jimmy")

print(obj.handle())


#Unregistered upcode 

handler_cls=get_handler("RIYUJAKI")
print(handler_cls)