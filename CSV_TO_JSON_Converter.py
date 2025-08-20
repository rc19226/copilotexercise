#movies data is upto date i am just experimenting with pull requests

import argparse
import csv
import json
import sys

def csv_to_json(csv_file_path, json_file_path):
    try:
        with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)
        with open(json_file_path, mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Successfully converted '{csv_file_path}' to '{json_file_path}'.")
    except FileNotFoundError:
        print(f"Error: File '{csv_file_path}' not found.", file=sys.stderr)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)

def main():
    parser = argparse.ArgumentParser(description="Convert a CSV file to JSON format.")
    parser.add_argument("csv_file", help="Path to the input CSV file")
    parser.add_argument("json_file", help="Path to the output JSON file")
    args = parser.parse_args()
    csv_to_json(args.csv_file, args.json_file)

if __name__ == "__main__":
    main()