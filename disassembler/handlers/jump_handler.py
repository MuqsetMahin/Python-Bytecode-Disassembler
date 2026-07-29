from disassembler.handlers.base import BaseHandler
from disassembler.core.registry import register


class JumpHandler(BaseHandler):
    def handle(self):
        return f"{self.text()} Jump to offset : {self._instruction.argval}"
    
    def text(self):
        pass

@register("JUMP_FORWARD")
class JumpForwardHandler(JumpHandler):  
    def text(self):
        return "Unconditionally,"
    

@register("POP_JUMP_IF_FALSE")
class PopJumpIfFalseHandler(JumpHandler):
    def text(self):
        return "If false,"


