import numpy as np
import pandas as pd

"""
the following was fetched from the homework itself.
"""

# Generate a random dataframe with 30 columns and 30 rows
num_rows = 30
num_columns = 30

# Generate random values between 0 and 10
random_values = np.random.randint(0, 11, size=(num_rows, num_columns))

# Create a dataframe
df = pd.DataFrame(random_values)

# Add column names
column_names = ['Q{}'.format(i) for i in range(1, num_columns+1)]
df.columns = column_names

# Add row names
row_names = ['S{}'.format(i) for i in range(1, num_rows+1)]
df.index = row_names
path_variable = "../exported_csv_files/raw_score_dataframe.csv"
df.to_csv(
    path_or_buf=path_variable,
    sep=",",
    index=True,
    header=True
)
