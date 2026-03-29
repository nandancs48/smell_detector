# Execution Script for ML-Driven Code Smell Pipeline

$uv_path = "C:\Users\USER\.local\bin\uv.exe"

Write-Host "Checking for UV Package Manager..."
if (Test-Path $uv_path) {
    Write-Host "UV found at $uv_path! Using it to run the pipeline automatically..."
    
    Write-Host "--- 1. Training ML Model ---"
    & $uv_path run --with pandas --with scikit-learn src/ml_model.py
    
    Write-Host "`n--- 2. Executing Static Analysis on Sample Code ---"
    & $uv_path run --with pandas --with scikit-learn src/main.py samples/sample_input.py
}
else {
    Write-Host "UV not found. Attempting native Python..."
    
    Write-Host "--- 1. Training ML Model ---"
    python src/ml_model.py
    
    Write-Host "`n--- 2. Executing Static Analysis on Sample Code ---"
    python src/main.py samples/sample_input.py
}

Write-Host "`nPipeline Execution Complete!"
