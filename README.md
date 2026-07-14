# Healthcare BI Dashboard

An interactive, premium Healthcare Business Intelligence dashboard visualizing 50,000+ patient records across 4 analytical pages. 
This project features a fully functional **Power BI** dashboard embedded directly into a GitHub Pages site for seamless web access.

## 🔗 Live Dashboard

👉 **[View Live Dashboard](https://amarkayamkulam123-rgh.github.io/Healthcare_analysis/)**

## 📊 Dashboard Pages

| Page | Description |
|------|-------------|
| **Executive Overview** | KPI cards (revenue, patients, hospitals), revenue trends, condition distribution, monthly admissions |
| **Patient Demographics** | Age groups, gender splits, blood types, insurance providers |
| **Clinical Analysis** | Medical conditions, admission types, test results, medications, length of stay, heatmap |
| **Billing & Revenue** | Revenue trends, billing by condition/insurance/age, top hospitals, billing distribution |

## 🛠️ Tech Stack

- **Data Processing**: Python (Pandas, NumPy)
- **Visualization**: Microsoft Power BI (`.pbix`)
- **Hosting**: GitHub Pages (via Power BI embedded `<iframe>`)

## 📁 Project Structure

```
Healthcare_analysis/
├── docs/                       # Web deployment folder (GitHub Pages)
│   └── index.html              # Wrapper HTML embedding the Power BI dashboard
├── healthcare_dataset.csv      # Original raw dataset
├── clean_healthcare_data.py    # Python data cleaning pipeline
├── healthcare_data.csv         # Cleaned dataset used in Power BI (50K records)
├── cleaning_report.txt         # Log of cleaning actions and results
├── healthcare.pbix             # Core Power BI dashboard file
├── Healthcare_Premium_Theme.json  # Custom Power BI dark theme config
└── PowerBI_Dashboard_Guide.md  # Detailed visual-by-visual construction guide
```

## 🚀 How It Was Built

1. **Data Cleaning**: The raw `healthcare_dataset.csv` was processed using `clean_healthcare_data.py` to fix casing, remove duplicates, handle missing values, and calculate new fields (like Length of Stay).
2. **Dashboard Creation**: The cleaned `healthcare_data.csv` was loaded into Power BI (`healthcare.pbix`), utilizing a custom premium dark theme (`Healthcare_Premium_Theme.json`).
3. **Web Deployment**: The final Power BI dashboard was published to the web, and the public embed URL was placed inside `docs/index.html` to be hosted seamlessly via GitHub Pages.

## 📄 License

This project is for educational and portfolio purposes.
