# feature_builder.py

import numpy as np
from compatibility_tables import MBTI, ENNEA, ATTCH, get_score

def encode_user(profile: dict):
    s = profile["soulprint"]
    return {
      "mbti":      s["mbti"],
      "ennea":     s["enneagram"][:1],                     # drop the wing
      "attach":    s["attachment_style"].split("-")[0].lower(),
      "gives":     set(s["love_language"]["gives"]),
      "receives":  set(s["love_language"]["receives"]),
      "dealbreakers": set(profile["values_and_ideals"]["non_negotiables"]),
      "soft_flags":   set(profile["values_and_ideals"]["soft_red_flags"]),
    }

def build_pair_features(a_enc: dict, b_enc: dict):
    # 1) Hard rule: any dealbreaker hits soft-flag → no match
    if a_enc["dealbreakers"] & b_enc["soft_flags"] or b_enc["dealbreakers"] & a_enc["soft_flags"]:
        return None, 0

        # 2) Compatibility chart lookups
    if a_enc["mbti"] == b_enc["mbti"]:
        mbti_score = 1.0
    else:
        mbti_score = get_score(MBTI, a_enc["mbti"], b_enc["mbti"])

    # Enneagram: identical = 1.0
    if a_enc["ennea"] == b_enc["ennea"]:
        ennea_score = 1.0
    else:
        ennea_score = get_score(ENNEA, a_enc["ennea"], b_enc["ennea"])

    # Attachment: identical = 1.0
    if a_enc["attach"] == b_enc["attach"]:
        attach_score = 1.0
    else:
        attach_score = get_score(ATTCH, a_enc["attach"], b_enc["attach"])

    # 3) Love‑language overlap
    overlap = len(a_enc["gives"] & b_enc["receives"])
    love_score = overlap / max(len(a_enc["gives"]), 1)

    # 4) Pack into a feature vector
    features = np.array([mbti_score, ennea_score, attach_score, love_score], dtype=np.float32)
    return features, 1
