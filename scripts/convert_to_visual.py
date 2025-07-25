from graphviz import Digraph
import ast

# Load source code
file_path = "/mnt/data/greet.py"
with open(file_path, "r") as f:
    source_code = f.read()

# Parse into AST
tree = ast.parse(source_code)

# Initialize a Graphviz Digraph
dot = Digraph(comment="AST for greet.py")
dot.attr("node", shape="box", fontname="Courier")

# Helper to generate unique IDs and walk tree
node_id = 0
def next_id():
    global node_id
    node_id += 1
    return f"n{node_id}"

def add_nodes(dot, node, parent_id=None):
    current_id = next_id()
    label = type(node).__name__
    if isinstance(node, ast.Constant):
        label += f"\nvalue={repr(node.value)}"
    elif isinstance(node, ast.Name):
        label += f"\nid={node.id}"
    elif isinstance(node, ast.arg):
        label += f"\narg={node.arg}"
    elif isinstance(node, ast.FunctionDef):
        label += f"\nname={node.name}"
    elif isinstance(node, ast.Attribute):
        label += f"\nattr={node.attr}"

    dot.node(current_id, label)

    if parent_id:
        dot.edge(parent_id, current_id)

    for field_name, value in ast.iter_fields(node):
        if isinstance(value, list):
            for item in value:
                if isinstance(item, ast.AST):
                    add_nodes(dot, item, current_id)
        elif isinstance(value, ast.AST):
            add_nodes(dot, value, current_id)

    return dot

# Build the graph
add_nodes(dot, tree)

# Export to file
output_path = "/mnt/data/greet_ast_tree"
dot.render(output_path, format="png", cleanup=False)

output_path + ".png"
