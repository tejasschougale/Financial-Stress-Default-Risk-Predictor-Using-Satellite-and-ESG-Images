# Financial Stress & Default Risk Predictor Using Satellite and ESG Images

## 📊 Overview

This repository provides a full pipeline for predicting financial stress and default risk in companies by combining traditional financial indicators with alternative data sources such as satellite imagery and ESG event signals. It is tailored for asset managers, hedge funds, and analysts focusing on ESG-integrated investment strategies and supply chain risk management.

## 🧠 Features

- **Satellite Imagery Analysis**: Extract activity patterns from ports, factories, and mines using open imagery datasets (e.g., NASA MODIS, Sentinel-2, Planet).
- **ESG Event Detection**: Identify strikes, environmental violations, and labor disputes using natural language processing (NLP) on news and public filings.
- **Financial Signal Processing**: Integrate income statements, balance sheets, and cash flow data into predictive models.
- **ML Risk Modeling**: Predict probability of financial distress or default using tree-based models (Random Forest, XGBoost) and survival analysis.
- **Dashboard Visualization**: Visualize risk scores, factor contributions, and ESG alerts using Power BI.

## 📁 Directory Structure

```
financial-risk-predictor/
├── data/                   # Raw and processed data files
├── notebooks/              # Exploratory and development notebooks
├── src/                    # Source code for ETL, analysis, modeling
│   ├── data_pipeline.py
│   ├── image_analysis.py
│   ├── esg_nlp.py
│   ├── feature_engineering.py
│   ├── model_train.py
│   └── utils.py
├── models/                 # Stored models and results
├── dashboard/              # Power BI report files
├── reports/                # Output visualizations and logs
├── requirements.txt        # Python dependencies
├── .env.example            # Template for environment variables
└── README.md
```

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-org/financial-risk-predictor.git
cd financial-risk-predictor
```

### 2. Create a Virtual Environment and Install Dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Copy `.env.example` to `.env` and fill in necessary API keys and database credentials:

```bash
cp .env.example .env
```

### 4. Run Data Pipeline

```bash
python src/data_pipeline.py
```

### 5. Train Predictive Models

```bash
python src/model_train.py
```

### 6. Launch Power BI Dashboard

Open `dashboard/financial_risk_dashboard.pbix` in Power BI Desktop to view the risk metrics and visualizations.

## 🌐 Data Sources

- [NASA FIRMS](https://firms.modaps.eosdis.nasa.gov/)
- [ESA Copernicus Sentinel Hub](https://scihub.copernicus.eu/)
- [GDELT News API](https://www.gdeltproject.org/)
- [Refinitiv ESG Data](https://www.refinitiv.com/en/sustainable-finance/esg-scores)
- [SEC EDGAR](https://www.sec.gov/edgar.shtml)

## 🎯 Example Use Case

> Forecast credit risk in textile manufacturers across Southeast Asia by correlating:
>
> - Reduced shipping activity from satellite images of regional ports
> - ESG alerts for factory strikes or environmental citations
> - Increasing leverage and falling operating cash flow

## ⚡ Tech Stack

- Python 3.10+
- scikit-learn, XGBoost, transformers
- OpenCV, rasterio, geopy
- PostgreSQL + PostGIS
- Power BI

## 🎉 Contributing

We welcome contributions from financial engineers, data scientists, and ESG analysts. Please open issues and pull requests to collaborate.

## ✅ License

MIT License. See `LICENSE` file for details.

