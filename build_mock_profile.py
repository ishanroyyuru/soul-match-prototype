# build_mock_profiles.py

import json
from generate_mock_data import random_user, NUM_USERS

# Generate the same 200 fake users as before
profiles = [random_user() for _ in range(NUM_USERS)]

# Write them out as a JSON array
with open("mock_profiles.json", "w") as f:
    json.dump(profiles, f, indent=2)

print(f"Wrote mock_profiles.json with {len(profiles)} profiles")
