SOUL Match Prototype

A simple, extensible service to compute in‑person compatibility scores based on user Soulprint profiles. Converts each user’s MBTI, Enneagram, attachment style, and love‑language data into a weighted average score via a FastAPI endpoint.

Features

Mock data generation*: Build rich JSON profiles and synthetic match pairs.*

Feature builder*: Encodes profiles and applies dealbreaker rules.*

Model training*: Train rich or logistic regression models on synthesized data.*

API*: Expose a /similarity endpoint to compute real‑time compatibility.*

Prerequisites

Python 3.10+

Git

venv* or Conda for isolation*

Setup

Clone the repo

git clone https://github.com/yourusername/soul-match-prototype.git
cd soul-match-prototype

Create & activate a virtual environment

python -m venv venv
source venv/bin/activate    # mac/linux
# or Windows: .\venv\Scripts\activate

Install dependencies

pip install -r requirements.txt

Generating Mock Profiles

python build_mock_rich_profiles.py

Creates mock_profiles.json with 200 rich Soulprint profiles.

Generating Training Pairs

python generate_pairs_rich.py

Produces data/rich_pairs.joblib (feature vectors & labels).

Training the Model

Rich model (GBDT) + Calibration

python train_rich.py              # trains GBDT -> data/rich_match_model.joblib
python train_logistic.py          # trains logistic -> data/logistic_model.joblib
python calibrate_model.py         # calibrates logistic -> data/calibrated_model.joblib

Running the API

python -m uvicorn match_api:app --reload --port 8000

Visit http://127.0.0.1:8000/docs for Swagger UI.

Testing

Use the /similarity endpoint with sample JSON payloads. Example:

curl -X POST http://127.0.0.1:8000/similarity \
     -H "Content-Type: application/json" \
     --data @test_payload.json

File Structure

├── build_mock_rich_profiles.py  # generates mock_profiles.json
├── generate_pairs_rich.py       # builds feature pairs
├── feature_builder.py           # encodes & computes feature vectors
├── train_rich.py                # trains GBDT model
├── train_logistic.py            # trains logistic model
├── calibrate_model.py           # calibrates logistic model
├── match_api.py                 # FastAPI service
├── data/                        # output: rich_pairs.joblib
├── mock_profiles.json           # generated mock profiles
├── requirements.txt
├── README.md
└── .gitignore

Cleanup

You can safely remove old artifacts:

pairs_labels.joblib**, match_model.joblib (from early prototypes)

test.py* (deprecated)*

Next Steps

Containerize with Docker

Add CI tests (pytest)

Integrate with front‑end or React Native demo

Fine‑tune feature weights or incorporate real data

