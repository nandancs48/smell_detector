# ML-Driven Code Smell Detection Compiler - Presentation

## Slide 1: Title
- **Project**: ML-Driven Code Smell Detection Compiler
- **Objective**: Automate the discovery of poor coding practices and security vulnerabilities directly within a compiler-like static analysis pipeline.

## Slide 2: Problem Statement
- Code smells (long functions, deep nesting, magic numbers, hardcoded credentials) compromise system maintainability and security.
- Manual reviews are slow and error-prone.
- Compilers inherently unroll code into ASTs (Abstract Syntax Trees), an ideal data structure for static logic analysis.

## Slide 3: Architecture & Approach
- **Frontend / Parser**: Uses Python's native `ast` module to read `.py` files and generate tree objects.
- **Feature Extractor**: Traverses the AST to log metrics like line length, nesting depth, and variable count.
- **Rule Engine**: Hardcoded heuristic thresholds (e.g., nesting > 3 is a smell).
- **ML Classifer**: A Random Forest model trained on historical code datasets to predict "smelliness" of functions based on their extracted numerical metrics.

## Slide 4: Rule-Based Engine Highlights
- Detects **Basic Smells**: Long Functions, Too Many Parameters.
- Detects **Extended Smells**: Global Variables misuse, Hardcoded Credentials, Empty Exception (`except: pass`) blocks.

## Slide 5: Machine Learning Integration
- **Model**: Scikit-Learn `RandomForestClassifier`
- **Features**: `[length, num_params, complexity, max_depth, num_vars]`
- **Why ML?**: Overcomes rigid heuristic rules by learning the complex combination of threshold limits. For example, a 15-line function might be fine, but a 15-line function with 5 parameters and heavy nesting is smelly.

## Slide 6: Results & Evaluation
- **Testing**: Fed heavily obfuscated and nested functions. Both rule-engine and ML accurately classified bad code structure.
- **Accuracy**: Random forest model achieves > 95% accuracy on synthetic training distributions distinguishing standard vs overly complex code.

## Slide 7: Future Work & Conclusion
- **Future Improvements**:
  - Support for more languages (Java, C++)
  - Deep Learning embeddings over raw code tokens (CodeBERT)
- **Conclusion**: Integrating static analysis and ML directly into the code iteration loop dramatically increases code safety and lifecycle longevity.
