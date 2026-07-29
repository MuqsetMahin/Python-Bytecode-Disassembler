from disassembler.core.instruction import Instruction


instr=Instruction(
    opname="Load",
    arg=0,
    argval=3,
    argrepr='3',
    offset=0,
    starts_line=True,
    line_number=4
)

print(instr)