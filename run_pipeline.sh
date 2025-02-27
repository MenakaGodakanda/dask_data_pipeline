#!/bin/bash
source pipeline/bin/activate
echo "Running Data Ingestion..."
python scripts/data_ingestion.py
echo "Running Data Processing..."
python scripts/data_processing.py
echo "Running Data Analysis..."
python scripts/data_analysis.py

