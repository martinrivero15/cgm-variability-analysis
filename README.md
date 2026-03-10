# Diabetes CGM Analysis Project

This project aims to replicate and extend the analysis described in the following paper:

**Glycaemic variability metrics derived from continuous glucose monitoring data**  
https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0225817

The goal is to build a data analysis pipeline for Continuous Glucose Monitoring (CGM) data that can later be applied to a diabetes and distress research project.

## Objectives

The project implements several analyses described in the article:

- Visualization of glucose time series for individual patients
- Aggregated glucose curves by group
- Calculation of glucose variability metrics
- Entropy and nonlinear measures
- Detrended Fluctuation Analysis (DFA)
- Quality reports per patient/day
- Summary tables
- Principal Component Analysis (PCA)

## Project Structure

- `data/raw` — Original data
- `data/processed` — Processed data
- `notebooks` — Jupyter notebooks for exploration, metrics and visualization
- `src` — Python scripts for utilities, metrics, DFA, plots and reports
- `results/figures` — Generated figures
- `results/tables` — Generated tables

## Planned Analyses

### Visualizations
- Glucose vs time for individual patients
- Clinical glucose range bands
- Aggregated curves by group (median + percentile bands)

### Metrics
- Mean glucose
- Standard deviation
- Coefficient of variation
- MAGE
- CONGA-2
- Glycaemic Fluctuation Index
- Time under 100 mg/dL (TU100)
- Area over 140 mg/dL (AO140)

### Nonlinear Measures
- Approximate Entropy (ApEn)
- Sample Entropy (SampEn)
- Poincaré plot measures (SD1, SD2)

### DFA
- DFAraw
- DFAint
- Window and segment analysis

### Statistical Analysis
- Principal Component Analysis (PCA)

## Requirements

See `requirements.txt` for dependencies.