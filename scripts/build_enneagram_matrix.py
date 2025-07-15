# scripts/build_ennea_matrix.py

import pandas as pd
import pathlib

# The nine Enneagram types, in the same order for rows and columns
ENNEA_TYPES = ["1","2","3","4","5","6","7","8","9"]

# Paste your chart values here as 1.0 / 0.8 / 0.6
# Row 1 = type “1” vs. types 1–9, Row 2 = type “2” vs. 1–9, etc.
data = [
    # 1  2    3    4    5    6    7    8    9
    [1.0, 0.8, 0.6, 0.6, 0.8, 0.6, 0.6, 0.6, 1.0],  # Type 1
    [0.8, 1.0, 0.6, 0.8, 0.6, 1.0, 0.8, 0.8, 0.6],  # Type 2
    [0.6, 0.6, 1.0, 0.8, 0.6, 0.6, 1.0, 0.6, 0.8],  # Type 3
    [0.6, 0.8, 0.8, 1.0, 0.8, 0.8, 0.6, 1.0, 0.6],  # Type 4
    [0.8, 0.6, 0.6, 0.8, 1.0, 0.6, 0.8, 0.6, 0.6],  # Type 5
    [0.6, 1.0, 0.6, 0.8, 0.6, 1.0, 0.8, 0.8, 0.6],  # Type 6
    [0.6, 0.8, 1.0, 0.6, 0.8, 0.8, 1.0, 0.6, 0.8],  # Type 7
    [0.6, 0.8, 0.6, 1.0, 0.6, 0.8, 0.6, 1.0, 0.8],  # Type 8
    [1.0, 0.6, 0.8, 0.6, 0.6, 0.6, 0.8, 0.8, 1.0],  # Type 9
]

# Convert to a DataFrame and save
df = pd.DataFrame(data, index=ENNEA_TYPES, columns=ENNEA_TYPES)
out = pathlib.Path(__file__).parent.parent / "data" / "ennea_matrix.csv"
df.to_csv(out)
print(f"Wrote Enneagram matrix to {out} with shape {df.shape}")
