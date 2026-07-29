from dataclasses import dataclass
from typing import Optional,Any

@dataclass
class Instruction:
    opname:     str
    arg:        Optional[int]
    argval:     Optional[Any]
    argrepr:    str
    offset:     int
    starts_line:bool
    line_number:int

    @classmethod
    def from_dis_instructions(cls,raw_data):
        return cls(
            opname=raw_data.opname,
            arg=raw_data.arg,
            argval=raw_data.argval,
            argrepr=raw_data.argrepr,
            offset=raw_data.offset,
            starts_line=raw_data.starts_line,
            line_number=raw_data.line_number
        )
