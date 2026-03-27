class A:
    label = "base class"
class B(A):
    label = "Masala Blend"
class C(A):
    label = "Herbal Blend"
class D(B, C):
    pass
cup = D()
print(cup.label)#output: Masala Blend
#kyoki D class me B class pehle aata hai isliye B class ka label print hota hai. Agar C class pehle aata to C class ka label print hota.    
print(D.__mro__)