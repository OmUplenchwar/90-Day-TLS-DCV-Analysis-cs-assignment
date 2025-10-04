
from tabulate import tabulate

# --- Research Data from Paper (Section 3.2, 3.1) ---
# Total certificates scraped (approximate for analysis context)
TOTAL_CERTS_SCRAPED = 800000 
# Percentage of certificates found to be 90 days or less
PERCENT_90_DAYS_OR_LESS = 0.625 # 62.5%

# --- Calculation ---
PERCENT_GREATER_THAN_90_DAYS = 1.0 - PERCENT_90_DAYS_OR_LESS # Represents the high-risk legacy pool
RISK_POOL_COUNT = TOTAL_CERTS_SCRAPED * PERCENT_GREATER_THAN_90_DAYS

# --- Output for Report & Screenshot ---
print("="*60)
print("Policy Enforcement Risk Analysis: Legacy System Disruption")
print("="*60)
print(f"Analysis based on the {TOTAL_CERTS_SCRAPED:,} certificates scraped in the research.")
print("-" * 60)

data = [
    ["Certificates <= 90 Days", f"{PERCENT_90_DAYS_OR_LESS*100:.1f}%", f"{TOTAL_CERTS_SCRAPED * PERCENT_90_DAYS_OR_LESS:,.0f}"],
    ["Certificates > 90 Days (High-Risk Pool)", f"{PERCENT_GREATER_THAN_90_DAYS*100:.1f}%", f"{RISK_POOL_COUNT:,.0f}"],
]

print(tabulate(data, headers=["Category", "Percentage of Web", "Estimated Count"], tablefmt="fancy_grid"))

print("-" * 60)
print(f"Conclusion: An immediate, hard enforcement of 90-day validity would immediately risk service disruption for approximately {PERCENT_GREATER_THAN_90_DAYS*100:.1f}% of current web infrastructure (legacy systems). This necessitates a **Tiered Trust Enforcement Policy** to prevent widespread outages.")