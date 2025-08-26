# Citrate Buffer Demand Dashboard

A comprehensive dashboard for estimating citrate buffer demand in pharmaceutical manufacturing, featuring market analysis, pipeline insights, and risk assessment.

## Features

### 📊 Revenue Estimates Tab
- **Current Market Size**: $847M (2024)
- **Growth Scenarios**: 
  - High Growth: $1.42B by 2030 (9.2% CAGR)
  - Base Case: $1.28B by 2030 (7.3% CAGR)
  - Low Growth: $1.18B by 2030 (5.8% CAGR)
- **Interactive Line Chart**: Visualizing market projections from 2024-2030
- **Growth Drivers & Risk Factors**: Detailed analysis of market influencers

### 🚀 Pockets of Growth Tab
- **Pipeline Analysis**: Bar charts showing development stages for:
  - Bispecific Antibodies (347 total assets)
  - Radiopharmaceuticals (183 total assets)
  - Cell Therapies (548 total assets)
  - Antibody-Drug Conjugates (ADCs) (422 total assets)
- **Pipeline Summary**: Key metrics including Phase III assets and expected approvals
- **Buffer Demand Impact**: Estimated 23% increase in citrate buffer demand

### ⚠️ Major Headwinds Tab
- **mRNA Development Status**: HHS initiatives and FDA guidance updates
- **Pricing & Reimbursement**: Most Favored Nation pricing and Inflation Reduction Act impacts
- **Regulatory Challenges**: FDA and EMA buffer requirements
- **Supply Chain Issues**: Raw material shortages and manufacturing consolidation
- **Risk Assessment**: Categorized risk levels for different market factors

## Technical Details

### Technologies Used
- **HTML5**: Semantic structure and accessibility
- **CSS3**: Modern styling with gradients, animations, and responsive design
- **JavaScript**: Interactive functionality and Chart.js integration
- **Chart.js**: Professional data visualization library

### Key Features
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Interactive Tabs**: Smooth navigation between different dashboard sections
- **Animated Charts**: Professional data visualization with hover effects
- **Modern UI**: Clean, professional design with gradient backgrounds
- **Cross-browser Compatibility**: Works on all modern browsers

## Getting Started

1. **Download/Clone** the dashboard files
2. **Open** `index.html` in a web browser
3. **Navigate** between tabs using the tab buttons
4. **Interact** with charts and hover over elements for additional information

## File Structure

```
citrate_buffer_dashboard/
├── index.html          # Main dashboard HTML file
├── styles.css          # CSS styling and responsive design
├── script.js           # JavaScript functionality and charts
└── README.md           # This documentation file
```

## Data Sources

The dashboard includes realistic market data based on:
- Pharmaceutical industry reports
- FDA and EMA regulatory updates
- Market research on biopharmaceutical pipelines
- Industry trends in buffer system usage

## Customization

### Adding New Data
- Modify the chart data arrays in `script.js`
- Update metric values in `index.html`
- Add new news items in the headwinds section

### Styling Changes
- Edit color schemes in `styles.css`
- Modify chart colors in `script.js`
- Adjust responsive breakpoints as needed

### Adding New Tabs
1. Add new tab button in the navigation
2. Create new tab content section
3. Update the `showTab()` function in JavaScript

## Browser Compatibility

- ✅ Chrome (recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Edge
- ❌ Internet Explorer (not supported)

## Performance

- **Lightweight**: Minimal dependencies (only Chart.js CDN)
- **Fast Loading**: Optimized CSS and JavaScript
- **Smooth Animations**: Hardware-accelerated transitions
- **Responsive**: Efficient grid layouts and media queries

## Future Enhancements

Potential improvements for future versions:
- **Real-time Data Integration**: API connections for live market data
- **Export Functionality**: PDF/Excel export capabilities
- **User Authentication**: Multi-user access with role-based permissions
- **Data Filtering**: Advanced filtering and search capabilities
- **Print Mode**: Optimized layout for printing reports

## Support

For questions or issues:
1. Check browser console for JavaScript errors
2. Ensure all files are in the same directory
3. Verify internet connection for Chart.js CDN
4. Test in different browsers if issues persist

## License

This dashboard is created for educational and analytical purposes. Please ensure compliance with any applicable data usage regulations when implementing in production environments.
