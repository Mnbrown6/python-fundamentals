""" All about numbers"""

""" Task 1"""

aa: float = 34_038

bb: float = 45_838.8734

cc: float = -3_695_365

d = 0b_0110_0010_1011

e = 0x_174_C0


print(aa)
print(bb)
print(cc)
print(d)
print(e)


"""Task 2 """

def numeric_types(value1: int):
    print(hex(value1))
    print(bin(value1))
    print(oct(value1))
    print(value1)


numeric_types(29)

