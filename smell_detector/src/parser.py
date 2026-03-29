import ast

class CodeParser:
    def __init__(self, file_path):
        self.file_path = file_path
        with open(file_path, "r", encoding="utf-8") as file:
            self.source_code = file.read()
        self.tree = ast.parse(self.source_code, filename=file_path)

    def get_functions(self):
        """Return all function definitions in the AST."""
        return [node for node in ast.walk(self.tree) if isinstance(node, ast.FunctionDef) or isinstance(node, ast.AsyncFunctionDef)]

    def get_classes(self):
        """Return all class definitions in the AST."""
        return [node for node in ast.walk(self.tree) if isinstance(node, ast.ClassDef)]

    def get_all_nodes(self):
        """Return all nodes in the AST."""
        return list(ast.walk(self.tree))
    
    def get_tree(self):
        return self.tree
