import argparse
import csv
from datetime import datetime


def main():
    parser = argparse.ArgumentParser(description="Count NYC 311 complaints by type and borough within a date range.")

    parser.add_argument("-i", "--input", type=str, required=True, help="Path to input CSV file")
    parser.add_argument("-s", "--start", type=str, required=True, help="Start date (MM/DD/YYYY)")
    parser.add_argument("-e", "--end", type=str, required=True, help="End date (MM/DD/YYYY)")
    parser.add_argument("-o", "--output", type=str, help="Path to output CSV file (optional)")

    args = parser.parse_args()

    saved_data = {}
    start_date = datetime.strptime(args.start, "%m/%d/%Y").date()
    end_date = datetime.strptime(args.end, "%m/%d/%Y").date()

    # Count complaints by type and borough within the date range
    with open(args.input, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            complaint_date = datetime.strptime(row["Created Date"], "%m/%d/%Y %I:%M:%S %p").date()

            if start_date <= complaint_date <= end_date:
                key = (row["Complaint Type"], row["Borough"])
                saved_data[key] = saved_data.get(key, 0) + 1

    # Write results to a CSV file or terminal
    if args.output:
        with open(args.output, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Complaint Type", "Borough", "Count"])

            for (complaint_type, borough), count in saved_data.items():
                writer.writerow([complaint_type, borough, count])
    else:
        writer = csv.writer(__import__("sys").stdout)
        writer.writerow(["Complaint Type", "Borough", "Count"])

        for (complaint_type, borough), count in saved_data.items():
            writer.writerow([complaint_type, borough, count])


if __name__ == "__main__":
    main()
