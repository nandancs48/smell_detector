# ML-Driven Code Smell Detection Compiler

This project is an automated code analysis pipeline that blends traditional static metric extraction with a Machine Learning model (Random Forest Classifier) to identify problematic or "smelly" Python functions.

The pipeline processes Python source code, extracts deterministic metrics (like length, cyclomatic complexity, parameter count, nesting depth), evaluates them against rule-based thresholds, and feeds them into a trained ML model for a final assessment of code quality.

## Project Structure

*   **`src/parser.py`**: Parses external target `.py` files into an Abstract Syntax Tree (AST).
*   **`src/feature_extractor.py`**: Extracts critical metrics from the AST (function lengths, number of variables, parameters, maximum nesting depth, etc.).
*   **`src/rule_engine.py`**: Contains deterministic rules to identify specific code violations (e.g., hardcoded credentials, too many parameters, catch-all exceptions, magic numbers).
*   **`src/dataset_generator.py`**: Generates a synthetic dataset of clean vs. smelly function metrics to bootstrap the ML model.
*   **`src/ml_model.py`**: Contains the Machine Learning component. It trains a RandomForest classifier on the generated data.
*   **`src/main.py`**: The main entry point. It coordinates the parser, rule engine, and ML model to provide a full analysis report on a target file.
*   **`run_pipeline.ps1`**: A PowerShell script that automates model training and code analysis.

## Prerequisites

The project requires Python and the following packages:
*   `pandas`
*   `scikit-learn`

The `run_pipeline.ps1` script will seamlessly utilize the `uv` package manager if it's installed on your system to run the model without requiring global dependency installation.

## How to Run

To train the machine learning model and run a test analysis on the sample file, open a terminal in the project directory and run the execution script:

```powershell
.\run_pipeline.ps1
```

If you encounter an execution policy error on Windows, use this command to temporarily bypass restrictions and run the pipeline:

```powershell
powershell -ExecutionPolicy Bypass -File .\run_pipeline.ps1
```

### Manual Execution

1.  **Generate Dataset (Optional but recommended):**
    ```bash
    python src/dataset_generator.py
    ```
2.  **Train the Machine Learning Model:**
    ```bash
    python src/ml_model.py
    ```
3.  **Run the Analyzer on a specific file:**
    ```bash
    python src/main.py samples/sample_input.py
    ```

## Extending the Project

*   **Custom Rules:** You can modify `src/rule_engine.py` to add custom threshold detections for specific code bases.
*   **Advanced Features:** Modify `src/feature_extractor.py` to count specific AST nodes if you want deeper intelligence to reach the ML Model.

