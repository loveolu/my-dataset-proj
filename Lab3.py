import argparse
import pandas as pd  # You need to import pandas

# Function 1: Sequential Split (80% train, 20% test)
def splitData(df):
    """
    This function splits the dataset sequentially into 80% training data and 20% testing data.
    """
    train_size = int(len(df) * 0.8)
    train_data = df[:train_size]
    test_data = df[train_size:]
    return train_data, test_data

# Function 2: Random Split (80% train, 20% test)
def splitDataRandom(df):
    """
    This function splits the dataset randomly into 80% training data and 20% testing data.
    """
    # Using train_test_split from pandas
    df_shuffled = df.sample(frac=1, random_state=42).reset_index(drop=True)  # Shuffle the data
    train_size = int(len(df_shuffled) * 0.8)
    train_data = df_shuffled[:train_size]
    test_data = df_shuffled[train_size:]
    return train_data, test_data

# Function 3: Three-Way Split (70% train, 15% validation, 15% test)
def splitDataThreeWay(df):
    """
    This function splits the dataset into three parts:
    70% training data, 15% validation data, and 15% testing data.
    """
    train_size = int(len(df) * 0.7)
    val_size = int(len(df) * 0.15)

    train_data = df[:train_size]
    val_data = df[train_size:train_size + val_size]
    test_data = df[train_size + val_size:]

    return train_data, val_data, test_data

# Function 4: Dataset Statistics (mean, max, min, correlation)
def datasetStatistics(df):
    """
    This function computes and prints basic statistics of the dataset:
    mean, max, min, and correlation.
    """
    print("Dataset Statistics:")
    print(f"Mean:\n{df.mean()}")
    print(f"Max:\n{df.max()}")
    print(f"Min:\n{df.min()}")
    print(f"Correlation:\n{df.corr()}")

# Command-Line Argument Handling
def main():
    parser = argparse.ArgumentParser(description="Titanic Dataset Splitter")
    parser.add_argument("--file", required=True, help="Path to dataset file")
    args = parser.parse_args
