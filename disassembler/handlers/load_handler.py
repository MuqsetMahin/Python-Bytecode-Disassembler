from disassembler.handlers.base import BaseHandler
from disassembler.core.registry import register

@register("LOAD_FAST")
class LoadFastHandler(BaseHandler):
    def handle(self):
        return f"Load local variable :{self._instruction.argval}"