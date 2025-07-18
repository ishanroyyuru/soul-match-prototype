# scripts/build_mbti_matrix.py

import pandas as pd

MBTI_TYPES = [
    "ENFJ","ENFP","ENTJ","ENTP","ESFJ","ESFP","ESTJ","ESTP",
    "INFJ","INFP","INTJ","INTP","ISFJ","ISFP","ISTJ","ISTP"
]

# compatibility percentages from your screenshot, row‑by‑row
data = [
    [86,91,42,73,64,80,22,41,74,73,16,35,30,40,18,9],
    [91,97,37,85,42,93,27,76,51,73,13,36,11,49,4,14],
    [42,37,91,81,53,51,87,74,25,13,46,47,29,6,66,41],
    [73,85,81,94,32,87,70,92,11,35,22,51,5,14,11,35],
    [64,42,53,32,94,40,77,37,74,17,32,5,79,57,71,19],
    [80,93,51,87,40,70,39,75,43,58,22,39,12,58,8,26],
    [22,27,87,70,77,39,96,78,14,3,33,22,48,22,79,55],
    [41,76,74,92,37,75,78,95,5,24,17,39,12,43,20,62],
    [74,51,25,11,74,43,14,5,95,85,65,50,85,58,53,23],
    [73,73,13,35,17,58,3,24,85,97,70,84,46,78,21,49],
    [16,13,46,22,32,22,33,17,65,70,86,89,79,45,85,78],
    [35,36,47,51,5,39,22,39,50,84,89,96,38,43,51,81],
    [30,11,29,5,79,12,48,12,85,46,79,38,95,76,93,62],
    [40,49,6,14,57,58,22,43,58,78,45,43,76,97,47,76],
    [18,4,66,11,71,8,79,20,53,21,85,51,93,47,96,78],
    [9,14,41,35,19,26,55,62,23,49,78,81,62,76,78,96],
]

# convert to 0–1 floats
df = pd.DataFrame(data, index=MBTI_TYPES, columns=MBTI_TYPES) / 100.0

# ensure your data/ folder exists
df.to_csv("data/mbti_matrix.csv")
print("mbti_matrix.csv written with shape", df.shape)
