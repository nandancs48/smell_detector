# Final Project Report: ML-Driven Code Smell Detection Compiler

## 1. Executive Summary
This report summarizes the completion of the 14-week project aimed at building a hybrid Code Smell Detection Compiler pipeline. The system was designed from the ground up to parse Python code into an Abstract Syntax Tree (AST), extract quantitative metrics, use a deterministic Rule-Engine for immediate flagging, and finally process an overarching Machine Learning classifier to output a comprehensive code quality report.

## 2. Implementation Journey
- **Weeks 1-3:** Explored compiler static analysis and constructed the Software Requirements Specification (SRS) along with a threat matrix mapping code smells to tangible security risks (e.g., hardcoded credentials).
- **Weeks 4-5:** Detailed System Architecture. Determined that the `ast` module provided the most robust baseline. Outlined the metrics required (Cyclomatic complexity, Line length, Variables count, Nesting depth).
- **Weeks 6-8:** Built `parser.py`, `feature_extractor.py`, and `rule_engine.py`. Implemented rigorous basic smells (Long function, magic numbers) and advanced smells (Global misuses, Empty overrides).
- **Weeks 9-10:** Integrated Pandas and Scikit-Learn. Built `dataset_generator.py` to synthetically model healthy vs smelly code. Trained a Random Forest model in `ml_model.py` that serializes to `models/model.pkl`.
- **Weeks 11-12:** Unified all modules under the `main.py` CLI pipeline wrapper. Benchmarked system using `samples/sample_input.py` which contains multiple syntactically valid but fundamentally flawed code blocks. All components performed rapidly and with high precision.

## 3. Results & Evaluation 
Running `python src/main.py samples/sample_input.py` correctly triggers:
1. **Rule Engine Alerts**: Depth violations, variable count warnings, detection of hardcoded dummy passwords.
2. **ML Alert**: The RandomForest model flags the functions as "SMELLY" given their inflated parameter counts and severe nesting depth.

The ML architecture validates that rigid thresholds ("function > 20 lines is bad") can be replaced or augmented by a classifier that holistically views metrics. 

## 4. Conclusion
The resulting system matches the complete specifications of the initial 14-week plan, delivering a modern AI-augmented static code analyzer capable of preventing technical debt organically.
