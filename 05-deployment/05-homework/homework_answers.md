# Homework 5: Deploying Machine Learning Models

[ML Zoomcamp 2026 — official assignment](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/main/cohorts/2026/homework/05-deployment/homework.md)

The goal is to load an existing lead-scoring model, serve it through FastAPI, and test the same prediction in Docker. The course provides `pipeline.bin`, the API implementation, and the Dockerfile. The model is **not retrained** in this homework.

## Environment

- Python: `3.11.15`
- Local `uv` at the time of testing: `0.13.4`
- scikit-learn: `1.7.2`
- FastAPI and Uvicorn: versions pinned by the provided `uv.lock`
- Docker Desktop with the WSL 2 backend

From the `05-deployment/05-homework` directory, install the locked dependencies and check the model:

```powershell
uv sync --locked
uv run python smoke_test.py
Get-FileHash .\pipeline.bin -Algorithm SHA256
```

The model's expected SHA-256 is `1646bbdcd38d4f044da6b630c5b332c93a314245a8c21929011c42de51f629f1`.

## Answers

| Question | Answer | How it was checked |
| --- | --- | --- |
| Q1 — `uv` version | `0.13.4` (setup check only) | `uv --version` on this PC |
| Q2 — scikit-learn | **`1.7.2`** | `pyproject.toml` and `uv.lock` |
| Q3 — direct prediction | **`0.533`** | Load `pipeline.bin` with `pickle`; call `predict_proba` |
| Q4 — FastAPI prediction | **`0.770`** | Send a POST request to the local `/predict` endpoint |
| Q5 — Docker Python image | **`python:3.11.15-slim-bookworm`** | First `FROM` instruction in the provided `Dockerfile` |
| Q6 — Docker prediction | **`0.770`** | Repeat the Q4 request against the container |

Q1 is a local setup check and is not a graded answer. The unrounded model outputs recorded in the earlier verified run were `0.5329944186432507` (Q3) and `0.769799` (Q4 and Q6).

## Q3: Predict directly with Python

`q3_solution.py` reads `pipeline.bin` using `pickle`, normalizes the question's input record with the course's `normalize_record` function, and asks the fitted pipeline for the positive-class probability.

```powershell
uv run python q3_solution.py
```

Expected output:

```text
Q3 conversion probability: 0.533
```

Only load pickle files from trusted sources, since loading a pickle can execute code.

## Q4: Run the API locally

Start the provided FastAPI application in **terminal 1**:

```powershell
uv run uvicorn predict:app --host 0.0.0.0 --port 9696
```

In **terminal 2**, from the same directory, run the supplied client (`q6_test.py` uses the exact Q4 input):

```powershell
uv run python q6_test.py
Invoke-RestMethod http://localhost:9696/health
```

Expected prediction: `conversion_probability = 0.769799`, `conversion = True`.

Stop the local server with **Ctrl+C** before starting Docker, since they cannot both use port 9696 on the host.

## Q5–Q6: Run the model in Docker

The reference Dockerfile uses `python:3.11.15-slim-bookworm` (with a pinned image digest). Build and start the image in **terminal 1**:

```powershell
docker build -t zoomcamp-model:2026-hw5 .
docker run --rm -p 9696:9696 zoomcamp-model:2026-hw5
```

In **terminal 2**, run the same client and health check:

```powershell
uv run python q6_test.py
Invoke-RestMethod http://localhost:9696/health
```

The Docker result should match Q4: `0.770` when rounded to three decimals. Stop the container with **Ctrl+C**.

## What I learned

- `pickle` lets a Python program load an already fitted ML pipeline.
- `uv` and `uv.lock` make the project's Python dependencies reproducible.
- FastAPI provides an HTTP interface, so other programs can request predictions.
- A Docker *image* packages the application and its environment; a *container* runs that image.
- Testing the same example locally and in Docker helps confirm that the deployment behaves consistently.

These steps are for local deployment and testing, not a publicly hosted production service.
