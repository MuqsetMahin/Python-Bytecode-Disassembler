from disassembler.handlers.base import BaseHandler
from disassembler.core.registry import register

@register("RETURN_VALUE")
class ReturnValueHandler(BaseHandler):
    def handle(self):
        return f"Return value at line : {self._instruction.line_number}. Offset : {self._instruction.offset}"
    


@register("COMPARE_OP")
class CompareOpHandler(BaseHandler):
    def handle(self):
        return f"Operation : {self._instruction.opname}. Comparing with : {self._instruction.argval}"