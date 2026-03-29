# 13. Global misuse
my_global_config = True

# 14. Large Class
class ExcessivelyLargeClassThatDoesTooMuch:
    def method_one(self): pass
    def method_two(self): pass
    def method_three(self): pass
    def method_four(self): pass
    def method_five(self): pass
    def method_six_too_many(self): pass

def completely_clean_function(a, b):
    return a + b
    
# 1. Long function, 2. Too many params
def completely_unmaintainable_and_smelly_function(a, b, c, d, e, f, g):
    # 10. Hardcoded credentials
    password = "super_secret_password_123!"
    
    # 7. Magic numbers
    magic = 88
    
    # 6. Unused vars
    unused_var = "I am never used"
    
    # 12. Un-descriptive variable names
    q = 100
    z = 200
    
    # 11. Overuse of prints
    print("Starting process")
    print("Doing work")
    print("Ending work")
    
    # 3. Deep nesting & 4. High complexity
    try:
        if a > b:
            for i in range(10):
                if i % 2 == 0:
                    if c == d:
                        print("Deeply nested!")
                        if e == f:
                            pass # Too deep
    # 9. Catch-all Exception
    except Exception as ex:
        # 8. Empty exception handler
        pass
        
    global my_global_config
    if my_global_config:
        # 5. Too many returns
        return magic
    if q > z:
        return 1
    if z > q:
        return -1
    return 0
