# SOUL Match Prototype

A lightweight service to calculate in‑person compatibility scores from “Soulprint” JSON profiles. The system:

- **Encodes** user attributes (MBTI, Enneagram, attachment style, love languages) into feature vectors  
- **Applies** dealbreaker rules (hard disqualifications)  
- **Computes** a weighted average compatibility score via a FastAPI endpoint

---

## Features

- **Mock Data Generation**: `build_mock_rich_profiles.py` creates sample Soulprint JSON files  
- **Pair Generation**: `generate_pairs_rich.py` turns profiles into feature‑label datasets  
- **Model Training**:  
  - `train_rich.py` (Gradient‑Boosting)  
  - `train_logistic.py` (Logistic Regression)  
  - `calibrate_model.py` (Probability calibration)  
- **API**: `match_api.py` exposes POST `/similarity` to score two profiles  

---

## Prerequisites

- Python 3.10 or newer  
- Git  
- Virtual environment (`venv`) or Conda  

---

## Setup

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/soul-match-prototype.git
   cd soul-match-prototype
