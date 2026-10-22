# ML Zoomcamp 2026 - Homework 6

Homework for Module 6: Decision Trees and Ensemble Learning.

## Files

- `06-homework.ipynb` - solutions with outputs and plots
- `car_fuel_efficiency_2026.csv` - dataset used in the notebook
- `requirements.txt` - Python dependencies

## Requirements

Python 3.11.15, NumPy 2.3.3, pandas 2.3.2, scikit-learn 1.7.2, XGBoost 3.2.0, Matplotlib and JupyterLab.

The numerical library versions match the [course data release](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/main/cohorts/2026/data/README.md). Newer scikit-learn versions can give different random forest results.

## Running the notebook

From this folder, create an environment and install the dependencies:

```powershell
uv venv --python 3.11.15 .venv
uv pip install --python .venv/Scripts/python.exe -r requirements.txt
```

Start JupyterLab using this environment:

```powershell
.\.venv\Scripts\python.exe -m jupyterlab
```

Open `06-homework.ipynb`, select the Python kernel from this `.venv`, and run all cells from top to bottom. Keep the CSV in the same folder as the notebook.

Answers are written in the comments below each question.

## Homework answers

| Question | Answer |
|---|---|
| Q1 - Original splitting feature | `model_year` |
| Q2 - Validation RMSE | `1.837` |
| Q3 - Number of estimators | `100` |
| Q4 - Best max depth | `10` |
| Q5 - Most important feature among the four options | `vehicle_weight` |
| Q6 - XGBoost eta | `0.1` |

For Q4, max depth 10 has a mean validation RMSE of about 1.755405. For Q6, after 100 rounds, eta 0.3 gives RMSE 1.826458 and eta 0.1 gives RMSE 1.724810.

The data is split into 6,000 training, 2,000 validation and 2,000 test rows. All parameter comparisons use the validation data.