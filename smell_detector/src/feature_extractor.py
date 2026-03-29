import ast

class FeatureExtractor:
    @staticmethod
    def extract_function_features(func_node):
        """Extracts numerical features from a single function AST node."""
        
        # 1. Function Length (LOC)
        if hasattr(func_node, 'end_lineno') and hasattr(func_node, 'lineno'):
            length = func_node.end_lineno - func_node.lineno + 1
        else:
            length = len(func_node.body) # fallback approximation
            
        # 2. Number of Parameters
        num_params = len(func_node.args.args)
        
        # 3. Cyclomatic Complexity approximation
        complexity = 1
        for node in ast.walk(func_node):
            if isinstance(node, (ast.If, ast.While, ast.For, ast.ExceptHandler, ast.With, ast.comprehension)):
                complexity += 1
            elif isinstance(node, ast.BoolOp):
                complexity += len(node.values) - 1
                
        # 4. Maximum Nesting Depth
        def get_max_depth(node, current_depth):
            max_d = current_depth
            for child in ast.iter_child_nodes(node):
                child_depth = current_depth
                if isinstance(node, (ast.If, ast.For, ast.While, ast.Try, ast.With)):
                    child_depth += 1
                max_d = max(max_d, get_max_depth(child, child_depth))
            return max_d
            
        max_depth = get_max_depth(func_node, 0)
        
        # 5. Variable Count
        variables = set()
        for node in ast.walk(func_node):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        variables.add(target.id)
        num_vars = len(variables)

        # 6. Return statement count
        num_returns = sum(1 for node in ast.walk(func_node) if isinstance(node, ast.Return))

        return {
            "name": func_node.name,
            "lineno": getattr(func_node, 'lineno', 0),
            "length": length,
            "num_params": num_params,
            "complexity": complexity,
            "max_depth": max_depth,
            "num_vars": num_vars,
            "returns": num_returns
        }

    @staticmethod
    def extract_file_features(tree):
        """Extract global/file-level features."""
        global_vars = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Global):
                global_vars.extend(node.names)
        
        return {
            "num_globals": len(set(global_vars))
        }
