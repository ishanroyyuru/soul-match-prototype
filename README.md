# SOUL Match Prototype

Baseline personality-based matchmaking engine.

## Quick start

```bash
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt

python generate_mock_data.py   # build demo data
python train.py                # train logistic model
python -m uvicorn match_api:app --reload --port 8000
# Open http://127.0.0.1:8000/docs to test
