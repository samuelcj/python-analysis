import pandas as pd

# Load the CMDB Excel file
cmdb_file_path = 'cmdb_data.xlsx'
cmdb_data = pd.read_excel(cmdb_file_path)

# Function to find applications with missing tag values
def find_missing_tag_values(data):
    missing_values = []

    for index, row in data.iterrows():
        app_name = row['Application Name']
        app_code = row['Application Code']
        expected_tag_key = row['Expected Tag Key']
        expected_tag_value = row['Expected Tag Value']

        # Check if the Expected Tag Value is missing (blank or NaN)
        if pd.isna(expected_tag_value) or expected_tag_value == '':
            missing_values.append({
                'Application Name': app_name,
                'Application Code': app_code,
                'Expected Tag Key': expected_tag_key,
                'Expected Tag Value': expected_tag_value
            })

    return missing_values

# Find applications with missing tag values
missing_values = find_missing_tag_values(cmdb_data)

# Print the results
if missing_values:
    print("Applications with missing tag values:")
    for entry in missing_values:
        print(entry)
else:
    print("No missing tag values found.")
    
# Convert missing values to a DataFrame
missing_values_df = pd.DataFrame(missing_values)

# Save to a new Excel file
missing_values_df.to_excel('missing_tag_values.xlsx', index=False)
print("Results saved to 'missing_tag_values.xlsx'.")