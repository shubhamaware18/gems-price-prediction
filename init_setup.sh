# Print a message indicating the start of the script along with the current date and time.
echo [$(date)]: "START"

echo [$(date)]: "creating env with python 3.8 version" 

# Create a Conda environment named 'env' with Python version 3.8 in the current directory.
conda create --prefix ./env python=3.8 -y

# Print a message indicating the activation of the created Conda environment.
echo [$(date)]: "Activating the Environment"

# Activate the Conda environment named 'env'.
source activate ./env

# Print a message indicating the installation of development requirements.
echo [$(date)]: "Installing the Development requirements"

# Install Python packages listed in the 'requirements_dev.txt' file using pip.
pip install -r requirements_dev.txt

# Print a message indicating the end of the script along with the current date and time.
echo [$(date)]: "END"
