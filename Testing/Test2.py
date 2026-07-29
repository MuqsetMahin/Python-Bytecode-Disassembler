from disassembler.core.instruction import Instruction
import dis


def sample(a, b):
    if a > b:
        return a
    else:
        return b
    

for raw_data in dis.get_instructions(sample):
    my_instr=Instruction.from_dis_instructions(raw_data)
    print(my_instr)