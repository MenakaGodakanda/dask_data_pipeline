import dask.dataframe as dd
import matplotlib.pyplot as plt

def plot_data(df):
    """Generate a simple plot from aggregated data."""
    result = df.groupby('category_column').agg({'column_x': 'mean'}).compute()
    
    result.plot(kind='bar', figsize=(10,5))
    plt.xlabel('Category')
    plt.ylabel('Average Value')
    plt.title('Average Column X by Category')
    plt.show()

if __name__ == "__main__":
    df = dd.read_csv("./data/large_dataset.csv")
    plot_data(df)

