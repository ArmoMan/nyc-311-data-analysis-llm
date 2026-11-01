def calculate_rodent_percentages(df):
    # Keep only rodent complaints
    df_rodent = df[df["Complaint Type"].str.contains("Rodent", case=False, na=False)].copy()

    # Count complaints per location type
    df_rodent = df_rodent.groupby("Location Type", as_index=False, dropna=False).size()

    # Calculate percentage of total rodent complaints
    df_rodent["Percentage"] = df_rodent["size"] / df_rodent["size"].sum() * 100

    return df_rodent
