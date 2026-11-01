# NYC 311 Data Analysis with LLM

A Python-based data analysis project exploring New York City's 311 service requests from 2024.

This project was initially developed as part of COMP 370 coursework at McGill University. The different assignments were later merged into a single project, with the goal of integrating an LLM to answer questions directly about the available data. The AI will use existing Python functions to retrieve and analyze relevant data, then present the results in natural language.

## Features

- Data cleaning and preprocessing of NYC 311 complaints
- Complaint analysis by borough and date range
- Monthly response-time analysis by ZIP code
- Noise complaint analysis by month and descriptor
- Rodent complaint analysis by location type
- Interactive visualizations using Bokeh

## Technologies Used

Python, Pandas, Matplotlib, Bokeh, Git

## Project Structure

- `src/` → Reusable data processing and analysis functions
- `scripts/` → Data preprocessing and analysis scripts
- `dashboards/` → Bokeh visualizations
- `data/raw/` → Original datasets
- `data/processed/` → Processed datasets
- `notebooks/` → Exploratory data analysis
- `docs/` → Documentation

## Installation

Set up a virtual environment and install the required packages:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

Run the noise and rodent dashboards:

```bash
python -m dashboards.noise_dashboard
python -m dashboards.rodent_dashboard
```

For the interactive response-time dashboard:

```bash
PYTHONPATH=. bokeh serve dashboards/response_time_dashboard.py --show
```

## Project Background

Initially developed as part of COMP 370 coursework at McGill University, this project combines data processing, statistical analysis, and interactive visualizations.

The next step is to integrate an LLM that can interpret user questions and call predefined Python functions to retrieve relevant statistics from the datasets.