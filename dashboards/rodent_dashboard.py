
from bokeh.plotting import figure, show
import pandas as pd

from src.paths import DATA_PROCESSED


def main():
    # Load rodent complaint percentages
    path_f = DATA_PROCESSED / "rodent_percentages.csv"
    df = pd.read_csv(path_f, low_memory=False).fillna(0)

    # Sort location types by percentage (highest first)
    df = df.sort_values("Percentage", ascending=False)

    # Extract location types and percentages
    location_type = list(df["Location Type"])
    percentage = list(df["Percentage"])

    # Create bar chart
    p = figure(x_range=location_type, height=800, width=1500, title="Rodent Complaints by Location Type", toolbar_location=None, tools="")

    p.vbar(x=location_type, top=percentage, width=0.5)

    # Configure graph
    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.xaxis.axis_label = "Location Type"
    p.yaxis.axis_label = "Percentage of Rodent Complaints (%)"
    p.xaxis.major_label_orientation = 189.4

    show(p)


if __name__ == "__main__":
    main()
