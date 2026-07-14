# Power BI Dashboard — Visual-by-Visual Detailed Guide

> For each visual below, I tell you **exactly** which visual to pick, which fields to drag into which wells, and how to format it.

---

## Before You Start — Common Setup

1. **Load Data:** Home → Get Data → Text/CSV → select `healthcare_data.csv` → Load
2. **Create Age Group Column:** Modeling → New Column → paste the Age Group DAX
3. **Create all 10 Measures:** Modeling → New Measure → paste each DAX formula one by one
4. **Rename Pages:** Right-click each page tab at the bottom → Rename

---

# 📄 PAGE 1: Executive Overview

> Right-click page tab → Rename → type `Executive Overview`

---

### Visual 1 — Card: Total Revenue

| Step | Action |
|---|---|
| **Pick visual** | Click on the **Card** icon in the Visualizations pane (looks like a single number box) |
| **Fields well** | Drag `Total Revenue` measure → **Fields** well |
| **Format → Callout value** | Display units: **None** (to show full number) or **Thousands/Millions** |
| **Format → Callout value** | Value decimal places: **2** |
| **Format → Callout value** | Add prefix: **₹** or **$** in the format string |
| **Format → Category label** | Toggle **ON**, it will show "Total Revenue" below the number |
| **Format → General → Title** | Toggle **ON** → Title text: `Total Revenue` |
| **Size** | Place at top-left corner, make it approximately 1/5 of page width |

---

### Visual 2 — Card: Total Patients

| Step | Action |
|---|---|
| **Pick visual** | **Card** |
| **Fields well** | Drag `Total Patients` measure → **Fields** well |
| **Format → Callout value** | Display units: **None** |
| **Format → Callout value** | Decimal places: **0** |
| **Format → Category label** | Toggle **ON** |
| **Format → General → Title** | Title text: `Total Patients` |
| **Size** | Place next to Total Revenue card |

---

### Visual 3 — Card: Total Hospitals

| Step | Action |
|---|---|
| **Pick visual** | **Card** |
| **Fields well** | Drag `Total Hospitals` measure → **Fields** well |
| **Format → Callout value** | Display units: **None**, Decimal places: **0** |
| **Format → Category label** | Toggle **ON** |
| **Format → General → Title** | Title text: `Total Hospitals` |
| **Size** | Place next to Total Patients card |

---

### Visual 4 — Card: Max Billing

| Step | Action |
|---|---|
| **Pick visual** | **Card** |
| **Fields well** | Drag `Max Billing` measure → **Fields** well |
| **Format → Callout value** | Display units: **None**, Decimal places: **2**, Prefix: **₹** or **$** |
| **Format → Category label** | Toggle **ON** |
| **Format → General → Title** | Title text: `Max Billing` |
| **Size** | Place next to Total Hospitals card |

---

### Visual 5 — Card: Avg Billing

| Step | Action |
|---|---|
| **Pick visual** | **Card** |
| **Fields well** | Drag `Avg Billing` measure → **Fields** well |
| **Format → Callout value** | Display units: **None**, Decimal places: **2**, Prefix: **₹** or **$** |
| **Format → Category label** | Toggle **ON** |
| **Format → General → Title** | Title text: `Avg Billing` |
| **Size** | Place at end of top card row |

---

### Visual 6 — Line Chart: Revenue by Year

| Step | Action |
|---|---|
| **Pick visual** | Click **Line Chart** icon in Visualizations pane (line going up) |
| **X-Axis well** | Drag `Admission Year` → **X-axis** |
| **Y-Axis well** | Drag `Total Revenue` measure → **Y-axis** |
| **Fix X-Axis** | ⚠️ Click the dropdown arrow on `Admission Year` in the X-axis well → select **"Don't summarize"** (so it shows 2019, 2020... not a sum) |
| **Format → X-axis** | Title: **ON** → text: `Year` |
| **Format → Y-axis** | Title: **ON** → text: `Revenue` · Display units: **Millions** |
| **Format → Data labels** | Toggle **ON** → Decimal places: **1** · Display units: **Millions** |
| **Format → Lines → Stroke width** | Set to **3** for a thicker line |
| **Format → Markers** | Toggle **ON** → Shape: **Circle** → Size: **5** |
| **Format → General → Title** | Title text: `Revenue Trend by Year` |
| **Size** | Place in the middle-left area, take roughly half the page width |

