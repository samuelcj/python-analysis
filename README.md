# PYTHON ANALYSIS PROJECT

# CMDB Missing Tag Value Finder

This Python script analyzes a Configuration Management Database (CMDB) Excel file to identify entries with missing `Expected Tag Value` fields. It generates a report of these missing values and saves the results to a new Excel file.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Script Workflow](#Script-Workflow)
- [Script Details](#Script-Details)
- [How To Use The Script](#How-To-Use-The-Script)
- [Example Output](#Example-Output)

## Overview

The script reads an Excel file (`cmdb_data.xlsx`) containing CMDB data, identifies entries with missing `Expected Tag Value` fields, and saves the results to a new Excel file (`missing_tag_values.xlsx`). It uses the `pandas` library for data manipulation and analysis.

## Features

- **Load CMDB Data**: Reads an Excel file containing CMDB data.
- **Identify Missing Tag Values**: Checks for missing or blank values in the `Expected Tag Value` column.
- **Generate Report**: Creates a list of entries with missing tag values.
- **Save Results**: Exports the results to a new Excel file for further analysis.

## Installation

To use this script, you need to have Python installed along with the `pandas` library. If you don't have `pandas` installed, you can install it using pip:

```bash
pip install pandas
```

## Script Workflow

1. **Load CMDB Data**: The script loads an Excel file named `cmdb_data.xlsx` containing CMDB data.
2. **Find Missing Tag Values**: It searches for missing values in the **Expected Tag Value** column.
3. **Output Missing Values**: The results are printed to the console, showing the applications with missing tag values.
4. **Save Results**: The missing values are saved in a new Excel file, `missing_tag_values.xlsx`.

## Script Details

### 1. Importing Libraries

```python
import pandas as pd
```

The `pandas` library is used to load and manipulate the Excel data.

### 2. Loading the CMDB Data

```python
cmdb_file_path = 'cmdb_data.xlsx'
cmdb_data = pd.read_excel(cmdb_file_path)
```

The script reads the CMDB data from an Excel file named `cmdb_data.xlsx`. Ensure that this file is in the same directory as the script or modify the path.

### 3. Finding Missing Tag Values

```python
def find_missing_tag_values(data):
    missing_values = []
    
    for index, row in data.iterrows():
        app_name = row['Application Name']
        app_code = row['Application Code']
        expected_tag_key = row['Expected Tag Key']
        expected_tag_value = row['Expected Tag Value']
        
        if pd.isna(expected_tag_value) or expected_tag_value == '':
            missing_values.append({
                'Application Name': app_name,
                'Application Code': app_code,
                'Expected Tag Key': expected_tag_key,
                'Expected Tag Value': expected_tag_value
            })
    
    return missing_values
```

The `find_missing_tag_values` function checks each row in the dataset for missing **Expected Tag Value** entries (either blank or `NaN`).

### 4. Processing the Data

```python
missing_values = find_missing_tag_values(cmdb_data)

if missing_values:
    print("Applications with missing tag values:")
    for entry in missing_values:
        print(entry)
else:
    print("No missing tag values found.")
```

This part processes the data and prints missing values to the console. If no missing values are found, a message is displayed indicating that.

### 5. Saving the Results

```python
missing_values_df = pd.DataFrame(missing_values)
missing_values_df.to_excel('missing_tag_values.xlsx', index=False)
print("Results saved to 'missing_tag_values.xlsx'.")
```

If missing values are found, they are saved in a new Excel file named `missing_tag_values.xlsx`.

## How To Use The Script

1. Ensure that your CMDB data is stored in an Excel file named `cmdb_data.xlsx`.
2. Run the script using Python.
3. If any applications have missing tag values, they will be printed to the console.
4. The missing tag values will be saved to a new Excel file, `missing_tag_values.xlsx`.

## Example Output

If missing values are found, the output in the console might look like this:

```
Applications with missing tag values:
{'Application Name': 'App1', 'Application Code': '001', 'Expected Tag Key': 'Environment', 'Expected Tag Value': nan}
{'Application Name': 'App2', 'Application Code': '002', 'Expected Tag Key': 'Owner', 'Expected Tag Value': ''}
```

The `missing_tag_values.xlsx` file will contain the same data.

## Notes

- The script expects the CMDB Excel file to contain the following columns:
  - `Application Name`
  - `Application Code`
  - `Expected Tag Key`
  - `Expected Tag Value`
  
- The column names should be adjusted in the script if the structure of your CMDB file differs.
- Missing tag values are determined by checking if the **Expected Tag Value** field is either empty or contains `NaN`.

