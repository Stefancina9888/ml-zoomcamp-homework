"""ML Zoomcamp 2026, Homework 5, Question 3."""

import pickle
from pathlib import Path

from model import normalize_record

lead = {
    "lead_source": "paid_ads",
    "industry": "technology",
    "employment_status": "employed",
    "location": "north_america",
    "number_of_courses_viewed": 2,
    "annual_income": 79276.0,
    "interaction_count": 4,
    "lead_score": 0.41,
}

# Load the model trained and supplied by the course.
model_file = Path(__file__).with_name("pipeline.bin")
with model_file.open("rb") as f:
    pipeline = pickle.load(f)

# Use the same preprocessing as the API.
record = normalize_record(lead)
probability = pipeline.predict_proba([record])[0, 1]
print(f"Q3 conversion probability: {probability:.3f}")
