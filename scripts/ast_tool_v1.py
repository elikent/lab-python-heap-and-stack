import ast
import astpretty
from pathlib import Path

FILE_NAME = "greet.py"

# Define path to script you want analyzed
script_to_analyze = Path(__file__).parent / FILE_NAME

# Convert script into string
with open(script_to_analyze, "r") as f:
    code = f.read()

tree = ast.parse(code)
print(f"--- AST for {FILE_NAME} ---\n")
print(astpretty.pprint(tree))
