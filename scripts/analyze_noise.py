
import pandas as pd

from src.paths import DATA_PROCESSED
from src.noise_analysis import calculate_noise_percentages


def main():
    df = pd.read_csv(DATA_PROCESSED / "2024data.csv", low_memory=False)

    # Calculate noise percentages
    df_final = calculate_noise_percentages(df)

    # Save processed results
    df_final.to_csv(DATA_PROCESSED / "noise_percentages.csv")


if __name__ == "__main__":
    main()
