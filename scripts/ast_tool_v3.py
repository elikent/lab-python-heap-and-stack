# This version implements proper exit codes

import ast
import astpretty
import argparse
from pathlib import Path
import sys

# Parses a Python file and pretty-prints its AST
def analyze_file(file_path: Path) -> bool:
    """Parses a Python file and pretty-prints its AST. Returns True on success, False on failure."""
    if not file_path.is_file():
        print(f"Error: File not found at {file_path}", file=sys.stderr)
        return False
    print(f"--- AST for {file_path.name} ---\n")
    
    try:
        # read script into string
        with open(file_path, "r", encoding='utf-8') as f:
            code = f.read()
        
        # create tree object from string and print
        tree = ast.parse(code, filename=file_path.name)
        print(astpretty.pprint(tree))
    except SyntaxError as e:
        print(f"An error occurred while parsing the file: {e}", file=sys.stderr)
        return False
    return True

# Main function to parse command-line arguments and run the analysis.
def main():
    parser = argparse.ArgumentParser(
        description="A script to parse a Python file and display its Abstract Syntax Tree (AST)."
    )
    parser.add_argument(
        "filename",
        type=str,
        help="The Python file to analyze."    
    )
    args = parser.parse_args()

    # Construct the full path relative to this script's location
    script_dir = Path(__file__).parent
    file_to_analyze = script_dir / args.filename

    if not analyze_file(file_to_analyze):
        sys.exit(1)

if __name__ == "__main__":
    main()