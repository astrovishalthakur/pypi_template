echo [$(date)] "START"
echo [$(date)] "Creating environment"
conda create --prefix ./env python=3.8 -y
echo [$(date)] "Activating environment"
source activate ./env
echo [$(date)] "Installing dev requirements"
pip install -r requirements_dev.txt
echo [$(date)] "Environment setup complete"