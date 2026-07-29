from abc import ABC,abstractmethod
from disassembler.decorators.logging_decorator import log_call
from disassembler.decorators.counter_decorator import count_total_call

class BaseHandler(ABC):
    def __init__(self,instruction):
        self._instruction=instruction

    @count_total_call
    @log_call
    def run(self):
        return self.handle()
    
    @abstractmethod
    def handle(self):
        pass
        