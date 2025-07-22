# script to output disassembly
'''import dis

with open("i:\\My Drive\\it-learning\\my-projects\\lab-python-heap-and-stack\\scripts\\greet.py") as f:
    code = compile(f.read(), "test1.py", "exec")
    dis.dis(code)'''

import dis
import io
import sys

# Step 1: Read the code from test1.py
with open("i:\\My Drive\\it-learning\\my-projects\\lab-python-heap-and-stack\\scripts\\greet.py") as f:
    code = compile(f.read(), "test1.py", "exec")

# Step 2: Create a text buffer
buffer = io.StringIO()

# Step 3: Redirect stdout to the buffer
original_stdout = sys.stdout
sys.stdout = buffer

# Step 4: Run dis.dis() while stdout is redirected
dis.dis(code)

# Step 5: Restore stdout
sys.stdout = original_stdout

# Step 6: Write buffer content to file
with open("i:\\My Drive\\it-learning\\my-projects\\lab-python-heap-and-stack\\output\\disassembly_output.txt", "w") as f:
    f.write(buffer.getvalue())

# Optional: Print confirmation
print("Bytecode disassembly written to disassembly_output.txt")