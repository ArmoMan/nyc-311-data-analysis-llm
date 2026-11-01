from bokeh.plotting import figure, show
from bokeh.palettes import viridis

import pandas as pd
from src.paths import DATA_PROCESSED


def main():
    # Load noise complaint percentages
    path_f = DATA_PROCESSED / "noise_percentages.csv"
    df = pd.read_csv(path_f, low_memory=False).fillna(0)

    # Convert months to strings for Bokeh categorical axis
    df["Created Date"] = df["Created Date"].astype(str)
    months = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

    # Create figure
    fig = figure(x_range=months, height=800, width=900, title="Noise Complaints by Month")

    # Create stacked bar chart
    cols = viridis(len(df.columns[1:]))
    fig.vbar_stack(list(df.columns[1:]), x="Created Date", source=df, color=cols, width=0.5, legend_label=list(df.columns[1:]))

    # Move legend outside the plot
    legend = fig.legend[0]
    fig.add_layout(legend, "right")

    # Axis labels
    fig.xaxis.axis_label = "Month"
    fig.yaxis.axis_label = "Percentage (%)"

    show(fig)


if __name__ == "__main__":
    main()

