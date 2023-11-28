class Prototype:
    def clone(self):
        pass
class ConcretePrototype(Prototype):

    def __init__(self, prototype):
        self.field1 = prototype.field1

    def clone(self):
        return Prototype(self)

class SubclassPrototype(Prototype):

    def __init__(self, prototype):
        super().__init__(prototype)
        self.field2 = prototype.field2

    def clone(self):

        return Prototype(self)