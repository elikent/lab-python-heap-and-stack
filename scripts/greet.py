import dis

def greet(name):
    return ", ".join(["Hello", name])

print(greet("Eli"))

print(dis.Bytecode(greet).info())