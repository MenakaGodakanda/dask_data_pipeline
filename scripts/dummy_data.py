import pandas as pd
import numpy as np

# Generate a large dataset with random values
num_rows = 1_000_000
data = {
    'category_column': np.random.choice(['A', 'B', 'C', 'D'], num_rows),
    'column_x': np.random.randn(num_rows) * 100
}

df = pd.DataFrame(data)
df.to_csv("data/large_dataset.csv", index=False)

