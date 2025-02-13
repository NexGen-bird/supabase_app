from datetime import datetime
from libs.applibs.utils import date_format
data = [
    {'id': '52abdb6c-03e0-4db8-b1cc-58f71c16196e', 'name': 'Jayesh T', 'email': 'jayeshT@gmail.com', 'address': 'Test', 'phone_number': '9702071144', 'planstartdate': '2025-02-04', 'planexpirydate': '2025-03-03'},
    {'id': '52abdb6c-03e0-4db8-b1cc-58f71c16196e', 'name': 'Jayesh T', 'email': 'jayeshT@gmail.com', 'address': 'Test', 'phone_number': '9702071144', 'planstartdate': '2025-02-04', 'planexpirydate': '2025-03-05'},
    {'id': 'bcc00d31-99e0-4814-8c94-08cd090e82e4', 'name': 'Rocky Kamble', 'email': 'rockykamble@gmail.com', 'address': 'Test', 'phone_number': '1234567890', 'planstartdate': '2025-02-03', 'planexpirydate': '2025-03-02'}
]

# Sort data by 'planexpirydate' in descending order
sorted_data = sorted(data, key=lambda x: datetime.strptime(x['planexpirydate'], "%Y-%m-%d"), reverse=False)

# Function to process sorted records
def process_records(records):
    for record in records:
        print(f"Processing: {record['name']} with expiry date {date_format(record['planexpirydate'])}")

# Pass sorted records to function
process_records(sorted_data)
