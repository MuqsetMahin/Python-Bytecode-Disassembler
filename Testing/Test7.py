from disassembler.core.disassembler import Disassembler
from disassembler.decorators.counter_decorator import count

import disassembler.handlers.misc_handler,disassembler.handlers.jump_handler,disassembler.handlers.load_handler


def sample(a, b):
    if a > b:
        return a
    else:
        return b
    
object=Disassembler(sample)

for i in object.opcode_filter("RETURN_VALUE"):
    pass