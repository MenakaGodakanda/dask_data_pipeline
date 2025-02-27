# Dask Data Pipeline for Large-Scale Data Processing

This project demonstrates how to build a custom data pipeline using Dask and Python for efficient large-scale data processing on Ubuntu. The project is fully open-source and optimized for performance.

## Overview
<img width="1283" alt="Screenshot 2025-02-27 at 4 45 15 pm" src="https://github.com/user-attachments/assets/33832dd9-777f-4313-b879-762e6e377062" />

### Explanation
The pipeline consists of three stages:
- **Data Ingestion** – Load large CSV files using Dask.
- **Data Processing** – Clean, filter, and aggregate large datasets efficiently.
- **Data Analysis & Visualization** – Generate insights and visualizations.

## Installation & Setup

###1. Prerequisites
Ensure you have Ubuntu, Python 3.8+, and pip installed.
```
sudo apt update
sudo apt install python3 python3-pip -y
```

### 2. Clone the Repository
```
git clone https://github.com/MenakaGodakanda/dask-data-pipeline.git
cd dask_data_pipeline
```

### 3. Create a Virtual Environment
```
python3 -m venv pipeline
source pipeline/bin/activate
```

### 4. Install Dependencies
```
pip install dask pandas numpy matplotlib pyarrow
```
- **Dask (`dask`)**
  - A parallel computing library that scales Python code for large datasets.
  - Used for efficient data ingestion, processing, and computation.
  - Works similarly to pandas but optimized for big data.

- **Pandas (`pandas`)**
  - A data manipulation and analysis library.
  - Used for handling tabular data (CSV, SQL, etc.).
  - Helps in creating test datasets and small-scale operations.

- **NumPy (`numpy`)**
  - A library for numerical computing and handling large arrays.
  - Provides efficient mathematical operations for data transformation.
  - Used in generating random datasets and numerical computations.

- **Matplotlib (`matplotlib`)**
  - A plotting library for visualizing data.
  - Used to create bar charts, histograms, and other plots.
  - Helps in analyzing processed results.

- **PyArrow (`pyarrow`)**
  - A library for handling Apache Arrow columnar data format.
  - Improves the efficiency of data storage and memory operations.
  - Used in Dask to process large-scale data faster.

### 5. Running the Data Pipeline

#### Step 1: Generate a Large CSV File
Run the script to create a 1 million-row dataset for testing.
```
python scripts/dummy_data.py
```
- The generate file will save in `data/` folder.
![Screenshot 2025-02-27 160639](https://github.com/user-attachments/assets/64b96871-eafd-405b-8fa7-8da8ca29606a)
![Screenshot 2025-02-27 161116](https://github.com/user-attachments/assets/260bb3bc-3578-4675-ba23-7c4899bbcf76)

#### Step 2: Run the Pipeline
- You can manually run each script.
- **Data Ingestion (`data_ingestion.py`)**
  - Loads large CSV files efficiently using Dask.
  - Uses lazy evaluation for memory-efficient operations.
  - Outputs the first few rows of the dataset.
```
python scripts/data_ingestion.py
```
![Screenshot 2025-02-27 161008](https://github.com/user-attachments/assets/7c08d762-1198-4dae-b499-d595c89e84b7)

- **Data Processing (`data_processing.py`)**
  - Cleans data (drops missing values, converts types, and filters invalid values).
  - Performs aggregation (e.g., calculates the mean of a column by category).
  - Saves the processed data.
```
python scripts/data_processing.py
```
![Screenshot 2025-02-27 161024](https://github.com/user-attachments/assets/2e5d262d-02ae-4941-a207-a459a36e245a)

- **Data Analysis (`data_analysis.py`)**
  - Generates bar charts to visualize aggregated results.
  - Uses Matplotlib for visualization.
  - Computes results efficiently using Dask's parallel processing.
```
python scripts/data_analysis.py
```
![Screenshot 2025-02-27 161058](https://github.com/user-attachments/assets/7b08f36c-4b26-4a1f-aae2-bb33fa2cfd18)

- A bar chart is generated showing the average value of `column_x grouped` by `category_column` (A, B, C, D).

- Or automate the entire process using:
```
chmod +x run_pipeline.sh
./run_pipeline.sh
```
![Screenshot 2025-02-27 161302](https://github.com/user-attachments/assets/ad753369-1f39-4e5e-8a8d-468588e1ae49)

## Project Structure
```
dask_data_pipeline/
│── data/                    # Directory for input/output data
│── scripts/                 # Python scripts for processing
│   ├── data_ingestion.py    # Load data
│   ├── data_processing.py   # Process data with Dask
│   ├── data_analysis.py     # Analyze and visualize data
│   ├── dummy_data.py        # Script to create a large CSV dataset
│── notebooks/               # Jupyter Notebooks for testing
│── run_pipeline.sh          # Shell script to automate execution
│── README.md                # Project documentation
```

## License

This project is open-source under the MIT License.
