# report/generate_csv.py

import csv
import os

def write_report(data_list, output_path):
    if not data_list:
        print("⚠ No data to write.")
        return

    # Get all unique field names across all dicts
    fieldnames = set()
    for data in data_list:
        fieldnames.update(data.keys())
    fieldnames = list(fieldnames)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in data_list:
            writer.writerow(row)

    print(f"[📄] Report saved at {output_path}")
