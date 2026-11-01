# Calculate response time in hours
def add_response_time(df):
    df["Response Time"] = (df["Closed Date"] - df["Created Date"]).dt.total_seconds() / 3600
    return df


# Extract closing month
def add_closed_month(df):
    df["Month"] = df["Closed Date"].dt.month
    return df


# Calculate average response time per ZIP code and month
def add_avrg_respotime_per_zip_and_month(df):
    df_grouped = df.groupby(["Incident Zip", "Month"], as_index=False)["Response Time"].mean()
    return df_grouped


# Calculate average response time per month
def add_avr_resp_per_month(df):
    df_grouped = df.groupby(["Month"], as_index=False)["Response Time"].mean()
    return df_grouped
