import dis
code = '''
a = 1
b = 2
print(a+b)
'''

for i in dis.get_instructions(code):
    print(i)
    break
    print(i.positions.lineno,i.opname,i.arg)
# dis.disassemble(code)
# print(type(dis.dis(code)))
bytecode = dis.dis(code)
# with open('ByteCode_Representation.txt','w') as file:
#     file.write(dis.dis(code))
# print(bytecode)


# compiled = compile(code,'', 'exec')
# # print(type(compiled)) # <class 'code'>
# print('Compiled : \n',compiled.co_code)

# exec(compiled)

#  --------------------------------------------------------------

#  Alter Code
# code = '''
# num1 = 10
# num2 = 10

# def sum_of_two(n1,n2):
#     return n1 + n2


# print(sum_of_two(num1,num2))
# '''