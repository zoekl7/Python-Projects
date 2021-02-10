
#private/protected
class Protected:
    def __init__(self):
        #Private is indicated with the double underscore
        self.__privateVar = 17

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private

obj = Protected()
obj.getPrivate()
obj.setPrivate(35)
obj.getPrivate()

