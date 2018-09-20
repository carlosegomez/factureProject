class MyMetaClass(type):
    def __new__(cls, clsname, superclasses, attributedict):
        print(cls)
        print(clsname)
        print(superclasses)
        print(attributedict)
        return super().__new__(cls, clsname, superclasses, attributedict)


class MyClass(metaclass=MyMetaClass):
    pass