---

### Visual 7 — Donut Chart: Patients by Medical Condition

| Step | Action |
|---|---|
| **Pick visual** | Click **Donut Chart** icon in Visualizations pane (circle with a hole) |
| **Legend well** | Drag `Medical Condition` → **Legend** |
| **Values well** | Drag `Total Patients` measure → **Values** |
| **Format → Legend** | Position: **Bottom** or **Right** |
| **Format → Detail labels** | Toggle **ON** → Label style: select **"Category, percent of total"** |
| **Format → Detail labels** | Decimal places: **1** |
| **Format → General → Title** | Title text: `Patients by Medical Condition` |
| **Size** | Place in the middle-right area, next to the Line Chart |

---

### Visual 8 — Card: Avg Age

| Step | Action |
|---|---|
| **Pick visual** | **Card** |
| **Fields well** | Drag `Avg Age` measure → **Fields** well |
| **Format → Callout value** | Display units: **None**, Decimal places: **1** |
| **Format → Category label** | Toggle **ON** |
| **Format → General → Title** | Title text: `Avg Age` |
| **Size** | Place in the bottom card row, first position |

---

### Visual 9 — Card: Male %

| Step | Action |
|---|---|
| **Pick visual** | **Card** |
| **Fields well** | Drag `Male %` measure → **Fields** well |
| **Format → Callout value** | Decimal places: **1** |
| **Format → Callout value** | If your DAX used `* 100`, add suffix **%** in Format → Callout value → Display |
| **Format → Category label** | Toggle **ON** |
| **Format → General → Title** | Title text: `Male %` |
| **Size** | Place next to Avg Age card in the bottom row |

---

### Visual 10 — Card: Female %

| Step | Action |
|---|---|
| **Pick visual** | **Card** |
| **Fields well** | Drag `Female %` measure → **Fields** well |
| **Format → Callout value** | Decimal places: **1**, Suffix: **%** |
| **Format → Category label** | Toggle **ON** |
| **Format → General → Title** | Title text: `Female %` |
| **Size** | Place next to Male % card |

---

### Visual 11 — Card: Emergency %

| Step | Action |
|---|---|
| **Pick visual** | **Card** |
| **Fields well** | Drag `Emergency %` measure → **Fields** well |
| **Format → Callout value** | Decimal places: **1**, Suffix: **%** |
| **Format → Category label** | Toggle **ON** |
| **Format → General → Title** | Title text: `Emergency %` |
| **Size** | Place next to Female % card |

---

### Visual 12 — Card: Avg Length of Stay

| Step | Action |
|---|---|
| **Pick visual** | **Card** |
| **Fields well** | Drag `Avg Length of Stay` measure → **Fields** well |
| **Format → Callout value** | Decimal places: **1**, Suffix: **days** |
| **Format → Category label** | Toggle **ON** |
| **Format → General → Title** | Title text: `Avg Length of Stay` |
| **Size** | Place at end of bottom card row |

---

### Page 1 — Slicers

#### Slicer A: Admission Year

| Step | Action |
|---|---|
| **Pick visual** | Click **Slicer** icon (funnel with lines) |
| **Field well** | Drag `Admission Year` → **Field** well |
| **Slicer type** | Click the dropdown arrow (**▼**) on the slicer header → choose **List** or **Dropdown** |
| **Format → Selection** | Multi-select with Ctrl: **ON**, "Select all" option: **ON** |
| **Size** | Place at top of the page (above the cards) or as a thin strip on the left side |

#### Slicer B: Gender

| Step | Action |
|---|---|
| **Pick visual** | **Slicer** |
| **Field well** | Drag `Gender` → **Field** well |
| **Slicer type** | Dropdown or Tile style |
| **Size** | Place next to the Year slicer |

#### Slicer C: Medical Condition

| Step | Action |
|---|---|
| **Pick visual** | **Slicer** |
| **Field well** | Drag `Medical Condition` → **Field** well |
| **Slicer type** | **Dropdown** (recommended since 6 values) |
| **Size** | Place next to the Gender slicer |

