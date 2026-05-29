# This runs all 4 steps automatically one by one

import subprocess
import sys

steps = [
    ("step1_collect_data.py",  "STEP 1: Data Collection"),
    ("step2_clean_data.py",    "STEP 2: Data Cleaning"),
    ("step3_analysis.py",      "STEP 3: Data Analysis"),
    ("step4_dashboard.py",     "STEP 4: Dashboard"),
]

print("RUNNING FULL E-COMMERCE ANALYSIS PIPELINE")
print("=" * 55)

for filename, label in steps:
    print(f"\n{'=' * 55}")
    print(f" {label}")
    print(f"{'=' * 55}")

    result = subprocess.run([sys.executable, filename])  # Run each file

    if result.returncode != 0:
        print(f"\n ERROR in {filename}. Please fix it and try again.")
        break
    else:
        print(f"{label} done!")

print("\n" + "=" * 55)
print("ALL STEPS COMPLETE! Check your project folder.")
print("=" * 55)
