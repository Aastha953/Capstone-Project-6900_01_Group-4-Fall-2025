import pandas as pd

# === Load the Combined Dataset ===
file_path = r"C:\Users\aasth\Downloads\Combined_Traffic_Data cleaned.csv"
df = pd.read_csv(file_path)

# === Remove 'Unnamed' Columns ===
df = df.loc[:, ~df.columns.str.contains('^Unnamed', case=False)]
print("✅ Removed Unnamed columns.")
print("Columns remaining:", df.columns.tolist())

# === Display Total Records ===
print("Total rows in dataset:", len(df))

# === Perform Random Sampling (5% of total data) ===
sample_df = df.sample(frac=0.05, random_state=42)  # use n= for fixed-size sample if preferred

# === Save Sample to New CSV ===
output_path = r"C:\Users\aasth\Downloads\Traffic_Sample.csv"
sample_df.to_csv(output_path, index=False)

print("\n✅ Random sample created successfully.")
print("Sample shape:", sample_df.shape)
print("Saved to:", output_path)

# === Preview of Sample Data ===
sample_df.head()