---

# 📄 PAGE 2: Patient Demographics

> Right-click page tab → Rename → type `Patient Demographics`

---

### Visual 1 — Card: Total Patients

| Step | Action |
|---|---|
| **Pick visual** | **Card** |
| **Fields well** | Drag `Total Patients` → **Fields** |
| **Format** | Decimal places: **0**, Display units: **None** |
| **Size** | Top-left |

---

### Visual 2 — Card: Avg Age

| Step | Action |
|---|---|
| **Pick visual** | **Card** |
| **Fields well** | Drag `Avg Age` → **Fields** |
| **Format** | Decimal places: **1** |
| **Size** | Next to Total Patients |

---

### Visual 3 — Card: Male %

| Step | Action |
|---|---|
| **Pick visual** | **Card** |
| **Fields well** | Drag `Male %` → **Fields** |
| **Format** | Decimal places: **1**, Suffix: **%** |
| **Size** | Next to Avg Age |

---

### Visual 4 — Card: Female %

| Step | Action |
|---|---|
| **Pick visual** | **Card** |
| **Fields well** | Drag `Female %` → **Fields** |
| **Format** | Decimal places: **1**, Suffix: **%** |
| **Size** | Next to Male % |

---

### Visual 5 — Clustered Bar Chart: Patients by Age Group

| Step | Action |
|---|---|
| **Pick visual** | Click **Clustered Bar Chart** (horizontal bars icon) |
| **Y-Axis well** | Drag `Age Group` → **Y-axis** |
| **X-Axis well** | Drag `Total Patients` measure → **X-axis** |
| **Sort order** | Click the **three dots (⋯)** on the visual → Sort by → `Age Group` → Sort ascending (so 0-17 is on top) |
| **Format → Y-axis** | Title: **ON** → text: `Age Group` |
| **Format → X-axis** | Title: **ON** → text: `No. of Patients` |
| **Format → Data labels** | Toggle **ON** → Decimal places: **0** |
| **Format → Bars → Colors** | Pick a gradient color or use a single teal/blue color |
| **Format → General → Title** | Title text: `Patients by Age Group` |
| **Size** | Place below cards, left half of the page |

---

### Visual 6 — Donut Chart: Gender Split

