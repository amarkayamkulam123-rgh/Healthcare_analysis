"""
Preprocess healthcare_data.csv into aggregated JSON for the web dashboard.
Outputs dashboard_data.json with all KPIs, chart data, and breakdowns.
"""

import pandas as pd
import numpy as np
import json
import os

# Paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE = os.path.join(SCRIPT_DIR, "..", "healthcare_data.csv")
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "dashboard_data.json")


def age_group(age):
    if age <= 17:
        return "0-17"
    elif age <= 30:
        return "18-30"
    elif age <= 45:
        return "31-45"
    elif age <= 60:
        return "46-60"
    elif age <= 75:
        return "61-75"
    else:
        return "76+"


def main():
    print("Loading data...")
    df = pd.read_csv(INPUT_FILE)
    print(f"Loaded {len(df):,} rows")

    # Clean up
    df["Billing Amount"] = pd.to_numeric(df["Billing Amount"], errors="coerce").fillna(0)
    df["Age"] = pd.to_numeric(df["Age"], errors="coerce").fillna(0).astype(int)
    df["Length of Stay (Days)"] = pd.to_numeric(df["Length of Stay (Days)"], errors="coerce").fillna(0)
    df["Admission Year"] = pd.to_numeric(df["Admission Year"], errors="coerce").fillna(0).astype(int)
    df["Age Group"] = df["Age"].apply(age_group)

    data = {}

    # ── KPIs ──
    data["kpis"] = {
        "totalRevenue": round(float(df["Billing Amount"].sum()), 2),
        "totalPatients": int(len(df)),
        "totalHospitals": int(df["Hospital"].nunique()),
        "maxBilling": round(float(df["Billing Amount"].max()), 2),
        "avgBilling": round(float(df["Billing Amount"].mean()), 2),
        "avgAge": round(float(df["Age"].mean()), 1),
        "malePercent": round(float((df["Gender"] == "Male").sum() / len(df) * 100), 1),
        "femalePercent": round(float((df["Gender"] == "Female").sum() / len(df) * 100), 1),
        "emergencyPercent": round(float((df["Admission Type"] == "Emergency").sum() / len(df) * 100), 1),
        "avgLOS": round(float(df["Length of Stay (Days)"].mean()), 1),
    }

    # ── Revenue by Year ──
    rev_year = df.groupby("Admission Year")["Billing Amount"].sum().reset_index()
    rev_year = rev_year.sort_values("Admission Year")
    data["revenueByYear"] = {
        "labels": rev_year["Admission Year"].astype(str).tolist(),
        "values": rev_year["Billing Amount"].round(2).tolist(),
    }

    # ── Patients by Year ──
    pat_year = df.groupby("Admission Year").size().reset_index(name="count")
    pat_year = pat_year.sort_values("Admission Year")
    data["patientsByYear"] = {
        "labels": pat_year["Admission Year"].astype(str).tolist(),
        "values": pat_year["count"].tolist(),
    }

    # ── Patients by Medical Condition ──
    cond = df["Medical Condition"].value_counts().reset_index()
    cond.columns = ["condition", "count"]
    data["patientsByCondition"] = {
        "labels": cond["condition"].tolist(),
        "values": cond["count"].tolist(),
    }

    # ── Patients by Age Group ──
    age_order = ["0-17", "18-30", "31-45", "46-60", "61-75", "76+"]
    ag = df["Age Group"].value_counts().reindex(age_order, fill_value=0)
    data["patientsByAgeGroup"] = {
        "labels": ag.index.tolist(),
        "values": ag.values.tolist(),
    }

    # ── Gender Distribution ──
    gen = df["Gender"].value_counts()
    data["genderDistribution"] = {
        "labels": gen.index.tolist(),
        "values": gen.values.tolist(),
    }

    # ── Gender by Age Group ──
    gag = df.groupby(["Age Group", "Gender"]).size().unstack(fill_value=0)
    gag = gag.reindex(age_order, fill_value=0)
    data["genderByAgeGroup"] = {
        "labels": gag.index.tolist(),
        "male": gag.get("Male", pd.Series(0, index=gag.index)).tolist(),
        "female": gag.get("Female", pd.Series(0, index=gag.index)).tolist(),
    }

    # ── Patients by Blood Type ──
    bt = df["Blood Type"].value_counts().sort_index()
    data["patientsByBloodType"] = {
        "labels": bt.index.tolist(),
        "values": bt.values.tolist(),
    }

    # ── Patients by Insurance Provider ──
    ins = df["Insurance Provider"].value_counts().head(10)
    data["patientsByInsurance"] = {
        "labels": ins.index.tolist(),
        "values": ins.values.tolist(),
    }

    # ── Avg Billing by Condition ──
    abc = df.groupby("Medical Condition")["Billing Amount"].mean().sort_values(ascending=False).reset_index()
    data["avgBillingByCondition"] = {
        "labels": abc["Medical Condition"].tolist(),
        "values": abc["Billing Amount"].round(2).tolist(),
    }

    # ── Admission Type Distribution ──
    at = df["Admission Type"].value_counts()
    data["admissionTypeDistribution"] = {
        "labels": at.index.tolist(),
        "values": at.values.tolist(),
    }

    # ── Test Results Distribution ──
    tr = df["Test Results"].value_counts()
    data["testResultsDistribution"] = {
        "labels": tr.index.tolist(),
        "values": tr.values.tolist(),
    }

    # ── Medication Usage ──
    med = df["Medication"].value_counts().head(10)
    data["medicationUsage"] = {
        "labels": med.index.tolist(),
        "values": med.values.tolist(),
    }

    # ── Avg LOS by Condition ──
    los = df.groupby("Medical Condition")["Length of Stay (Days)"].mean().sort_values(ascending=False).reset_index()
    data["avgLOSByCondition"] = {
        "labels": los["Medical Condition"].tolist(),
        "values": los["Length of Stay (Days)"].round(1).tolist(),
    }

    # ── Condition vs Test Results (Heatmap data) ──
    ct = pd.crosstab(df["Medical Condition"], df["Test Results"])
    data["conditionVsTestResults"] = {
        "conditions": ct.index.tolist(),
        "testResults": ct.columns.tolist(),
        "values": ct.values.tolist(),
    }

    # ── Revenue by Insurance Provider ──
    ri = df.groupby("Insurance Provider")["Billing Amount"].sum().sort_values(ascending=False).head(10).reset_index()
    data["revenueByInsurance"] = {
        "labels": ri["Insurance Provider"].tolist(),
        "values": ri["Billing Amount"].round(2).tolist(),
    }

    # ── Revenue by Medical Condition ──
    rc = df.groupby("Medical Condition")["Billing Amount"].sum().sort_values(ascending=False).reset_index()
    data["revenueByCondition"] = {
        "labels": rc["Medical Condition"].tolist(),
        "values": rc["Billing Amount"].round(2).tolist(),
    }

    # ── Revenue by Admission Type ──
    rat = df.groupby("Admission Type")["Billing Amount"].sum()
    data["revenueByAdmissionType"] = {
        "labels": rat.index.tolist(),
        "values": rat.round(2).tolist(),
    }

    # ── Avg Billing by Age Group ──
    abag = df.groupby("Age Group")["Billing Amount"].mean().reindex(age_order, fill_value=0)
    data["avgBillingByAgeGroup"] = {
        "labels": abag.index.tolist(),
        "values": abag.round(2).tolist(),
    }

    # ── Top 10 Hospitals by Revenue ──
    hosp = df.groupby("Hospital")["Billing Amount"].sum().sort_values(ascending=False).head(10).reset_index()
    data["topHospitalsByRevenue"] = {
        "labels": hosp["Hospital"].tolist(),
        "values": hosp["Billing Amount"].round(2).tolist(),
    }

    # ── Monthly Trend (patients per month across all years) ──
    month_order = ["January", "February", "March", "April", "May", "June",
                   "July", "August", "September", "October", "November", "December"]
    mo = df["Admission Month"].value_counts().reindex(month_order, fill_value=0)
    data["patientsByMonth"] = {
        "labels": month_order,
        "values": mo.values.tolist(),
    }

    # ── Billing Distribution (histogram bins) ──
    bins = list(range(0, 55001, 5000))
    labels_hist = [f"${b//1000}k-${(b+5000)//1000}k" for b in bins[:-1]]
    hist_vals, _ = np.histogram(df["Billing Amount"].dropna(), bins=bins)
    data["billingDistribution"] = {
        "labels": labels_hist,
        "values": hist_vals.tolist(),
    }

    # Convert numpy ints to native Python ints
    def convert(obj):
        if isinstance(obj, (np.integer,)):
            return int(obj)
        if isinstance(obj, (np.floating,)):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, default=convert)

    print(f"Dashboard data saved to: {OUTPUT_FILE}")
    print(f"File size: {os.path.getsize(OUTPUT_FILE) / 1024:.1f} KB")


if __name__ == "__main__":
    main()
