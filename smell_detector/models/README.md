# Machine Learning Models Directory

This folder is intended to store the trained Machine Learning classifiers for code smell detection.

**Why is this folder (mostly) empty?**
Because Machine Learning models are generated dynamically based on the training data! A `.pkl` file containing the weights of the Random Forest algorithm is highly specific to your environment and Python version.

**How to generate the model file:**
Open your terminal in the root `smell_detector` directory and run:

```bash
python src/ml_model.py
```

Once that script finishes successfully, a new file named `model.pkl` will appear right here in this folder!
