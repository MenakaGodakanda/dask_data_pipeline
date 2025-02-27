import dask.dataframe as dd

def clean_data(df):
    """Clean and transform data using Dask."""
    df = df.dropna()  # Drop missing values
    df['column_x'] = df['column_x'].astype(float)  # Ensure correct types
    df = df[df['column_x'] > 0]  # Filter invalid values
    return df

def aggregate_data(df):
    """Perform aggregation operations."""
    result = df.groupby('category_column').agg({'column_x': 'mean'}).compute()
    return result

if __name__ == "__main__":
    df = dd.read_csv("./data/large_dataset.csv")
    df = clean_data(df)
    aggregated_result = aggregate_data(df)
    print(aggregated_result)

