# PySpark Streaming to Kafka Example

This project demonstrates how to use PySpark Structured Streaming to read JSON files from a local directory, transform the data, and publish the results to a Kafka topic. The setup is automated using `setup.py` for convenience.

## Project Structure

- `jup_test.ipynb`: Jupyter notebook containing the main PySpark streaming pipeline code.
- `setup.py`: Script to set up the Python virtual environment and install all dependencies.
- `data/`: Directory where you place JSON files to simulate streaming input.
- `artifacts/`: Spark artifacts and checkpoints.
- `env/`, `pyspark-env/`: Python virtual environments (if used).

## Prerequisites

- **macOS** (commands are for zsh shell)
- **Homebrew** (for installing Java, Spark, Kafka, ZooKeeper)
- **Python 3.8+**
- **Java 17** (OpenJDK recommended)
- **Apache Spark 3.4.x** (or 3.3.x; avoid Spark 4.0.0 for Kafka integration)
- **Kafka and ZooKeeper**

## Setup Instructions

### 1. Install System Dependencies

Install Java, Spark, Kafka, and ZooKeeper using Homebrew:
```zsh
brew install openjdk@17 apache-spark zookeeper kafka
```

### 2. Start ZooKeeper and Kafka
```zsh
zookeeper-server-start /opt/homebrew/etc/zookeeper/zoo.cfg &
brew services start kafka
```

### 3. Set JAVA_HOME
Add to your shell profile (e.g., `~/.zshrc`):
```zsh
export JAVA_HOME="/opt/homebrew/opt/openjdk@17/libexec/openjdk.jdk/Contents/Home"
export PATH="$JAVA_HOME/bin:$PATH"
```
Restart your terminal or run the above lines directly.

### 4. Run the Project Setup Script
This will create a Python virtual environment, install all Python dependencies, and register the Jupyter kernel.
```zsh
python setup.py
```

### 5. Create the Data Directory
```zsh
mkdir -p data
```

### 6. Create the Kafka Topic
```zsh
kafka-topics --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic first-kafka-topic
```

### 7. Run the Notebook
- Open `jup_test.ipynb` in Jupyter or VS Code.
- Select the `Python (env)` kernel (created by the setup script).
- Run the cells to start the streaming job.
- Place new JSON files into the `data/` directory to simulate streaming input.

### 8. Monitor the Kafka Topic
```zsh
kafka-console-consumer --bootstrap-server localhost:9092 --topic first-kafka-topic --from-beginning
```

## Notes
- The `setup.py` script automates Python environment setup and dependency installation.
- Ensure the Kafka connector package version matches your Spark and Scala versions. For Spark 3.4.x, use `org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.1`.
- Spark 4.0.0 is not yet supported for Kafka streaming as of June 2025.
- If you encounter errors, check that Java, Spark, and Kafka versions are compatible and that all services are running.

## Troubleshooting
- **NoClassDefFoundError**: Downgrade Spark to 3.4.x and use the matching Kafka connector.
- **Schema errors**: Ensure your JSON files match the schema defined in the notebook.
- **Kafka connection errors**: Make sure Kafka is running and accessible at `localhost:9092`.

## License
MIT License
