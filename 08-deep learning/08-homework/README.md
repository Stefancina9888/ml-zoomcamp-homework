# ML Zoomcamp 2026 - Homework 8

Homework for Module 8 on neural networks and deep learning. The model classifies curly and straight hair with PyTorch.

## Files

- `08-homework.ipynb` - solutions with outputs for each question
- `requirements-cpu.txt` - course CPU dependencies and JupyterLab

## Requirements

Python 3.11.15, PyTorch 2.9.0+cpu, torchvision 0.24.0+cpu, NumPy 2.3.3 and Pillow 11.3.0. From this folder, create the environment and install the dependencies.

```powershell
uv venv --python 3.11.15 .venv
uv pip install --python .venv/Scripts/python.exe -r requirements-cpu.txt
```

## Running the notebook

```powershell
.\.venv\Scripts\python.exe -m jupyterlab
```

Open `08-homework.ipynb`, select the Python kernel from this `.venv` and run all cells from top to bottom. 


## Homework answers

| Question | Answer |
|---|---|
| Q1 - Loss | `nn.BCEWithLogitsLoss()` |
| Q2 - Number of parameters | `20073473` |
| Q3 - Median baseline training accuracy | `0.81` |
| Q4 - Population standard deviation of baseline training loss | `0.139` |
| Q5 - Mean augmented evaluation loss | `0.575` |
| Q6 - Mean augmented evaluation accuracy, epochs 6-10 | `0.72` |

[Homework 8 instructions](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/main/cohorts/2026/homework/08-deep-learning/homework.md) · [Course reference script](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/main/cohorts/2026/homework/08-deep-learning/reference_train.py)
