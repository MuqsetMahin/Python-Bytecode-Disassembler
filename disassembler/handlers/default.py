from disassembler.handlers.base import BaseHandler


class DefaultHandler(BaseHandler):
    def handle(self):
        return f"{self._instruction.opname} - A default handler. Arguments: {self._instruction.argval}"
