import dask.dataframe as dd

def load_data(file_path):
    """Load large CSV file using Dask."""
    df = dd.read_csv(file_path)
    return df

if __name__ == "__main__":
    df = load_data("./data/large_dataset.csv")
    print(df.head())  # Print a few rows

