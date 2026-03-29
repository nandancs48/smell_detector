import argparse
import sys
import os

from parser import CodeParser
from feature_extractor import FeatureExtractor
from rule_engine import RuleEngine
from ml_model import predict

def main():
    parser = argparse.ArgumentParser(description="ML-Driven Code Smell Detection Compiler")
    parser.add_argument("file", help="Python source file to analyze")
    args = parser.parse_args()
    
    target_file = args.file
    if not os.path.exists(target_file):
        print(f"Error: File {target_file} does not exist.")
        sys.exit(1)
        
    print(f"--- Analyzing {target_file} ---")
    
    try:
        app_parser = CodeParser(target_file)
    except Exception as e:
        print(f"Failed to parse {target_file}: {e}")
        sys.exit(1)
        
    tree = app_parser.get_tree()
    functions = app_parser.get_functions()
    
    # 1. File level metrics
    file_features = FeatureExtractor.extract_file_features(tree)
    file_smells = RuleEngine.analyze_file(tree)
    
    if file_smells:
        print("\n[File-Level Smells Detected]:")
        for smell in file_smells:
            print(f"  - {smell}")
            
    print(f"\nFound {len(functions)} functions.")
    
    # 2. Function level metrics
    for func in functions:
        features = FeatureExtractor.extract_function_features(func)
        rule_based_smells = RuleEngine.analyze_function(features, func)
        
        # 3. ML Prediction
        ml_is_smelly = False
        try:
             ml_is_smelly = predict(features)
        except Exception:
             ml_is_smelly = None # Model not trained or Error
             
        # Report
        print(f"\nFunction: {features['name']}() at line {features['lineno']}")
        print(f"  Metrics: Length={features['length']}, Params={features['num_params']}, "
              f"Complexity={features['complexity']}, MaxDepth={features['max_depth']}, Vars={features['num_vars']}")
              
        if rule_based_smells:
            print("  [Rule Engine Alerts]:")
            for smell in rule_based_smells:
                print(f"    - {smell}")
        else:
            print("  [Rule Engine Alerts]: None")
            
        if ml_is_smelly is not None:
             print(f"  [ML Model Prediction]: {'SMELLY' if ml_is_smelly else 'CLEAN'}")
        else:
             print("  [ML Model Prediction]: Model not found or error loading model. Run 'python src/ml_model.py' first.")

if __name__ == "__main__":
    main()
