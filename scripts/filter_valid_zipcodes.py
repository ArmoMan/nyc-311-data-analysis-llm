import pandas as pd
from src.paths import DATA_PROCESSED

"""
I did this before running this script in the terminal: 
    echo "Unique Key,Created Date,Closed Date,Agency,Agency Name,Complaint Type,Descriptor,Location Type,Incident Zip,Incident Address,Street Name,Cross Street 1,Cross Street 2,Intersection Street 1,Intersection Street 2,Address Type,City,Landmark,Facility Type,Status,Due Date,Resolution Description,Resolution Action Updated Date,Community Board,BBL,Borough,X Coordinate (State Plane),Y Coordinate (State Plane),Open Data Channel Type,Park Facility Name,Park Borough,Vehicle Type,Taxi Company Borough,Taxi Pick Up Location,Bridge Highway Name,Bridge Highway Direction,Road Ramp,Bridge Highway Segment,Latitude,Longitude,Location" > 2024data.csv

    csvtool col 2 311_Service_Requests_from_2010_to_Present_20250928.csv | grep -E '[0-9]{1,2}/[0-9]{1,2}/2024' >> 2024data.csv
"""

def main():
    df = pd.read_csv(DATA_PROCESSED / "2024data.csv", low_memory=False)
    # Remove complaints with missing ZIP codes
    df = df[df["Incident Zip"].notnull()]
    df.to_csv(DATA_PROCESSED / "2024_trimmed_data.csv", index=False)

if __name__ == "__main__":
    main()
