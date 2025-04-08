import json
from sklearn.model_selection import train_test_split

# Load the JSON data
with open('journal_entries.json', 'r') as f:
    data = json.load(f)

# Split the data into training, validation, and test sets
train_data, temp_data = train_test_split(data, test_size=0.3, random_state=42)
val_data, test_data = train_test_split(temp_data, test_size=0.5, random_state=42)

# Save the splits into separate JSON files
with open('train_data.json', 'w') as f:
    json.dump(train_data, f, indent=4)

with open('val_data.json', 'w') as f:
    json.dump(val_data, f, indent=4)

with open('test_data.json', 'w') as f:
    json.dump(test_data, f, indent=4)

print("Data split completed.")
