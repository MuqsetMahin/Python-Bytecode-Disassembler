call_count=0

def count_total_call(func):
    def wrapper(self):
        global call_count
        call_count+=1
        return func(self)
    return wrapper



def count():
    return call_count