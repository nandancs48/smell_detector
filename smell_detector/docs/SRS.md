# Software Requirements Specification (SRS) - ML-Driven Code Smell Detection Compiler

## 1. Introduction
This project builds a static analysis compiler pipeline that employs both rule-based and machine-learning-driven approaches to detect code smells and poor coding practices that could lead to maintainability issues or security vulnerabilities.

## 2. Problem Definition
Code smells are indicators of deeper problems in software architecture and implementation, leading to technical debt. Our compiler targets the Python language, utilizing its inherent `ast` capabilities to extract abstract structures (e.g., function length, cyclomatic complexity) to mathematically and heuristically determine the presence of smells. 

## 3. Project Objectives and Scope
1. Implement a static python analyzer using `ast`.
2. Extract functional and structural metrics from code.
3. Detect basic rules (Long Function, Deep Nesting, Unused Variables, Magic Numbers, Too Many Params).
4. Detect extended rules (Global misuses, Empty Exceptions, Hardcoded Credentials, High Complexity).
5. Leverage a Machine Learning classifier trained on code metrics to predict "smelly" code segments automatically.

## 4. Functional Requirements
- **AST Parsing**: The system shall process valid Python source files to generate an Abstract Syntax Tree.
- **Feature Extraction**: The system shall calculate metrics per function and class.
- **Reporting**: The system shall generate a detailed textual report identifying the line numbers and logic issues (smells) detected.
- **Rule Engine**: The system shall use hardcoded thresholds for immediate flag classification.
- **ML Integration**: The system shall pass extracted metrics to a pre-trained ML model for secondary classification.

## 5. Non-Functional Requirements
- **Performance**: The parsing and rule evaluation should take less than 1 second per 1000 lines of code.
- **Scalability**: The system should be able to scan an entire directory structure iteratively.
- **Extensibility**: Adding new rule-based logic or retraining the ML model should be seamless.

## 6. Threat & Security Analysis
Insecure coding practices often map directly to code smells:
- **Hardcoded Credentials**: Directly leads to broken authentication if committed to source control.
- **Empty Exception Handling**: Masking exceptions (`except: pass`) hides system failures and potential attacks from operators.
- **Global Variables Misuse**: Can lead to unpredictable state and race conditions in concurrent data modification.
- **Magic Numbers**: Represents undocumented, potentially unsafe constraints that hinder auditing and updating core parameters securely.
