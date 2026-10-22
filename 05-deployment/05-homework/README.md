# ML Zoomcamp 2026 — Homework 5

## Deploying Machine Learning Models

This homework focuses on loading a pretrained machine learning model and serving predictions using FastAPI and Docker.

The project uses Python 3.11.15, scikit-learn 1.7.2, and uv for dependency management.

## Homework Answers

| Question | Answer |
|---|---|
| Q1 — uv version | 0.13.4 (environment check) |
| Q2 — scikit-learn version | 1.7.2 |
| Q3 — Conversion probability | 0.533 |
| Q4 — FastAPI prediction | 0.770 |
| Q5 — Python base image | `python:3.11.15-slim-bookworm` |
| Q6 — Docker prediction | 0.770 |

## Running the Project

Install the project dependencies:

```bash
uv sync --locked
```

Run the direct model prediction:

```bash
uv run python q3_solution.py
```

Start the FastAPI server:

```bash
uv run uvicorn predict:app --host 0.0.0.0 --port 9696
```

Test the API from another terminal:

```bash
uv run python q6_test.py
```

Stop the API before running Docker.

Build and run the Docker container:

```bash
docker build -t zoomcamp-model:2026-hw5 .
docker run --rm -p 9696:9696 zoomcamp-model:2026-hw5
```

Run the same API test from another terminal.

## Files

- `05-homework.ipynb` — notebook with calculations and explanations.
- `q3_solution.py` — direct prediction using the pretrained model.
- `homework_answers.md` — detailed answers and commands.
- `predict.py` — FastAPI application.
- `model.py` — feature preparation.
- `pipeline.bin` — pretrained model.
- `Dockerfile` — container configuration.
- `pyproject.toml` and `uv.lock` — Python dependencies.

The original course model is used without retraining.

## References

[DataTalksClub ML Zoomcamp 2026 — Homework 5](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/main/cohorts/2026/homework/05-deployment/homework.md)