| Step | Action |
|---|---|
| **Pick visual** | **Donut Chart** |
| **Legend well** | Drag `Gender` → **Legend** |
| **Values well** | Drag `Total Patients` measure → **Values** |
| **Format → Legend** | Position: **Bottom** |
| **Format → Detail labels** | Toggle **ON** → Label style: **"Category, percent of total"** → Decimal places: **1** |
| **Format → Slices → Colors** | Male: pick **Blue (#4A90D9)** · Female: pick **Pink (#E91E8C)** or any contrasting pair |
| **Format → General → Title** | Title text: `Gender Distribution` |
| **Size** | Place to the right of the Age Group bar chart |

---

### Visual 7 — Stacked Column Chart: Gender by Age Group

| Step | Action |
|---|---|
| **Pick visual** | Click **Stacked Column Chart** (stacked vertical bars icon) |
| **X-Axis well** | Drag `Age Group` → **X-axis** |
| **Y-Axis well** | Drag `Total Patients` measure → **Y-axis** |
| **Legend well** | Drag `Gender` → **Legend** |
| **Sort** | Click ⋯ → Sort by → `Age Group` → Ascending |
| **Format → Legend** | Position: **Top** |
| **Format → X-axis** | Title: **ON** → text: `Age Group` |
| **Format → Y-axis** | Title: **ON** → text: `Patients` |
| **Format → Data labels** | Toggle **ON** |
| **Format → Colors** | Male: **Blue** · Female: **Pink** (matches the donut above) |
| **Format → General → Title** | Title text: `Gender Breakdown by Age Group` |
| **Size** | Place below the Age Group bar chart, left half |

---

### Visual 8 — Clustered Column Chart: Patients by Blood Type

| Step | Action |
|---|---|
| **Pick visual** | Click **Clustered Column Chart** (vertical bars icon) |
| **X-Axis well** | Drag `Blood Type` → **X-axis** |
| **Y-Axis well** | Drag `Total Patients` measure → **Y-axis** |
| **Format → X-axis** | Title: **ON** → text: `Blood Type` |
| **Format → Y-axis** | Title: **ON** → text: `Patients` |
| **Format → Data labels** | Toggle **ON** → Decimal places: **0** |
| **Format → Columns → Color** | Use a single color like **teal (#009688)** or use **conditional formatting**: click **fx** icon next to color → Format by: **Field value** → Based on: `Total Patients` → Gradient |
| **Format → General → Title** | Title text: `Patients by Blood Type` |
| **Size** | Place below the Donut chart, right half |

---

### Visual 9 — Clustered Bar Chart: Patients by Insurance Provider

| Step | Action |
|---|---|
| **Pick visual** | **Clustered Bar Chart** (horizontal bars) |
| **Y-Axis well** | Drag `Insurance Provider` → **Y-axis** |
| **X-Axis well** | Drag `Total Patients` measure → **X-axis** |
| **Sort** | Click ⋯ → Sort by → `Total Patients` → Sort descending |
| **Format → Y-axis** | Title: **ON** → text: `Insurance Provider` |
| **Format → X-axis** | Title: **ON** → text: `Patients` |
| **Format → Data labels** | Toggle **ON** → Decimal places: **0** |
| **Format → General → Title** | Title text: `Patients by Insurance Provider` |
| **Size** | Place as a full-width strip at the bottom of the page |

---

### Page 2 — Slicers

| Slicer | Field | Style |
|---|---|---|
| **Admission Year** | `Admission Year` → Field well | Dropdown |
| **Medical Condition** | `Medical Condition` → Field well | Dropdown |

Place both slicers at the top of the page.

---

# 📄 PAGE 3: Clinical Analysis

> Right-click page tab → Rename → type `Clinical Analysis`

---

### Visual 1 — Card: Total Patients

| Step | Action |
|---|---|
| **Pick visual** | **Card** |
| **Fields well** | Drag `Total Patients` → **Fields** |
| **Format** | Decimal places: **0** |

---

### Visual 2 — Card: Emergency %

| Step | Action |
|---|---|
| **Pick visual** | **Card** |
| **Fields well** | Drag `Emergency %` → **Fields** |
| **Format** | Decimal places: **1**, Suffix: **%** |

---

### Visual 3 — Card: Avg Length of Stay

| Step | Action |
|---|---|
| **Pick visual** | **Card** |
| **Fields well** | Drag `Avg Length of Stay` → **Fields** |
| **Format** | Decimal places: **1**, Suffix: **days** |

---

### Visual 4 — Card: Avg Billing

| Step | Action |
|---|---|
| **Pick visual** | **Card** |
| **Fields well** | Drag `Avg Billing` → **Fields** |
| **Format** | Decimal places: **2**, Prefix: **₹** or **$** |

---

### Visual 5 — Clustered Bar Chart: Patients by Medical Condition

| Step | Action |
|---|---|
| **Pick visual** | **Clustered Bar Chart** |
| **Y-Axis well** | Drag `Medical Condition` → **Y-axis** |
| **X-Axis well** | Drag `Total Patients` measure → **X-axis** |
| **Sort** | Click ⋯ → Sort by → `Total Patients` → Sort descending |
| **Format → Data labels** | Toggle **ON** → Decimal places: **0** |
| **Format → Bars → Colors** | Use conditional formatting: click **fx** → Gradient based on `Total Patients` → Low: light teal → High: dark teal |
| **Format → General → Title** | Title text: `Patients by Medical Condition` |
| **Size** | Place below cards, left half |

---

### Visual 6 — Clustered Bar Chart: Avg Billing by Condition

| Step | Action |
|---|---|
| **Pick visual** | **Clustered Bar Chart** |
| **Y-Axis well** | Drag `Medical Condition` → **Y-axis** |
| **X-Axis well** | Drag `Avg Billing` measure → **X-axis** |
| **Sort** | Click ⋯ → Sort by → `Avg Billing` → Sort descending |
| **Format → X-axis** | Title: **ON** → text: `Avg Billing Amount` |
| **Format → Data labels** | Toggle **ON** → Decimal places: **0** → Display units: **Thousands** |
| **Format → General → Title** | Title text: `Avg Billing by Medical Condition` |
| **Size** | Place to the right of Visual 5 |

---

### Visual 7 — Donut Chart: Admission Type Breakdown

| Step | Action |
|---|---|
| **Pick visual** | **Donut Chart** |
| **Legend well** | Drag `Admission Type` → **Legend** |
| **Values well** | Drag `Total Patients` measure → **Values** |
| **Format → Detail labels** | Toggle **ON** → Label style: **"Category, percent of total"** → Decimal places: **1** |
| **Format → Slices → Colors** | Emergency: **Red (#E74C3C)** · Urgent: **Orange (#F39C12)** · Elective: **Green (#27AE60)** |
| **Format → General → Title** | Title text: `Admission Type Distribution` |
| **Size** | Place in the middle row, left side |

---

### Visual 8 — Donut Chart: Test Results Distribution

| Step | Action |
|---|---|
| **Pick visual** | **Donut Chart** |
| **Legend well** | Drag `Test Results` → **Legend** |
| **Values well** | Drag `Total Patients` measure → **Values** |
| **Format → Detail labels** | Toggle **ON** → Label style: **"Category, percent of total"** → Decimal places: **1** |
| **Format → Slices → Colors** | Normal: **Green (#27AE60)** · Abnormal: **Red (#E74C3C)** · Inconclusive: **Yellow (#F1C40F)** |
| **Format → General → Title** | Title text: `Test Results Distribution` |
| **Size** | Place next to Admission Type donut |

---

### Visual 9 — Clustered Column Chart: Medication Usage

| Step | Action |
|---|---|
| **Pick visual** | **Clustered Column Chart** (vertical bars) |
| **X-Axis well** | Drag `Medication` → **X-axis** |
| **Y-Axis well** | Drag `Total Patients` measure → **Y-axis** |
| **Sort** | Click ⋯ → Sort by → `Total Patients` → Sort descending |
| **Format → X-axis** | Title: **ON** → text: `Medication` |
| **Format → Y-axis** | Title: **ON** → text: `Patients` |
| **Format → Data labels** | Toggle **ON** → Decimal places: **0** |
| **Format → General → Title** | Title text: `Medication Usage` |
| **Size** | Place in the lower row, left side |

---

### Visual 10 — Clustered Bar Chart: Avg LOS by Medical Condition

| Step | Action |
|---|---|
| **Pick visual** | **Clustered Bar Chart** |
| **Y-Axis well** | Drag `Medical Condition` → **Y-axis** |
| **X-Axis well** | Drag `Avg Length of Stay` measure → **X-axis** |
| **Sort** | Click ⋯ → Sort by → `Avg Length of Stay` → Sort descending |
| **Format → X-axis** | Title: **ON** → text: `Avg Days` |
| **Format → Data labels** | Toggle **ON** → Decimal places: **1** |
| **Format → General → Title** | Title text: `Avg Length of Stay by Condition` |
| **Size** | Place next to Medication chart |

---

### Visual 11 — Matrix: Condition × Test Results

| Step | Action |
|---|---|
| **Pick visual** | Click **Matrix** icon (looks like a grid/table with hierarchy) |
| **Rows well** | Drag `Medical Condition` → **Rows** |
| **Columns well** | Drag `Test Results` → **Columns** |
| **Values well** | Drag `Total Patients` measure → **Values** |
| **Format → Style** | Style presets: pick **Bold header** or **Alternating rows** |
| **Format → Column headers** | Font size: **10**, Bold: **ON** |
| **Format → Row headers** | Font size: **10** |
| **Format → Values** | Font size: **10** |
| **Conditional formatting** | Click the dropdown arrow (▼) next to `Total Patients` in the Values well → **Conditional formatting → Background color** → Toggle **ON** → Format style: **Gradient** → Minimum color: **White** → Maximum color: **Dark Teal (#00796B)** |
| **Format → General → Title** | Title text: `Condition vs Test Results (Heatmap)` |
| **Size** | Place as a full-width visual at the bottom |

> [!TIP]
> The conditional formatting turns this into a heatmap — higher patient counts will appear as darker cells, making patterns easy to spot.

---

### Page 3 — Slicers

| Slicer | Field | Style |
|---|---|---|
| **Admission Year** | `Admission Year` → Field well | Dropdown |
| **Gender** | `Gender` → Field well | Tile / Buttons |
| **Age Group** | `Age Group` → Field well | Dropdown |

Place all three slicers at the top of the page.

---

# 📄 PAGE 4: Billing & Revenue

> Right-click page tab → Rename → type `Billing & Revenue`

---

### Visual 1 — Card: Total Revenue

| Step | Action |
|---|---|
| **Pick visual** | **Card** |
| **Fields well** | Drag `Total Revenue` → **Fields** |
| **Format** | Display units: **Millions** or **None**, Decimal places: **2**, Prefix: **₹** or **$** |

---

### Visual 2 — Card: Avg Billing

| Step | Action |
|---|---|
| **Pick visual** | **Card** |
| **Fields well** | Drag `Avg Billing` → **Fields** |
| **Format** | Decimal places: **2**, Prefix: **₹** or **$** |

---

### Visual 3 — Card: Max Billing

| Step | Action |
|---|---|
| **Pick visual** | **Card** |
| **Fields well** | Drag `Max Billing` → **Fields** |
| **Format** | Decimal places: **2**, Prefix: **₹** or **$** |

---

### Visual 4 — Line Chart: Revenue by Year

| Step | Action |
|---|---|
| **Pick visual** | **Line Chart** |
| **X-Axis well** | Drag `Admission Year` → **X-axis** |
| **Y-Axis well** | Drag `Total Revenue` measure → **Y-axis** |
| **Fix X-Axis** | ⚠️ Click dropdown on `Admission Year` in X-axis well → **"Don't summarize"** |
| **Format → Data labels** | Toggle **ON** → Display units: **Millions** → Decimal places: **1** |
| **Format → Markers** | Toggle **ON** → Size: **5** |
| **Format → Lines** | Stroke width: **3** → Color: **Dark Blue (#1A237E)** |
| **Format → General → Title** | Title text: `Revenue Trend by Year` |
| **Size** | Below cards, left half |

---

### Visual 5 — Clustered Bar Chart: Revenue by Insurance Provider

| Step | Action |
|---|---|
| **Pick visual** | **Clustered Bar Chart** |
| **Y-Axis well** | Drag `Insurance Provider` → **Y-axis** |
| **X-Axis well** | Drag `Total Revenue` measure → **X-axis** |
| **Sort** | Click ⋯ → Sort by → `Total Revenue` → Sort descending |
| **Format → X-axis** | Title: **ON** → text: `Revenue` → Display units: **Millions** |
| **Format → Data labels** | Toggle **ON** → Display units: **Millions** → Decimal places: **1** |
| **Format → General → Title** | Title text: `Revenue by Insurance Provider` |
| **Size** | Next to Line Chart, right half |

---

### Visual 6 — Clustered Column Chart: Revenue by Medical Condition

| Step | Action |
|---|---|
| **Pick visual** | **Clustered Column Chart** |
| **X-Axis well** | Drag `Medical Condition` → **X-axis** |
| **Y-Axis well** | Drag `Total Revenue` measure → **Y-axis** |
| **Sort** | Click ⋯ → Sort by → `Total Revenue` → Sort descending |
| **Format → Y-axis** | Display units: **Millions** |
| **Format → Data labels** | Toggle **ON** → Display units: **Millions** → Decimal places: **1** |
| **Format → Columns → Color** | Use conditional formatting: **fx** → Gradient → Low: **Light Blue** → High: **Dark Blue** |
| **Format → General → Title** | Title text: `Revenue by Medical Condition` |
| **Size** | Middle row, left half |

---

### Visual 7 — Donut Chart: Revenue by Admission Type

| Step | Action |
|---|---|
| **Pick visual** | **Donut Chart** |
| **Legend well** | Drag `Admission Type` → **Legend** |
| **Values well** | Drag `Total Revenue` measure → **Values** |
| **Format → Detail labels** | Toggle **ON** → Label style: **"Category, percent of total"** → Decimal places: **1** |
| **Format → Slices → Colors** | Emergency: **Red** · Urgent: **Orange** · Elective: **Green** |
| **Format → General → Title** | Title text: `Revenue by Admission Type` |
| **Size** | Middle row, right half |

---

### Visual 8 — Clustered Bar Chart: Avg Billing by Age Group

| Step | Action |
|---|---|
| **Pick visual** | **Clustered Bar Chart** |
| **Y-Axis well** | Drag `Age Group` → **Y-axis** |
| **X-Axis well** | Drag `Avg Billing` measure → **X-axis** |
| **Sort** | Click ⋯ → Sort by → `Age Group` → Sort ascending |
| **Format → X-axis** | Title: **ON** → text: `Avg Billing Amount` |
| **Format → Data labels** | Toggle **ON** → Decimal places: **0** → Display units: **Thousands** |
| **Format → General → Title** | Title text: `Avg Billing by Age Group` |
| **Size** | Lower row, left half |

---

### Visual 9 — Clustered Bar Chart: Top 10 Hospitals by Revenue

| Step | Action |
|---|---|
| **Pick visual** | **Clustered Bar Chart** |
| **Y-Axis well** | Drag `Hospital` → **Y-axis** |
| **X-Axis well** | Drag `Total Revenue` measure → **X-axis** |
| **Apply Top N Filter** | 1. In the **Filters pane** (right side), find `Hospital` under "Filters on this visual" |
| | 2. Change filter type from **Basic filtering** → **Top N** |
| | 3. Show top: **10** |
| | 4. By value: Drag `Total Revenue` measure into the **"By value"** box |
| | 5. Click **Apply filter** |
| **Sort** | Click ⋯ → Sort by → `Total Revenue` → Sort descending |
| **Format → Data labels** | Toggle **ON** → Decimal places: **0** |
| **Format → General → Title** | Title text: `Top 10 Hospitals by Revenue` |
| **Size** | Lower row, right half |

> [!IMPORTANT]
> The Top N filter is the key step here. Without it, you'll see all 39,874 hospitals which makes the chart unreadable. The filter shows only the top 10 revenue-generating hospitals.

---

### Visual 10 — Clustered Column Chart: Billing Distribution (Histogram)

| Step | Action |
|---|---|
| **Pick visual** | **Clustered Column Chart** |
| **X-Axis well** | Drag `Billing Amount` (the raw column, NOT the measure) → **X-axis** |
| **Create bins** | ⚠️ In the **Fields pane** (right side), right-click `Billing Amount` → **New group** → Bin type: **Bin** → Bin size: **5000** → Click OK |
| | This creates a new field called `Billing Amount (bins)` |
| **X-Axis well** | Replace with `Billing Amount (bins)` → **X-axis** |
| **Y-Axis well** | Drag `Total Patients` measure → **Y-axis** |
| **Format → X-axis** | Title: **ON** → text: `Billing Range` |
| **Format → Y-axis** | Title: **ON** → text: `Number of Patients` |
| **Format → Data labels** | Toggle **OFF** (too many bars) |
| **Format → General → Title** | Title text: `Billing Amount Distribution` |
| **Size** | Place as a full-width strip at the very bottom |

---

### Page 4 — Slicers

| Slicer | Field | Style |
|---|---|---|
| **Admission Year** | `Admission Year` → Field well | Dropdown |
| **Gender** | `Gender` → Field well | Tile / Buttons |
| **Medical Condition** | `Medical Condition` → Field well | Dropdown |
| **Insurance Provider** | `Insurance Provider` → Field well | Dropdown |

Place all four slicers in a row at the top of the page.

---

## Final Summary

| Page | Name | Cards | Charts | Slicers | Total Visuals |
|---|---|---|---|---|---|
| 1 | Executive Overview | 8 | 2 | 3 | **13** |
| 2 | Patient Demographics | 4 | 4 | 2 | **10** |
| 3 | Clinical Analysis | 4 | 5 + 1 Matrix | 3 | **13** |
| 4 | Billing & Revenue | 3 | 7 | 4 | **14** |
| | **TOTAL** | **19** | **18 + 1 Matrix** | **12** | **~50** |

> [!TIP]
> **Formatting consistency:** After building all pages, select a Card visual → right-click → **Copy formatting** → then select each other Card → right-click → **Paste formatting**. This ensures all cards have the same font, size, and style across pages.
