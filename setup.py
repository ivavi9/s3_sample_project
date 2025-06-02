# setup_project.py
# This script sets up a PySpark + Kafka environment using stable versions compatible with Spark 4.x.

import os
import sys
import subprocess

# 1. Set up environment variables
os.environ["JAVA_HOME"] = "/opt/homebrew/opt/openjdk@17/libexec/openjdk.jdk/Contents/Home"
os.environ["PATH"] = os.environ["JAVA_HOME"] + "/bin:" + os.environ.get("PATH", "")

# 2. Create virtual environment (if not already present)
venv_path = "env"
if not os.path.exists(venv_path):
    subprocess.run([sys.executable, "-m", "venv", venv_path])
    print("Virtual environment created.")
else:
    print("Virtual environment already exists.")

# 3. Activate virtual environment and install dependencies
pip_path = os.path.join(venv_path, "bin", "pip")
subprocess.run([pip_path, "install", "--upgrade", "pip"])
subprocess.run([pip_path, "install", "pyspark", "kafka-python", "jupyter", "ipykernel"])

# 4. Register the virtualenv with Jupyter kernel
i_python_path = os.path.join(venv_path, "bin", "python")
subprocess.run([i_python_path, "-m", "ipykernel", "install", "--user", "--name", "env", "--display-name", "Python (env)"])

print("Setup complete. Launch Jupyter using the 'env' kernel.")
