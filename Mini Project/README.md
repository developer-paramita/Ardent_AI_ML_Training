# 🧮 Python Projects — Statistical Calculator & House Price Prediction

> Two beginner-to-intermediate Python projects covering core programming concepts and applied Machine Learning.

---

## 📁 Project Structure

```
project2.py
├── Part 1 — Statistical Calculator    (CLI tool, type casting, math & stats)
└── Part 2 — House Price Prediction    (ML model, California Housing dataset)
```

---

## Part 1 — Statistical Calculator

A fully interactive command-line calculator built with pure Python. Demonstrates **user input handling**, **type casting**, and a range of **arithmetic & statistical operations**.

### ✨ Features

| Feature | Description |
|---|---|
| **Type Casting** | Auto-detects `int`, `float`, or `str` from raw input |
| **Arithmetic** | Addition, Subtraction, Multiplication, Division, Modulo, Floor Div, Power |
| **Percentage** | X% of Y · What % is X of Y · Percentage change |
| **Statistics** | Mean, Median, Mode (multi-mode), Average, Sum |
| **Expression Evaluator** | Evaluate custom math expressions like `(3+4)*2 - 10/5` |
| **Dataset Mode** | Enter multiple numbers, get full statistical breakdown with visual % bar |

### 🖥️ How to Run

```bash
python project2.py
```

### 📋 Menu Options

```
[1] Arithmetic         (A+B, A-B, A*B, A/B, A%B)
[2] Percentage         (X% of Y, change, ratio)
[3] Statistics         (mean, median, mode, avg)
[4] Expression         (custom math expression)
[0] Exit
```

### 🔢 Sample Output — Statistics

```
Dataset : [10, 20, 20, 30, 40]
Sorted  : [10, 20, 20, 30, 40]
Count   : 5

┌──────────────────────────────────────┐
│  Sum     =  120                      │
│  Average =  24                       │
│  Mean    =  24                       │
│  Median  =  20                       │
│  Mode    =  [20]                     │
└──────────────────────────────────────┘

Percentage of total (sum = 120):
        10  →    8.33%  ████
        20  →   16.67%  ████████
        20  →   16.67%  ████████
        30  →   25.00%  ████████████
        40  →   33.33%  ████████████████
```

### 📦 Dependencies

```bash
# Standard library only — no installation needed
python >= 3.8
```

---

## Part 2 — House Price Prediction (ML)

A supervised Machine Learning project that predicts California house prices using **Linear Regression**. Covers the complete ML pipeline from data loading to model evaluation and saving results.

### ✨ Features

- Loads the built-in **California Housing** dataset (20,640 samples, 8 features)
- Full **train/test split** (80/20)
- **Linear Regression** model training and prediction
- Model evaluation with **RMSE** and **R² Score**
- **Log transformation** for improved accuracy
- Visualization: Actual vs Predicted · Residual Plot · Feature Coefficients
- Exports predictions to **CSV**

### 📊 Dataset — California Housing

| Feature | Description |
|---|---|
| `MedInc` | Median income in block group |
| `HouseAge` | Median house age |
| `AveRooms` | Average number of rooms |
| `AveBedrms` | Average number of bedrooms |
| `Population` | Block group population |
| `AveOccup` | Average house occupancy |
| `Latitude` | Block group latitude |
| `Longitude` | Block group longitude |
| `Price` *(target)* | Median house value (in $100,000s) |

### 🔄 ML Pipeline — Step by Step

```
1. Import Libraries
2. Load Dataset          → fetch_california_housing()
3. Explore Data          → shape, info, describe
4. Check Missing Values  → isnull().sum()
5. Feature / Target Split → X (8 features), y (Price)
6. Train-Test Split      → 80% train / 20% test
7. Train Model           → LinearRegression().fit()
8. Predict               → model.predict(X_test)
9. Evaluate              → RMSE + R² Score
10. Visualize            → Scatter + Residual plots
11. Feature Importance   → model.coef_ coefficients
12. Log Transform        → np.log1p(y) for improvement
13. Save Results         → house_price_prediction.csv
```

### 📈 Model Results

| Metric | Baseline | After Log Transform |
|---|---|---|
| **RMSE** | ~0.74 | Lower |
| **R² Score** | ~0.60 | Higher |

> *Results may vary slightly by environment. Log transformation on the target variable generally improves R² for skewed price distributions.*

### 📦 Dependencies

```bash
pip install numpy pandas matplotlib scikit-learn
```

Or install all at once:

```bash
pip install -r requirements.txt
```

**`requirements.txt`**
```
numpy
pandas
matplotlib
scikit-learn
```

### 🖥️ How to Run

**Option A — As a Python script:**
```bash
python project2.py
```

**Option B — As a Jupyter Notebook (recommended for Part 2):**
```bash
jupyter notebook project2.ipynb
```

### 📤 Output Files

| File | Description |
|---|---|
| `house_price_prediction.csv` | Actual vs Predicted prices for all test samples |

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=flat)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)

---

## 🚀 Getting Started

```bash
# 1. Clone the repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

# 2. Install dependencies (for Part 2)
pip install numpy pandas matplotlib scikit-learn

# 3. Run the project
python project2.py
```

---

## 📚 Concepts Covered

- **Python Fundamentals** — functions, loops, conditionals, input/output
- **Type Casting** — `int()`, `float()`, `str()` with auto-detection
- **Statistics** — mean, median, mode, average, percentage
- **Data Science** — EDA, feature engineering, train-test split
- **Machine Learning** — Linear Regression, RMSE, R² evaluation
- **Data Visualization** — scatter plots, residual plots, coefficient charts
- **Log Transformation** — target variable normalization technique

---

## 👤 Author

**Your Name**
- GitHub: [@developer-paramita](https://github.com/developer-paramita)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
