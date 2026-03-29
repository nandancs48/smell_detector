import pandas as pd
import random
import os

def generate_dataset(output_path="data/features.csv", num_samples=1000):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    data = []
    
    for _ in range(num_samples):
        # Good code metrics
        if random.random() > 0.5:
            length = random.randint(1, 15)
            num_params = random.randint(0, 3)
            complexity = random.randint(1, 5)
            max_depth = random.randint(0, 2)
            num_vars = random.randint(0, 5)
            has_smell = 0
            
            # small chance to be slightly long but still fine
            if random.random() > 0.9:
                length = random.randint(16, 25)
        else:
            # Bad code metrics (smelly)
            length = random.randint(20, 100)
            num_params = random.randint(4, 10)
            complexity = random.randint(8, 25)
            max_depth = random.randint(3, 7)
            num_vars = random.randint(5, 20)
            has_smell = 1
            
            # could just have one bad attribute
            if random.random() > 0.5:
                # e.g. just too many params
                length = random.randint(1, 15)
                complexity = random.randint(1, 5)
                max_depth = random.randint(0, 2)
                num_vars = random.randint(0, 5)
                num_params = random.randint(6, 12)
                
        data.append([length, num_params, complexity, max_depth, num_vars, has_smell])
        
    df = pd.DataFrame(data, columns=["length", "num_params", "complexity", "max_depth", "num_vars", "has_smell"])
    df.to_csv(output_path, index=False)
    print(f"Generated synthetic dataset with {num_samples} samples at {output_path}")

if __name__ == "__main__":
    generate_dataset()
