import numpy as np
import pandas as pd

def create_and_filter_data():

    np.random.seed(123)

    arr = np.random.randint(0, 101, size=(10, 2))

    df = pd.DataFrame(arr, columns=['A', 'B'])

    filtered_df = df[df['A'] > 50]

    return filtered_df

if __name__ == '__main__':
    result_df = create_and_filter_data()
    print("Otrzymany DataFrame (A > 50):")
    print(result_df)
