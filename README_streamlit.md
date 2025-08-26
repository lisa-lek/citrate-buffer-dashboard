# Citrate Buffer Demand Dashboard - Streamlit Version

This is a Streamlit conversion of the original HTML dashboard for analyzing citrate buffer demand in pharmaceutical manufacturing.

## Features

- **Revenue Estimates**: Market projections with high, base, and low growth scenarios
- **Pockets of Growth**: Pipeline analysis for bispecific antibodies, radiopharmaceuticals, cell therapies, and ADCs
- **Major Headwinds**: Risk assessment and regulatory challenges affecting the market
- **Interactive Charts**: Built with Plotly for enhanced interactivity
- **Responsive Design**: Optimized for different screen sizes

## Installation

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

3. **Open your browser** and navigate to the URL shown in the terminal (typically `http://localhost:8501`)

## Dependencies

- `streamlit`: Web app framework
- `plotly`: Interactive charts and visualizations
- `pandas`: Data manipulation
- `numpy`: Numerical computing

## Dashboard Sections

### 📊 Revenue Estimates
- Current market size and projections through 2030
- Three growth scenarios with CAGR calculations
- Interactive line chart showing market trends
- Growth drivers and risk factors

### 📈 Pockets of Growth
- Pipeline analysis across therapeutic areas
- Bar charts for bispecific antibodies, radiopharmaceuticals, cell therapies, and ADCs
- Summary statistics and expected approvals

### ⚠️ Major Headwinds
- Regulatory challenges and updates
- Pricing and reimbursement impacts
- Supply chain considerations
- Risk assessment matrix

## Customization

The dashboard can be easily customized by:
- Modifying the data arrays in the Python code
- Adjusting the CSS styling in the `st.markdown` sections
- Adding new tabs or sections as needed
- Updating chart colors and layouts

## Data Sources

This dashboard uses market research data and projections for the pharmaceutical manufacturing industry. The data represents estimates and should be used for informational purposes only.

## License

This project is for educational and analytical purposes.
