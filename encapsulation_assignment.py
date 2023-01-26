# PROTECTED VARIABLE
class Protected:
    def __init__(self):
        self._protectedVar = 0
        self.__privateVar = 23 

    # PRIVATE VARIABLE
    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self,private):
        self.__privateVar = private

obj = Protected()
obj.getPrivate() # retrieves value stored in privateVar
obj.setPrivate(47) # privateVar new value
obj.getPrivate() # retrieves new value stored in privateVar
