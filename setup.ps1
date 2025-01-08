# setup.ps1

# Check if Python is installed
$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
    Write-Host "Python is not installed. Please install Python 3.9 or later."
    exit
}

# Upgrade pip
python -m pip install --upgrade pip

# Install dependencies
pip install -r requirement.txt

Write-Host "Setup is complete. You can now run your tests using the workflow."
