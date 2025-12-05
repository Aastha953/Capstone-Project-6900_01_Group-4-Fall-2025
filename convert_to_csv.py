import pandas as pd
from pathlib import Path
import os

# Optional: check your current working directory
print("Current working directory:", os.getcwd())

# Update these paths if your files are elsewhere
text_files = [
    r"C:\Users\aasth\Downloads\Facility Mobility Speeds.txt",
    r"C:\Users\aasth\Downloads\All Recorded PABT Passenger.txt",
    r"C:\Users\aasth\Downloads\All Recorded PABT Bus.txt"
]

for file in text_files:
    path = Path(file)
    output_csv = path.with_suffix('.csv')

    if not path.exists():
        print(f"❌ File not found: {file}")
        continue

    df = pd.read_csv(path, sep="\t")
    df.to_csv(output_csv, index=False)
    print(f"✅ Converted '{file}' → '{output_csv.name}' ({len(df)} rows, {len(df.columns)} columns)")

