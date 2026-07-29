import dis
from disassembler.core.registry import get_handler
from disassembler.core.instruction import Instruction
from disassembler.handlers.default import DefaultHandler


class Disassembler:
    def __init__(self,function):
        self.function=function

    def disassemble(self):
        for raw_data in dis.get_instructions(self.function.__code__):
            my_instr=Instruction.from_dis_instructions(raw_data)
            handler_cls=get_handler(my_instr.opname)
            if handler_cls:
                handler_obj=handler_cls(my_instr)
                yield handler_obj.run()
            else:
                handler_obj=DefaultHandler(my_instr)
                yield handler_obj.run()

    def opcode_filter(self,target_opname):
        for raw_data in dis.get_instructions(self.function.__code__):
            my_instr=Instruction.from_dis_instructions(raw_data)

            if my_instr.opname != target_opname:
                continue

            handler_cls=get_handler(my_instr.opname)

            if handler_cls:
                handler_obj=handler_cls(my_instr)
                yield handler_obj.run()
            else:
                handler_obj=DefaultHandler(my_instr)
                yield handler_obj.run()