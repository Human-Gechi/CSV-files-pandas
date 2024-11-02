import pandas as pd

# Load the existing CSV file
file_path = r"C:\Users\HP\file.csv"
column_names = ["Name", "Matric number", "Department", "Faculty"]

# Function to load data
def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
    except pd.errors.EmptyDataError:
        df = pd.DataFrame(columns=column_names)
    return df

# Function to add new data
def add_data(df):
    while True:
        # Prepare new data to add from terminal input
        mixed_input = input("Enter the mixed input (format: XXX/YYYY/NNN): ").capitalize()
        parts = mixed_input.split('/')

        # Convert and store the parts
        string_part = parts[0].capitalize()
        int_part1 = int(parts[1])
        int_part2 = int(parts[2])

        new_data = pd.DataFrame({
            "Name": [input("Enter your name: ").capitalize()],
            "Matric number": [mixed_input],
            "Department": [input("Enter your department here: ").capitalize()],
            "Faculty": [input("Enter faculty name here: ").capitalize()]
        })

        # Append new data to the DataFrame
        df = pd.concat([df, new_data], ignore_index=True)

        # Ask if the user wants to continue
        extra = input("Do you intend to continue? (yes/no): ").lower()
        if extra == "no":
            print("That ends it.")
            break

    df_sorted = df.sort_values(by=["Faculty", "Department", "Matric number", "Name"])
    # Save the sorted DataFrame back to the original CSV file
    df_sorted.to_csv(file_path, index=False)
    print("Data saved successfully!")
    return df_sorted

# Function to delete data
def delete_data(df):
    column_name = input("Enter the column name to delete by: ").capitalize()
    value = input(f"Enter the value in {column_name} to delete: ")
    if column_name not in df.columns:
        print("Invalid column name")
        return df
    # Filter out rows that match the condition
    df = df[df[column_name].astype(str) != value]
    
    # Save the updated DataFrame
    df.to_csv(file_path, index=False)
    print("Data deleted and saved successfully!")
    return df

# Function to search data
def search_data(df):
    column_name = input("Enter the column name to search: ").capitalize()
    search_value = input("Enter the search value: ")

    if column_name not in df.columns:
        print("Invalid column name")
        return

    search_results = df[df[column_name].astype(str).str.contains(search_value, case=False, na=False)]
    if search_results.empty:
        print("No results found.")
    else:
        print("Search results:")
        print(search_results)

# Function to view data
def view_data(df):
    print(df)

df = load_data(file_path)
while True:
    print("Options: 1. Add Data  2. Search Data  3. View Data 4. Delete Data 5. Exit")
    choice = input("Enter your choice: ").strip()

    if choice == '1':
        df = add_data(df)
    elif choice == '2':
        search_data(df)
    elif choice == '3':
        view_data(df)
    elif choice == '4':
        df = delete_data(df)
    elif choice == '5':
        print("Exiting...")
        df.to_csv(file_path, index=False)
        break
    else:
        print("Invalid choice, please try again.")