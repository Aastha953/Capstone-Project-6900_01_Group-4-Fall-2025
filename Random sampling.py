import pandas as pd

file_path = r"C:\Users\aasth\Downloads\All Recorded Traffic.csv"
output_path = r"C:\Users\aasth\Downloads\All_Recorded_Traffic_20k_random.csv"

# Load full file (only if your system can handle it)
df = pd.read_csv(file_path)

# Randomly sample 20,000 rows
df_sample = df.sample(n=20000, random_state=42)

# Save reduced sample
df_sample.to_csv(output_path, index=False)

print(f"✅ Random 20,000-row sample saved to: {output_path}")
