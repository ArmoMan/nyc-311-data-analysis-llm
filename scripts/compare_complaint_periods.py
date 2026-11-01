
import pandas as pd
import matplotlib.pyplot as plt

from src.paths import DATA_PROCESSED


def main():
    # Load complaint counts for both periods
    jan_feb = pd.read_csv(DATA_PROCESSED / "complaints_jan_feb.csv")
    jun_jul = pd.read_csv(DATA_PROCESSED / "complaints_jun_jul.csv")

    # Group complaint counts by type
    jan_feb_grouped = jan_feb.groupby("Complaint Type", as_index=False)["Count"].sum()

    # Find the most frequent complaint type in January-February
    jan_feb_grouped = jan_feb_grouped.sort_values(by="Count", ascending=False)
    top_complaint = jan_feb_grouped.iloc[0]["Complaint Type"]

    # Filter both periods for the same complaint type
    jan_feb = jan_feb[jan_feb["Complaint Type"] == top_complaint].sort_values(by="Borough")
    jun_jul = jun_jul[jun_jul["Complaint Type"] == top_complaint].sort_values(by="Borough")

    # Plot January-February complaints
    plt.bar(jan_feb["Borough"], jan_feb["Count"])
    plt.xlabel("Borough")
    plt.ylabel("Complaint Count")
    plt.title(f"{top_complaint} Complaints (January-February 2024)")
    plt.tight_layout()
    plt.show()

    # Plot June-July complaints
    plt.bar(jun_jul["Borough"], jun_jul["Count"])
    plt.xlabel("Borough")
    plt.ylabel("Complaint Count")
    plt.title(f"{top_complaint} Complaints (June-July 2024)")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
