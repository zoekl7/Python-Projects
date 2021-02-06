
#private
class Private:
    def __init__(self):
        #Private is indicated with the double underscore
        self.__privateVar = 17

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private

obj = Private()
obj.getPrivate()
obj.setPrivate(35)
obj.getPrivate()

#protected
class Protected:
    def __init__(self):
        self._protectedVar = 5

obj = Protected()
obj._protectedVar = 15
print(obj._protectedVar)
