# 🎓 Student Portfolio — AI & Python Projects

> A responsive, animated personal portfolio website built with vanilla **HTML, CSS & JavaScript** — showcasing hands-on AI/ML projects completed during a structured workshop.

![Portfolio Preview](https://img.shields.io/badge/Status-Live-brightgreen?style=flat-square)
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)

---

## 👤 About

**B.Sc (Computer Science) Student** — 2nd Year, 4th Semester  
📍 Haldia Institute of Management, Haldia, India  
🧠 Mentored by **SK Sahil** (AI Developer & Tutor) — [@code_scholar_eu](https://www.instagram.com/code_scholar_eu/)

Passionate about Python, data analysis, and Machine Learning. This portfolio showcases projects built during a hands-on AI/ML workshop, using Google Colab and pushed to GitHub.

---

## 🌐 Live Demo

> Open `index.html` in any modern browser — no build tools or dependencies required.

---

## ✨ Features

- **Animated particle canvas background** with WebGL-style connected dots
- **Floating gradient blobs** with smooth CSS keyframe animations
- **Typing effect** cycling through skills and focus areas
- **Scroll-reveal animations** using IntersectionObserver API
- **Sticky progress bar** showing read completion
- **Responsive layout** with mobile drawer navigation
- **Single-file architecture** — no frameworks, no bundlers
- **Quick personalization** via URL query params (`?name=YourName&github=https://...`)

---

## 🗂️ Project Structure

```
portfolio/
└── index.html       # Complete single-file portfolio (HTML + CSS + JS)
```

---

## 🛠️ Tech Stack

| Layer       | Technology                        |
|-------------|-----------------------------------|
| Markup      | HTML5 (semantic)                  |
| Styling     | CSS3 (custom properties, grid, flex, animations) |
| Scripting   | Vanilla JavaScript (ES6+)         |
| Icons       | Font Awesome 6.5 (CDN)            |
| Canvas      | HTML5 Canvas API (particle system)|

---

## 🧪 AI/ML Projects Showcased

### 📊 Project 1 — EDA Dashboard (Titanic Dataset)
A beginner-friendly Exploratory Data Analysis project using a real-world dataset.

- Loaded and explored dataset columns using **Pandas**
- Handled missing values using mean and mode imputation
- Created visualizations: survival count, gender vs survival, age distribution
- Derived and presented key insights clearly

**Tools:** `Python` · `Pandas` · `Matplotlib` · `Google Colab`

---

### 🏠 Project 2 — House Price Prediction
First supervised Machine Learning model using Linear Regression.

- Performed **train-test split** to evaluate on unseen data
- Trained model using **scikit-learn** LinearRegression
- Evaluated performance with **RMSE** and **R² score**
- Visualized actual vs predicted values

**Tools:** `Python` · `scikit-learn` · `Pandas` · `Matplotlib` · `Google Colab`

---

## 🧰 Skills Highlighted

- **Python Foundations** — variables, loops, functions, data structures
- **Data Handling** — Pandas DataFrames, cleaning, filtering, grouping
- **Visualization** — bar charts, histograms, scatter plots, residual analysis
- **ML Concepts** — supervised learning, model evaluation, feature engineering

---

## 🚀 Getting Started

### View Locally
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
open index.html    # macOS
# or just double-click index.html on Windows/Linux
```

### Personalize via URL
```
index.html?name=Your%20Name&github=https://github.com/your-username
```

### Personalize in Code
Open `index.html` and update the `LINKS` object near the bottom of the `<script>` block:

```js
const LINKS = {
  githubProfile:    "https://github.com/your-username",
  linkedin:         "https://linkedin.com/in/your-profile",
  project1Repo:     "https://github.com/your-username/project-1",
  project2Repo:     "https://github.com/your-username/project-2",
  project1Notebook: "https://colab.research.google.com/...",
  project2Notebook: "https://colab.research.google.com/...",
  email:            "your@email.com"
};
```

Also update your name in the `<h1>` tag and institution details in the `<header>`.

---

## 📱 Responsive Design

| Breakpoint | Layout                     |
|------------|----------------------------|
| ≥ 920px    | Full multi-column grid     |
| < 920px    | Single-column + hamburger menu |

---

## 📬 Contact

| Platform  | Link |
|-----------|------|
| 📸 Instagram | [@code_scholar_eu](https://www.instagram.com/code_scholar_eu/) |
| 💻 GitHub | [github.com/your-username](https://github.com/your-username) |
| 💼 LinkedIn | [linkedin.com/in/your-profile](https://linkedin.com/in/your-profile) |
| 📧 Email | student@email.com |

---

## 🙏 Acknowledgements

Special thanks to **SK Sahil** for mentoring through ML basics, GitHub workflow, and portfolio building as part of the AI/ML workshop program.

---

## 📄 License

This project is open source and free to use for educational and portfolio purposes.

---

*Built with ❤️ using HTML, CSS & JS — Ready for GitHub Pages*
