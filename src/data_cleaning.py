import pandas as pd


# Remove rows with missing closing dates
def remove_rows_missing_closed_date(df, column_name):
    return df[df[column_name].notna()]


# Remove rows where closing date is earlier than creation date
def remove_bigger_created_dates(df):
    df["Created Date"] = pd.to_datetime(df["Created Date"], format="%m/%d/%Y %I:%M:%S %p")
    df["Closed Date"] = pd.to_datetime(df["Closed Date"], format="%m/%d/%Y %I:%M:%S %p")
    return df[df["Closed Date"] >= df["Created Date"]]
