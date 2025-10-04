# Assignment 2: Securing the Web - DCV Automation & Revocation Data Improvement

**Research Paper:** "Securing the Web: Shortening TLS Certificate Lifespans for Enhanced Security" (Travis Friedrich)

## 1. Identified Research Gap

The original research established the security necessity of a 90-day TLS certificate lifespan. However, it concluded with an unaddressed question: **Will the Domain Control Validation (DCV) process need to be automated to be feasible at a 90-day cadence?** Additionally, the analysis was hindered by 33.78% of revocations being classified as 'unspecified', representing a critical security data quality gap.

## 2. Proposed Improvement (Model)

This project proposes a two-part solution for model improvement:

1. **DCV Operational Burden Simulation:** A Python script (`dcv_simulation.py`) to quantify the operational cost increase when moving from 398-day to 90-day validation, demonstrating the **absolute necessity of automation**.
2. **Enhanced Revocation Logging Model:** A conceptual schema (`enhanced_logging_model.txt`) to mandate detailed revocation reasons, addressing the 'unspecified' data gap and improving future security threat intelligence.

## 3. How to Run the Code

The analysis is executed via the Python script:

1. Ensure Python 3 is installed.
2. Install the `tabulate` library: `pip install tabulate`
3. Execute the script: `python dcv_simulation.py`

The output provides the calculated increase in yearly system burden.
