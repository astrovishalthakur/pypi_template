echo [$(date)] "START"
echo [$(date)] "Creating conda environment with python 3.8"
conda create --prefix ./env python=3.8 -y
echo [$(date)] "Activating environment"
source activate ./env
echo [$(date)] "Installing dev requirements"
pip install -r requirements_dev.txt
echo [$(date)] "Environment setup complete"