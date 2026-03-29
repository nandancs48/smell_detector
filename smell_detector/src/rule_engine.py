import ast

class RuleEngine:
    """Evaluates features and AST to detect basic and extended code smells. (14 code smells)"""
    
    # Thresholds
    MAX_FUNCTION_LENGTH = 20
    MAX_PARAMS = 5
    MAX_NESTING_DEPTH = 3
    MAX_COMPLEXITY = 10
    MAX_RETURNS = 3
    
    @classmethod
    def analyze_function(cls, features, func_node):
        smells = []
        
        # 1. Long Function
        if features["length"] > cls.MAX_FUNCTION_LENGTH:
            smells.append(f"Long Function: {features['length']} lines (Max: {cls.MAX_FUNCTION_LENGTH})")
            
        # 2. Too Many Parameters
        if features["num_params"] > cls.MAX_PARAMS:
            smells.append(f"Too Many Parameters: {features['num_params']} params (Max: {cls.MAX_PARAMS})")
            
        # 3. Deep Nesting
        if features["max_depth"] > cls.MAX_NESTING_DEPTH:
            smells.append(f"Deep Nesting: depth {features['max_depth']} (Max: {cls.MAX_NESTING_DEPTH})")
            
        # 4. High Complexity
        if features["complexity"] > cls.MAX_COMPLEXITY:
            smells.append(f"High Complexity: cyclomatic complexity {features['complexity']} (Max: {cls.MAX_COMPLEXITY})")
            
        # 5. Too Many Return Statements
        if features.get("returns", 0) > cls.MAX_RETURNS:
            smells.append(f"Too Many Returns: {features['returns']} returns (Max: {cls.MAX_RETURNS})")
            
        # 6. Unused Variables
        assigned_vars = set()
        used_vars = set()
        for node in ast.walk(func_node):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        assigned_vars.add(target.id)
            elif isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
                used_vars.add(node.id)
        for arg in func_node.args.args:
            assigned_vars.add(arg.arg)
        unused = assigned_vars - used_vars
        unused = {var for var in unused if len(var) > 1 and var != 'self'}
        if unused:
            smells.append(f"Unused Variables: {', '.join(unused)}")

        # 7. Magic Numbers
        magic_numbers = set()
        for node in ast.walk(func_node):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
                if node.value not in [0, 1, -1, 2, 100]: 
                    magic_numbers.add(node.value)
        if magic_numbers:
            smells.append(f"Magic Numbers used: {magic_numbers}")
            
        # 8. Empty Exception Block & 9. Catch-All Exception
        empty_excepts = 0
        catch_all = 0
        for node in ast.walk(func_node):
            if isinstance(node, ast.ExceptHandler):
                if len(node.body) == 1 and isinstance(node.body[0], ast.Pass):
                    empty_excepts += 1
                if node.type is None or (isinstance(node.type, ast.Name) and node.type.id == 'Exception'):
                    catch_all += 1
        if empty_excepts > 0:
            smells.append(f"Empty Exception Block: Found {empty_excepts} instances")
        if catch_all > 0:
            smells.append(f"Catch-All Exception: Found {catch_all} 'except Exception:' instances")
            
        # 10. Hardcoded Credentials
        credential_keywords = ['password', 'secret', 'token', 'api_key', 'pwd']
        hardcoded_creds = False
        for node in ast.walk(func_node):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        if any(kw in target.id.lower() for kw in credential_keywords):
                            if isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
                                if len(node.value.value) > 2: 
                                    hardcoded_creds = True
        if hardcoded_creds:
            smells.append("Hardcoded Credentials detected in variable assignment")

        # 11. Overuse of Print Statements
        print_count = sum(1 for node in ast.walk(func_node) if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'print')
        if print_count > 2:
            smells.append(f"Overuse of Print Statements: {print_count} prints")
            
        # 12. Single Letter Variables
        bad_names = [v for v in assigned_vars if len(v) == 1 and v not in ('i', 'j', 'k', '_', 'x', 'y')]
        if bad_names:
            smells.append(f"Un-descriptive variables: {', '.join(bad_names)}")

        return smells

    @classmethod
    def analyze_file(cls, tree):
        smells = []
        # 13. Global Variable Misuse
        global_uses = 0
        for node in ast.walk(tree):
            if isinstance(node, ast.Global):
                global_uses += len(node.names)
        
        if global_uses > 0:
            smells.append(f"Global Variables Misuse: Detected {global_uses} 'global' keyword uses.")
            
        # 14. Large Class
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                methods = [m for m in node.body if isinstance(m, ast.FunctionDef)]
                if len(methods) > 5:
                    smells.append(f"Large Class: Class '{node.name}' has {len(methods)} methods (Max: 5)")
            
        return smells
