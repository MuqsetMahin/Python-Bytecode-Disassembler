from disassembler.handlers.base import BaseHandler


try:
    obj=BaseHandler("ABCDF")
except TypeError as e:
    print("Error :" ,e)



class Check(BaseHandler):
    def handle(self):
        print("All Ok.")

Check("JKHJ").handle()