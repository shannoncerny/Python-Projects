# PROTECTED VARIABLE
class Protected:
    def __init__(self):
        self._protectedVar = 0
    obj = Protected()
    obj._protectedVar = 11
    # output will be 11
    print(obj._protectedVar)

# PRIVATE VARIABLE
class Private:
    def __init__(self):
        self.__privateVar = 23

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private

obj = Protected()
obj.getPrivate()
obj.setPrivate(47) # give privateVar a new value
obj.getPrivate() # retrieves new value stored in privateVar
