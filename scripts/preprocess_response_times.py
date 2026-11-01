import pandas as pd

from src.paths import DATA_PROCESSED
from src.data_cleaning import remove_rows_missing_closed_date, remove_bigger_created_dates
from src.response_time_analysis import add_response_time, add_closed_month, add_avrg_respotime_per_zip_and_month, add_avr_resp_per_month


def main():
    path_2024 = DATA_PROCESSED / "2024_trimmed_data.csv"
    zipcode_average_path = DATA_PROCESSED / "zipcode_response_times.csv"
    months_average_path = DATA_PROCESSED / "monthly_response_times.csv"

    # Load 2024 data
    df = pd.read_csv(path_2024, low_memory=False)

    # Clean data
    df = remove_rows_missing_closed_date(df, "Closed Date")
    df = remove_bigger_created_dates(df)

    # Add response time and closing month
    df = add_response_time(df)
    df = add_closed_month(df)

    # Calculate average response times
    zipcode_average = add_avrg_respotime_per_zip_and_month(df)
    months_average = add_avr_resp_per_month(df)

    # Save processed results
    zipcode_average.to_csv(zipcode_average_path, index=False)
    months_average.to_csv(months_average_path, index=False)

if __name__ == "__main__":
    main()



