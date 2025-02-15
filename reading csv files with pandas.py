import pandas as pd
def get_file_path():
    return input("Enter the path of the CSV file: ").strip()
# loading data
def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
    except pd.errors.EmptyDataError:
        df = pd.DataFrame()
    return df
def add_data(df):
    while True:
        new_data = {}
        for column in df.columns:
            new_data[column] = [input(f"Enter value for {column}: ").capitalize()]

        new_data_df = pd.DataFrame(new_data)
        df = pd.concat([df, new_data_df], ignore_index=True)

        extra = input("Do you intend to continue? (yes/no): ").lower()
        if extra == "no":
            print("That ends it.")
            break
    df.to_csv(file_path, index=False)
    print("Data saved successfully!")
    return df
def delete_data(df):
    column_name = input("Enter the column name to delete by: ").strip()
    value = input(f"Enter the value in {column_name} to delete: ").strip()

    if column_name not in df.columns:
        print("Invalid column name")
        return df
    df = df[df[column_name].astype(str).str.lower() != value.lower()]
    df.to_csv(file_path, index=False)
    print("Data deleted and saved successfully!")
    return df
# Function to search data
def search_data(df):
    column_name = input("Enter the column name to search: ").capitalize()
    search_value = input(f"Enter the value in {column_name}:")

    if column_name not in df.columns:
        print("Invalid column name")
        return
    search_results = df[df[column_name].astype(str).str.contains(search_value, case=False, na=False)]
    if search_results.empty:
        print("No results found.")
    else:
        print("Search results:")
        print(search_results)
def view_data(df):
    print(df)
file_path = get_file_path()
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
df.info()
print(df)