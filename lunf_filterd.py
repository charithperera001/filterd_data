import pandas as pd
import os

#  Full path to your subject_id list
cancer_ids = pd.read_csv(r"D:\Users\ASUS\Downloads\Book2.csv")['subject_id'].astype(int).tolist()
print(f"✅ Loaded {len(cancer_ids)} subject IDs.")

# Folder with all the MIMIC-IV CSV files
data_folder = r"H:\medical prognosis system\hosp\filtered"

# Function to filter files
def filter_csv_by_subject_id(filepath, id_column='subject_id', output_dir="filtered"):
    try:
        df = pd.read_csv(filepath)

        if id_column not in df.columns:
            print(f"Skipped: {os.path.basename(filepath)} (no '{id_column}')")
            return

        filtered = df[df[id_column].isin(cancer_ids)]

        os.makedirs(output_dir, exist_ok=True)
        out_file = os.path.join(output_dir, f"filtered_{os.path.basename(filepath)}")
        filtered.to_csv(out_file, index=False)
        print(f" Saved: {out_file} ({len(filtered)} rows)")
    except Exception as e:
        print(f" Error in {filepath}: {e}")

# List of files to process
csv_files = [
        "admissions.csv", "d_labitems.csv", "emar_detail.csv", "emar.csv", "omr.csv",
    "prescriptions.csv", "d_hcpcs.csv", "diagnoses_icd.csv", "hcpcsevents.csv",
    "patients.csv", "procedures_icd.csv", "d_icd_diagnoses.csv", "drgcodes.csv",
    "labevents.csv", "pharmacy.csv", "services.csv", "d_icd_procedures.csv",
    "microbiologyevents.csv", "poe.csv", "transfers.csv"

]

# Loop and process each file
for filename in csv_files:
    filepath = os.path.join(data_folder, filename)
    if os.path.exists(filepath):
        filter_csv_by_subject_id(filepath)
    else:
        print(f" File not found: {filepath}")
