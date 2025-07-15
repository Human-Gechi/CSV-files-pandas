import pandas as pd
import os

def find_file(filename, search_root):
    """Search entire directory tree starting from search_root for a given filename."""
    for root, _, files in os.walk(search_root):
        if filename in files:
            return os.path.join(root, filename)
    return None

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("Data loaded successfully!")
    except pd.errors.EmptyDataError:
        print("File is empty. Starting with an empty DataFrame.")
        df = pd.DataFrame()
    return df

def add_data(df, file_path):
    if df.empty:
        columns = input("Enter column names separated by commas: ").split(",")
        df = pd.DataFrame(columns=[col.strip().capitalize() for col in columns])

    while True:
        new_data = {}
        for column in df.columns:
            new_data[column] = [input(f"Enter value for {column}: ").capitalize()]
        new_data_df = pd.DataFrame(new_data)
        df = pd.concat([df, new_data_df], ignore_index=True)

        if input("Do you intend to continue? (yes/no): ").lower() == "no":
            print("That ends it.")
            break

    df.to_csv(file_path, index=False)
    print("Data saved successfully!")
    return df

def delete_data(df, file_path):
    column_name = input("Enter the column name to delete by: ").strip()
    value = input(f"Enter the value in {column_name} to delete: ").strip()
    if column_name not in df.columns:
        print("Invalid column name")
        return df
    df = df[df[column_name].astype(str).str.lower() != value.lower()]
    df.to_csv(file_path, index=False)
    print("Data deleted and saved successfully!")
    return df

def search_data(df):
    column_name = input("Enter the column name to search: ").capitalize()
    search_value = input(f"Enter the value in {column_name}: ")
    if column_name not in df.columns:
        print("Invalid column name")
        return
    search_results = df[df[column_name].astype(str).str.contains(search_value, case=False, na=False)]
    print("Search results:" if not search_results.empty else "No results found.")
    if not search_results.empty:
        print(search_results)

def view_data(df):
    print(df)


filename = input("Enter the file name with extension (e.g., cars.csv): ").strip()


search_root = "C:\\" if os.name == 'nt' else "/"

print(f"Searching for '{filename}' in {search_root}... This may take a while.")
file_path = find_file(filename, search_root)

if file_path is None:
    print("❌ File not found anywhere in the system.")
    exit()

print(f"✅ File found at: {file_path}")
df = load_data(file_path)

while True:
    print("\nOptions: 1. Add Data  2. Search Data  3. View Data  4. Delete Data  5. Exit")
    choice = input("Enter your choice: ").strip()
    if choice == '1':
        df = add_data(df, file_path)
    elif choice == '2':
        search_data(df)
    elif choice == '3':
        view_data(df)
    elif choice == '4':
        df = delete_data(df, file_path)
    elif choice == '5':
        print("Exiting...")
        df.to_csv(file_path, index=False)
        break
    else:
        print("Invalid choice, please try again.")

df.info()