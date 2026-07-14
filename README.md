# Healthcare BI Dashboard

An interactive, premium Healthcare Business Intelligence dashboard built with vanilla HTML, CSS, and JavaScript. Visualizes 50,000+ patient records across 4 analytical pages.

## 🔗 Live Dashboard

👉 **[View Live Dashboard](https://amarkayamkulam123-rgh.github.io/Healthcare_bi/dashboard/)**

## 📊 Dashboard Pages

| Page | Description |
|------|-------------|
| **Executive Overview** | KPI cards (revenue, patients, hospitals), revenue trends, condition distribution, monthly admissions |
| **Patient Demographics** | Age groups, gender splits, blood types, insurance providers |
| **Clinical Analysis** | Medical conditions, admission types, test results, medications, length of stay, heatmap |
| **Billing & Revenue** | Revenue trends, billing by condition/insurance/age, top hospitals, billing distribution |

## 🛠️ Tech Stack

- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Charts**: Chart.js 4.x
- **Design**: Custom dark premium theme (glassmorphism, micro-animations)
- **Data Processing**: Python (Pandas, NumPy)
- **Hosting**: GitHub Pages

## 📁 Project Structure

```
Healthcare_bi/
├── dashboard/                  # Web dashboard (GitHub Pages)
│   ├── index.html              # Main HTML
│   ├── style.css               # Premium dark theme
│   ├── dashboard.js            # Chart.js engine
│   ├── dashboard_data.json     # Preprocessed aggregated data
│   └── preprocess_data.py      # Data aggregation script
├── healthcare_data.csv         # Cleaned dataset (50K records)
├── healthcare_dataset.csv      # Original raw dataset
├── clean_healthcare_data.py    # Data cleaning pipeline
├── cleaning_report.txt         # Cleaning results log
├── healthcare.pbix             # Power BI file
├── Healthcare_Premium_Theme.json  # Power BI theme
└── PowerBI_Dashboard_Guide.md  # Visual-by-visual guide
```

## 🚀 Local Development

1. Clone the repository
2. Run the data preprocessor (requires Python 3 + pandas):
   ```bash
   cd dashboard
   python preprocess_data.py
   ```
3. Serve locally:
   ```bash
   python -m http.server 8000 --directory dashboard
   ```
4. Open `http://localhost:8000`

## 📈 Data Pipeline

1. **Raw Data** → `healthcare_dataset.csv` (original)
2. **Cleaning** → `clean_healthcare_data.py` → `healthcare_data.csv`
3. **Aggregation** → `preprocess_data.py` → `dashboard_data.json` (6.5 KB)
4. **Visualization** → Interactive web dashboard

## 🎨 Design

The dashboard uses a premium dark theme inspired by the Healthcare Premium Theme with:
- Dark navy backgrounds (`#0B1929`, `#0F2237`)
- Teal accent (`#00BFA5`) with vibrant chart palette
- Glassmorphism headers with backdrop blur
- Animated KPI counters
- Responsive layout (desktop → tablet → mobile)

## 📄 License

This project is for educational and portfolio purposes.
