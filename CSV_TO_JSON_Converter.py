import argparse
import csv
import json
import sys
from datetime import datetime

def format_date(date_str):
    try:
        # Try parsing the date in YYYY-MM-DD format
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        return dt.strftime("%B %d %Y").lower()
    except Exception:
        return date_str  # Return as is if parsing fails

def csv_to_json(csv_file_path, json_file_path):
    try:
        with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = []
            for row in reader:
                # Add note that rating is out of 10
                if "Rating" in row and row["Rating"]:
                    row["Rating"] = f"{row['Rating']} (out of 10)"
                # Format the date field
                if "Date" in row and row["Date"]:
                    row["Date"] = format_date(row["Date"])
                data.append(row)
        with open(json_file_path, mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Successfully converted '{csv_file_path}' to '{json_file_path}'.")
    except FileNotFoundError:
        print(f"Error: File '{csv_file_path}' not found.", file=sys.stderr)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)

def main():
    parser = argparse.ArgumentParser(description="Convert a CSV file to JSON format. Ratings are given out of 10. Dates are formatted as 'month day year'.")
    parser.add_argument("csv_file", help="Path to the input CSV file")
    parser.add_argument("json_file", help="Path to the output JSON file")
    args = parser.parse_args()
    csv_to_json(args.csv_file, args.json_file)

if __name__ == "__main__":
    main()