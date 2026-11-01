import pandas as pd

from src.paths import DATA_PROCESSED
from src.rodent_analysis import calculate_rodent_percentages


def main():
    df = pd.read_csv(DATA_PROCESSED / "2024data.csv", low_memory=False)

    # Calculate rodent percentages
    df_rodent = calculate_rodent_percentages(df)

    # Save processed results
    df_rodent.to_csv(DATA_PROCESSED / "rodent_percentages.csv", index=False)


if __name__ == "__main__":
    main()
