class A:

    def class_a_method(self):
        return 'I am just a class A method'

    def hello(self):
        return 'hello melissa'


class B:

    def class_b_method(self):
        return 'I am just a class B method'

    def hello(self):
        return 'hello ange'


class C(A,B):
    pass  



instanceA=A()
instanceB=B()
instanceC=C()

print(instanceA.class_a_method())
print(instanceA.hello())
print(instanceC.class_a_method())
help(instanceC)
print(C.mro())