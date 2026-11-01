import pandas as pd
from src.paths import DATA_PROCESSED


def get_top_noise_descriptor(month):
    if type(month) is not int or not 1 <= month <= 12:
        raise ValueError("Month must be an integer between 1 and 12")

    df = pd.read_csv(DATA_PROCESSED / "noise_percentages.csv", low_memory=False)

    # Filter to only keep rows with month
    df = df[df["Created Date"] == month]

    if df.empty:
        return {"error": "No data available for noise descriptor"}

    # Remove the month column
    df = df.drop(columns=["Created Date"]).fillna(0)

    # Get column with highest percentage
    # Personal note: idxmax(axis=1) finds the column name with the highest value for each row. It returns one result per row, so I use iloc[0].
    highest_column = df.idxmax(axis=1).iloc[0]
    highest_percentage = df[highest_column].iloc[0]

    return {"month": month, "descriptor": str(highest_column), "percentage": float(highest_percentage)}


def get_top_rodent_location():
    df = pd.read_csv(DATA_PROCESSED / "rodent_percentages.csv", low_memory=False)

    # Sort location types by percentage (highest first) of rodent complaints
    df = df.sort_values("Percentage", ascending=False)

    if df.empty:
        return {"error": "No data available for rodent location"}

    return {"location_type": str(df.iloc[0]["Location Type"]), "complaints_size": int(df.iloc[0]["size"]), "percentage": float(df.iloc[0]["Percentage"])}



def get_slowest_zipcode(month):
    return _get_zipcode_by_response_time(month, is_ascending=False)

def get_fastest_zipcode(month):
    return _get_zipcode_by_response_time(month, is_ascending=True)

# helper method to find zip code by response time
def _get_zipcode_by_response_time(month, is_ascending):
    if type(month) is not int or not 1 <= month <= 12:
        raise ValueError("Month must be an integer between 1 and 12")
    df = pd.read_csv(DATA_PROCESSED / "zipcode_response_times.csv", low_memory=False)

    # Filter by month
    df = df[df["Month"] == month]

    if df.empty:
        return {"error": "No response time data available for this month"}

    # Sort response times
    df = df.sort_values("Response Time", ascending=is_ascending)

    return {"month": month, "zipcode": str(df.iloc[0]["Incident Zip"]), "response_time": float(df.iloc[0]["Response Time"])}