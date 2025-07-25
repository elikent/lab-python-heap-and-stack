import ast
import astpretty
import argparse
from pathlib import Path

# Parses a Python file and pretty-prints its AST
def analyze_file(file_path: Path):
    # returns easily-readable error if file_path is not a file
    if not file_path.is_file():
        print(f"Error: File not found at {file_path}")
        return
    print(f"--- AST for {file_path.name} ---\n")
    
    try:
        # read script into string
        with open(file_path, "r", encoding='utf-8') as f:
            code = f.read()
        
        # create tree object from string and print
        tree = ast.parse(code, filename=file_path.name)
        print(astpretty.pprint(tree))
    except Exception as e:
        print(f"An error occurred while processing the file: {e}")

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
    analyze_file(file_to_analyze)

if __name__ == "__main__":
    main()