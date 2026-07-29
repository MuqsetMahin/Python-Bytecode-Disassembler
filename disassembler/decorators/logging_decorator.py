def log_call(func):
    def wrapper(self):
        print("Processing :",self._instruction.opname)
        result=func(self)
        print(result)
        print("End of processing :",self._instruction.opname)
        return result
    return wrapper