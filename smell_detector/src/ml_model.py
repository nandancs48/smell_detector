import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pickle
import os

def train_model(data_path="data/features.csv", model_path="models/model.pkl"):
    if not os.path.exists(data_path):
        print(f"Dataset not found at {data_path}. Please run dataset_generator.py first.")
        return
        
    df = pd.read_csv(data_path)
    
    X = df[["length", "num_params", "complexity", "max_depth", "num_vars"]]
    y = df["has_smell"]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    
    print(f"Model Accuracy: {acc * 100:.2f}%")
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    with open(model_path, "wb") as f:
        pickle.dump(model, f)
        
    print(f"Model saved to {model_path}")

def predict(features_dict, model_path="models/model.pkl"):
    if not os.path.exists(model_path):
        return None  # Model not trained
        
    with open(model_path, "rb") as f:
        model = pickle.load(f)
        
    # Order must match dataset
    X = pd.DataFrame({
        "length": [features_dict.get("length", 0)],
        "num_params": [features_dict.get("num_params", 0)],
        "complexity": [features_dict.get("complexity", 0)],
        "max_depth": [features_dict.get("max_depth", 0)],
        "num_vars": [features_dict.get("num_vars", 0)]
    })
    
    prediction = model.predict(X)[0]
    return bool(prediction)

if __name__ == "__main__":
    train_model()
