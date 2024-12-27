import pandas as pd
import os.path

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
parquet_path = './data/iris.parquet'

if not os.path.exists(parquet_path):
    # Also ensure the directory exists
    os.makedirs(os.path.dirname(parquet_path), exist_ok=True)

    # Download and save only if the file doesn't exist
    iris = pd.read_csv(url)
    iris.to_parquet(parquet_path)
    print("Created new parquet file")
else:
    print("Parquet file already exists")

iris = pd.read_parquet(parquet_path)

print(iris)
