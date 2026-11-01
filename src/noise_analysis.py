import pandas as pd


def calculate_noise_percentages(df):
    # Keep only noise complaints
    df_noise = df[df["Complaint Type"].str.contains("Noise", case=False, na=False)].copy()

    # Extract month from creation date
    df_noise["Created Date"] = pd.to_datetime(df_noise["Created Date"], format="%m/%d/%Y %I:%M:%S %p").dt.month

    # Keep only month and descriptor
    df_month_only = df_noise[["Created Date", "Descriptor"]].copy()

    # Count complaints per month and descriptor
    df_grouped = df_month_only.groupby(["Created Date", "Descriptor"], as_index=False, dropna=False).size()

    # Calculate percentage per month
    monthly_totals = df_grouped.groupby("Created Date")["size"].sum()
    df_grouped["Percentage"] = (df_grouped["size"] / df_grouped["Created Date"].map(monthly_totals)) * 100

    # Pivot: months as rows, descriptors as columns
    df_final = df_grouped.pivot(index="Created Date", columns="Descriptor", values="Percentage")

    return df_final
