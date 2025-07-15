# build_mock_rich_profiles.py

import json, random
from compatibility_tables import MBTI, ENNEA, ATTCH

# Helpers: pull valid keys from your tables
MBTI_TYPES    = list(MBTI.keys())
ENNEA_TYPES   = list(ENNEA.keys())
ATTACH_TYPES  = list(ATTCH.keys())
LOVE_GIVES    = ["Acts of service","Quiet presence","Gifts","Quality time","Words of affirmation","Physical touch"]
LOVE_RECEIVES = LOVE_GIVES  # same set

NUM_PROFILES = 200
RNG = random.Random(42)

profiles = []
for _ in range(NUM_PROFILES):
    profile = {
      "soulprint": {
        "mbti":               RNG.choice(MBTI_TYPES),
        "enneagram":          RNG.choice(ENNEA_TYPES) + "w" + str(RNG.randint(1,9)),
        "attachment_style":   RNG.choice(ATTACH_TYPES),
        "love_language": {
          "gives":    RNG.sample(LOVE_GIVES,    k=2),
          "receives": RNG.sample(LOVE_RECEIVES, k=2),
        },
      },
      "values_and_ideals": {
        "non_negotiables": RNG.sample(["Passive partners","Emotional unavailability","Lack of follow-through"], k=1),
        "soft_red_flags":  RNG.sample(["Indifference","Emotional vagueness","Surface-level only"], k=1),
      }
    }
    profiles.append(profile)

with open("mock_profiles.json", "w") as f:
    json.dump(profiles, f, indent=2)

print(f"Wrote {NUM_PROFILES} rich mock profiles to mock_profiles.json")
