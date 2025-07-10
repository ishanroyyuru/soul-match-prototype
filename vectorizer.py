# vectorizer.py
import numpy as np

LOVE_LANGS = [
    "physical_touch",
    "words_of_affirmation",
    "quality_time",
    "acts_of_service",
    "gifts",
]

HOBBIES = [
    "hiking", "reading", "movies", "gaming", "photography",
    "cooking", "travel", "music", "sports", "art",
]

def one_hot(items, master):
    vec = np.zeros(len(master), dtype=np.float32)
    for item in items:
        if item in master:
            vec[master.index(item)] = 1.0
    return vec

def vectorize(user_json: dict) -> np.ndarray:
    traits = np.array(
        [
            user_json["openness"],
            user_json["conscientiousness"],
            user_json["extroversion"],
            user_json["agreeableness"],
            user_json["neuroticism"],
        ],
        dtype=np.float32,
    )
    love_vec  = one_hot(user_json["love_languages"], LOVE_LANGS)
    hobby_vec = one_hot(user_json["hobbies"], HOBBIES)
    return np.concatenate([traits, love_vec, hobby_vec])

# quick smoke-test
if __name__ == "__main__":
    demo = {
        "openness": 0.8,
        "conscientiousness": 0.6,
        "extroversion": 0.4,
        "agreeableness": 0.9,
        "neuroticism": 0.2,
        "love_languages": ["physical_touch", "words_of_affirmation"],
        "hobbies": ["hiking", "reading", "movies"],
    }
    vec = vectorize(demo)
    print("Vector length:", len(vec))    # expect 20
    print("Vector:", vec)
