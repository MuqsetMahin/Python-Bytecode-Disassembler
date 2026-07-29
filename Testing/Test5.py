import dis
from disassembler.core.registry import get_handler
from disassembler.core.instruction import Instruction
import disassembler.handlers.load_handler
from disassembler.handlers.default import DefaultHandler
import disassembler.handlers.misc_handler,disassembler.handlers.jump_handler


def sample(a, b):
    if a==0:
        c=1
    else:
        c=2
        
    if a > b:
        return a
    else:
        return b
    
for raw_data in dis.get_instructions(sample.__code__):
    my_instr=Instruction.from_dis_instructions(raw_data)
    handler_cls=get_handler(my_instr.opname)
    if handler_cls:
        handler_obj=handler_cls(my_instr)
        print(handler_obj.handle())
    else:
        handler_obj=DefaultHandler(my_instr)
        print(handler_obj.handle())
