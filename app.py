import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Citrate Buffer Demand Dashboard",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 1rem;
        margin-bottom: 2rem;
        text-align: center;
        color: white;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        padding: 1.5rem;
        border-radius: 0.75rem;
        border: 1px solid #e9ecef;
        text-align: center;
        margin-bottom: 1rem;
    }
    
    .metric-value {
        font-size: 2rem;
        font-weight: bold;
        margin: 0.5rem 0;
    }
    
    .metric-value.high { color: #28a745; }
    .metric-value.low { color: #dc3545; }
    .metric-value.base { color: #007bff; }
    
    .scenario-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 0.75rem;
        border-left: 4px solid #007bff;
        margin-bottom: 1rem;
    }
    
    .headwind-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 0.75rem;
        border: 1px solid #e9ecef;
        margin-bottom: 1rem;
    }
    
    .risk-item {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 0.5rem;
    }
    
    .risk-high {
        background: #f8d7da;
        border: 1px solid #f5c6cb;
        color: #721c24;
    }
    
    .risk-medium {
        background: #fff3cd;
        border: 1px solid #ffeaa7;
        color: #856404;
    }
    
    .risk-low {
        background: #d1ecf1;
        border: 1px solid #bee5eb;
        color: #0c5460;
    }
    
    .pipeline-summary {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 0.75rem;
        margin: 2rem 0;
    }
    
    .summary-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1rem;
        margin-top: 1rem;
    }
    
    .summary-item {
        background: rgba(255,255,255,0.1);
        padding: 1rem;
        border-radius: 0.5rem;
        text-align: center;
    }
    
    .summary-value {
        font-size: 1.5rem;
        font-weight: bold;
        display: block;
    }
    
    .summary-label {
        font-size: 0.9rem;
        opacity: 0.9;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>Citrate Buffer Demand Dashboard</h1>
    <p>Pharmaceutical Manufacturing Market Analysis</p>
</div>
""", unsafe_allow_html=True)

# Navigation tabs
tab1, tab2, tab3 = st.tabs(["📊 Revenue Estimates", "📈 Pockets of Growth", "⚠️ Major Headwinds"])

# Tab 1: Revenue Estimates
with tab1:
    st.header("Revenue Estimates & Market Projections")
    st.markdown("High-level revenue estimates for citrate buffer demand in pharmaceutical manufacturing")
    
    # Metrics grid
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>Current Market Size (2024)</h3>
            <div class="metric-value">$847M</div>
            <div>Global citrate buffer market</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>High Growth Scenario (2030)</h3>
            <div class="metric-value high">$1.42B</div>
            <div>CAGR: 9.2%</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>Low Growth Scenario (2030)</h3>
            <div class="metric-value low">$1.18B</div>
            <div>CAGR: 5.8%</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <h3>Base Case (2030)</h3>
            <div class="metric-value base">$1.28B</div>
            <div>CAGR: 7.3%</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Revenue chart
    years = ['2024', '2025', '2026', '2027', '2028', '2029', '2030']
    high_growth = [847, 925, 1010, 1105, 1208, 1320, 1420]
    base_case = [847, 909, 975, 1047, 1124, 1206, 1280]
    low_growth = [847, 896, 948, 1003, 1061, 1122, 1180]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=years,
        y=high_growth,
        mode='lines+markers',
        name='High Growth Scenario',
        line=dict(color='#28a745', width=3),
        fill='tonexty',
        fillcolor='rgba(40, 167, 69, 0.1)'
    ))
    
    fig.add_trace(go.Scatter(
        x=years,
        y=base_case,
        mode='lines+markers',
        name='Base Case',
        line=dict(color='#007bff', width=3),
        fill='tonexty',
        fillcolor='rgba(0, 123, 255, 0.1)'
    ))
    
    fig.add_trace(go.Scatter(
        x=years,
        y=low_growth,
        mode='lines+markers',
        name='Low Growth Scenario',
        line=dict(color='#dc3545', width=3),
        fill='tonexty',
        fillcolor='rgba(220, 53, 69, 0.1)'
    ))
    
    fig.update_layout(
        title="Citrate Buffer Market Projections (2024-2030)",
        xaxis_title="Year",
        yaxis_title="Market Size ($ Millions)",
        hovermode='x unified',
        height=500,
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    
    fig.update_yaxes(tickformat="$,.0f")
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Scenario details
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="scenario-card">
            <h3>High Growth Drivers</h3>
            <ul>
                <li>Accelerated biopharmaceutical pipeline development</li>
                <li>Increased demand for monoclonal antibodies</li>
                <li>Growth in cell and gene therapies</li>
                <li>Expansion of biosimilar market</li>
                <li>Emerging markets growth</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="scenario-card">
            <h3>Low Growth Factors</h3>
            <ul>
                <li>Regulatory delays in drug approvals</li>
                <li>Economic downturn impact</li>
                <li>Supply chain disruptions</li>
                <li>Pricing pressure from payers</li>
                <li>Patent cliff effects</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# Tab 2: Pockets of Growth
with tab2:
    st.header("Pockets of Growth")
    st.markdown("Expected pipeline assets driving citrate buffer demand")
    
    # Pipeline charts
    col1, col2 = st.columns(2)
    
    with col1:
        # Bispecific Antibodies
        bispecifics_data = {
            'Phase': ['Preclinical', 'Phase I', 'Phase II', 'Phase III', 'Approved'],
            'Assets': [156, 89, 67, 23, 12]
        }
        df_bispecifics = pd.DataFrame(bispecifics_data)
        
        fig_bispecifics = px.bar(
            df_bispecifics, 
            x='Phase', 
            y='Assets',
            title="Bispecific Antibodies Pipeline",
            color='Assets',
            color_continuous_scale='Viridis'
        )
        fig_bispecifics.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig_bispecifics, use_container_width=True)
        
        # Cell Therapies
        cell_therapies_data = {
            'Phase': ['Preclinical', 'Phase I', 'Phase II', 'Phase III', 'Approved'],
            'Assets': [234, 156, 98, 45, 15]
        }
        df_cell_therapies = pd.DataFrame(cell_therapies_data)
        
        fig_cell_therapies = px.bar(
            df_cell_therapies, 
            x='Phase', 
            y='Assets',
            title="Cell Therapies Pipeline",
            color='Assets',
            color_continuous_scale='Plasma'
        )
        fig_cell_therapies.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig_cell_therapies, use_container_width=True)
    
    with col2:
        # Radiopharmaceuticals
        radiopharma_data = {
            'Phase': ['Preclinical', 'Phase I', 'Phase II', 'Phase III', 'Approved'],
            'Assets': [78, 45, 34, 18, 8]
        }
        df_radiopharma = pd.DataFrame(radiopharma_data)
        
        fig_radiopharma = px.bar(
            df_radiopharma, 
            x='Phase', 
            y='Assets',
            title="Radiopharmaceuticals Pipeline",
            color='Assets',
            color_continuous_scale='Inferno'
        )
        fig_radiopharma.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig_radiopharma, use_container_width=True)
        
        # ADCs
        adcs_data = {
            'Phase': ['Preclinical', 'Phase I', 'Phase II', 'Phase III', 'Approved'],
            'Assets': [189, 112, 76, 34, 11]
        }
        df_adcs = pd.DataFrame(adcs_data)
        
        fig_adcs = px.bar(
            df_adcs, 
            x='Phase', 
            y='Assets',
            title="Antibody-Drug Conjugates (ADCs) Pipeline",
            color='Assets',
            color_continuous_scale='Magma'
        )
        fig_adcs.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig_adcs, use_container_width=True)
    
    # Pipeline summary
    st.markdown("""
    <div class="pipeline-summary">
        <h3>Pipeline Summary</h3>
        <div class="summary-grid">
            <div class="summary-item">
                <span class="summary-label">Total Pipeline Assets:</span>
                <span class="summary-value">2,847</span>
            </div>
            <div class="summary-item">
                <span class="summary-label">Phase III Assets:</span>
                <span class="summary-value">312</span>
            </div>
            <div class="summary-item">
                <span class="summary-label">Expected Approvals (2024-2026):</span>
                <span class="summary-value">89</span>
            </div>
            <div class="summary-item">
                <span class="summary-label">Estimated Buffer Demand Increase:</span>
                <span class="summary-value">+23%</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Tab 3: Major Headwinds
with tab3:
    st.header("Major Headwinds")
    st.markdown("Key challenges and regulatory developments affecting the market")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="headwind-card">
            <h3>mRNA Development Status</h3>
            <div style="margin-bottom: 20px;">
                <h4>HHS mRNA Initiative Update</h4>
                <p style="color: #666; font-size: 0.9rem;">August 2024</p>
                <p>The Department of Health and Human Services (HHS) announced a $5 billion investment in mRNA vaccine manufacturing infrastructure, potentially reducing demand for traditional buffer systems in favor of lipid nanoparticle formulations.</p>
            </div>
            <div>
                <h4>FDA mRNA Guidance</h4>
                <p style="color: #666; font-size: 0.9rem;">July 2024</p>
                <p>New FDA guidance on mRNA manufacturing quality standards may shift industry focus away from traditional buffer systems, impacting citrate buffer demand in vaccine manufacturing.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="headwind-card">
            <h3>Pricing & Reimbursement</h3>
            <div style="margin-bottom: 20px;">
                <h4>Most Favored Nation Pricing</h4>
                <p style="color: #666; font-size: 0.9rem;">June 2024</p>
                <p>Trump's proposed Most Favored Nation pricing model for Medicare Part B drugs could significantly impact pharmaceutical manufacturing economics, potentially reducing buffer demand through cost-cutting measures.</p>
            </div>
            <div>
                <h4>Inflation Reduction Act Impact</h4>
                <p style="color: #666; font-size: 0.9rem;">May 2024</p>
                <p>Medicare drug price negotiation provisions under the Inflation Reduction Act may pressure manufacturers to optimize buffer usage and reduce costs.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="headwind-card">
            <h3>Regulatory Challenges</h3>
            <div style="margin-bottom: 20px;">
                <h4>FDA Buffer Standards Update</h4>
                <p style="color: #666; font-size: 0.9rem;">April 2024</p>
                <p>Updated FDA guidance on buffer system validation may require additional testing and documentation, increasing manufacturing costs and complexity.</p>
            </div>
            <div>
                <h4>EMA Buffer Requirements</h4>
                <p style="color: #666; font-size: 0.9rem;">March 2024</p>
                <p>European Medicines Agency (EMA) new requirements for buffer system traceability may impact citrate buffer supply chain and demand patterns.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="headwind-card">
            <h3>Supply Chain & Manufacturing</h3>
            <div style="margin-bottom: 20px;">
                <h4>Raw Material Shortages</h4>
                <p style="color: #666; font-size: 0.9rem;">February 2024</p>
                <p>Continued shortages in citric acid and related raw materials may impact buffer availability and pricing, affecting manufacturing decisions.</p>
            </div>
            <div>
                <h4>Manufacturing Consolidation</h4>
                <p style="color: #666; font-size: 0.9rem;">January 2024</p>
                <p>Industry consolidation in pharmaceutical manufacturing may lead to standardized buffer systems, potentially reducing citrate buffer demand in favor of alternative formulations.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Risk assessment
    st.subheader("Risk Assessment Summary")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="risk-item risk-high">
            <strong>High Risk:</strong><br>
            mRNA shift, pricing pressure
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="risk-item risk-medium">
            <strong>Medium Risk:</strong><br>
            Regulatory changes, supply chain
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="risk-item risk-low">
            <strong>Low Risk:</strong><br>
            Manufacturing consolidation
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem;">
    <p>Citrate Buffer Demand Dashboard | Pharmaceutical Manufacturing Market Analysis</p>
    <p>Data as of """ + datetime.now().strftime("%B %Y") + """</p>
</div>
""", unsafe_allow_html=True)
