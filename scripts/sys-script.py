import sys

def trace_stack(label):
    frame = sys._getframe()
    print(f"\nTrace at: {label}")
    print("Function name:", frame.f_code.co_name)
    print("Line number:", frame.f_lineno)
    print("File:", frame.f_code.co_filename)
    print("Locals:", frame.f_locals)

    caller = frame.f_back
    if caller:
        print("Called by:", caller.f_code.co_name)
        print("Caller Locals:", caller.f_locals)
    else:
        print("CCalled by: <None> (global frame)")

def greet(name):
    trace_stack("inside greet")
    return ", ".join(["Hello", name])

trace_stack("top level before call")
print(greet("Eli"))
trace_stack("top level after call")
