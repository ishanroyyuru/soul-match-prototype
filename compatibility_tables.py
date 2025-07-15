import pandas as pd
from pathlib import Path

DATA = Path(__file__).parent / "data"
MBTI  = pd.read_csv(DATA/"mbti_matrix.csv",  index_col=0).to_dict()
ENNEA = pd.read_csv(DATA/"ennea_matrix.csv",  index_col=0).to_dict()
ATTCH = pd.read_csv(DATA/"attachment_matrix.csv", index_col=0).to_dict()

def get_score(table, a, b):
    return table.get(a, {}).get(b, 0.5)   # default neutral
