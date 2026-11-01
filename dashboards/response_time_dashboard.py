
from bokeh.plotting import figure
from bokeh.models import Dropdown
from bokeh.events import MenuItemClick
from bokeh.layouts import column
from bokeh.io import curdoc

import pandas as pd
from src.paths import DATA_PROCESSED


# File paths
zipcode_average_path = DATA_PROCESSED / "zipcode_response_times.csv"
months_average_path = DATA_PROCESSED / "monthly_response_times.csv"

# Load processed data
df_zipcode = pd.read_csv(zipcode_average_path)
df_months = pd.read_csv(months_average_path)

# Create figure
graph = figure(title="Monthly Average 311 Complaint Response Time", x_axis_label="Month", y_axis_label="Average Response Time (hours)")

# Get unique zip codes for dropdowns
unique_zip_codes = list(map(str, df_zipcode["Incident Zip"].unique()))

# Plot overall monthly average
x_all = df_months["Month"]
y_all = df_months["Response Time"]
graph.line(x_all, y_all, legend_label="All ZIP Codes", color="red")

# Create lines for selected ZIP codes
line1 = graph.line([], [], legend_label="ZIP Code 1", color="blue")
line2 = graph.line([], [], legend_label="ZIP Code 2", color="green")

# Create dropdowns
dropdown1 = Dropdown(label="ZIP Code 1", button_type="warning", menu=unique_zip_codes)
dropdown2 = Dropdown(label="ZIP Code 2", button_type="warning", menu=unique_zip_codes)


def select_dropdown1(event):
    selected_rows = df_zipcode[df_zipcode["Incident Zip"].astype(str) == event.item]
    line1.data_source.data = {"x": selected_rows["Month"].tolist(), "y": selected_rows["Response Time"].tolist()}
    dropdown1.label = event.item


def select_dropdown2(event):
    selected_rows = df_zipcode[df_zipcode["Incident Zip"].astype(str) == event.item]
    line2.data_source.data = {"x": selected_rows["Month"].tolist(), "y": selected_rows["Response Time"].tolist()}
    dropdown2.label = event.item


dropdown1.on_event(MenuItemClick, select_dropdown1)
dropdown2.on_event(MenuItemClick, select_dropdown2)

# Add dashboard to Bokeh document
curdoc().add_root(column(dropdown1, dropdown2, graph))
