# NCAA Cinderella Team Detection (2013–2025)

This project analyzes NCAA Division I Men's Basketball performance data from 2013 to 2025 to identify "Cinderella teams"—low-seeded teams that make unexpectedly deep tournament runs. We combined interactive Tableau dashboards and unsupervised machine learning (Python-based KMeans clustering) to uncover patterns that distinguish these underdog teams from traditional contenders.

## 🏀 What Is a Cinderella Team?

A "Cinderella team" refers to a lower-seeded team (typically Seed ≥ 10) that exceeds expectations in the NCAA March Madness tournament—often making it to the Elite Eight (E8), Final Four (F4), or even winning the championship.

## 📊 Dataset

- **Source**: Kaggle College Basketball Dataset by Andrew Sundberg  
- **Seasons Covered**: 2013–2025  
- **Metrics Used**:
  - Efficiency (ADJOE, ADJDE)
  - Shooting (%EFG, 2P, 3P)
  - Turnover & Rebounding (TORD, ORB, DRB)
  - Tempo, WAB (Wins Above Bubble), BARTHAG (power rating)
  - Tournament Seed & Results

## 🔧 Methodology

### 🧠 Python Clustering (KMeans)
- Standardized 17 statistical features
- Applied **KMeans clustering (k=5)**
- Visualized clusters using:
  - **Radar Charts** (cluster profiles)
  - **PCA Projection** (2D representation)

### 🔍 Cinderella Filter Criteria
- Belongs to Cluster 0 or 4 (underdog profiles)
- Seed ≥ 10
- Postseason result in [E8, F4, CHMP]

### 📈 Tableau Visualizations
- Box Plot – BARTHAG by Seed Tier
- Scatter Plot – ADJOE vs. ADJDE
- Heatmap – Seed vs. Postseason Round
- Parallel Coordinates – Cinderella vs. Champion traits
- Team-Level Stats Table (interactive filterable)

## 💡 Key Findings

| Metric         | Why It Matters                                  |
|----------------|-------------------------------------------------|
| **BARTHAG > 0.83** | Indicates statistical parity with top teams |
| **WAB > 2.5**       | Cinderella teams consistently outperform seed expectations |
| **TORD > 20%**      | Strong defensive disruption is a core trait |
| **DRB > 70%**       | Dominance on defensive glass is critical     |

### 🏆 Identified Cinderella Teams (Examples)
| Team           | Year | Seed | Postseason | Cluster |
|----------------|------|------|------------|---------|
| Loyola Chicago | 2018 | 11   | Final Four | 4       |
| UCLA           | 2021 | 11   | Final Four | 4       |
| Dayton         | 2014 | 11   | Elite Eight | 0      |

These teams share defensively strong, tactically efficient, and statistically underrated profiles—proving Cinderella runs are **not random**.

## 📁 Project Structure

├── FinalProject.py # Python clustering & visualization
├── Data Visualization Final Report.docx # Written summary & findings
├── Cinderella_Team_Final.pptx # Project presentation slides
├── DAV - College Basketball analysis viz.twbx # Tableau dashboard (interactive)
├── README.md

markdown
Copy
Edit

## 🛠 How to Run (Python Part)

1. Place the dataset (`cbb.csv`) in the working directory.
2. Install required Python libraries:
   ```bash
   pip install pandas scikit-learn matplotlib seaborn
Run the Python script:

bash
Copy
Edit
python FinalProject.py
The script will:

Perform KMeans clustering

Display radar charts for each cluster

Generate PCA 2D plot

Print detailed info for detected Cinderella teams

👥 Contributors
Keyu Chen – Python modeling, clustering, Cinderella identification

Deniz U Zeran – Tableau analysis & dashboard creation

📌 Conclusion
This dual-method (visual + statistical) framework demonstrates that Cinderella teams share consistent, data-backed characteristics. The approach not only explains past upsets but also provides a practical tool for predicting future underdog success.


