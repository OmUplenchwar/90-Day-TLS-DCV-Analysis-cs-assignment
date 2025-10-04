import sys
import time
from tabulate import tabulate  # Use 'pip install tabulate' if needed

# --- Research Parameters ---
NUM_CERTS = 500  # A moderate-sized organization
DCV_TIME_PER_CERT_SEC = 0.5  # Simulated time (in seconds) taken for one automated DCV check

# --- Model Parameters from Research Paper ---
CURRENT_LIFESPAN_DAYS = 398
PROPOSED_LIFESPAN_DAYS = 90

# --- Simulation Logic ---
def calculate_dcv_burden(days, num_certs, time_per_cert):
    """Calculates the total system burden (time) to manage certificates over one year (365 days)."""
    num_validation_cycles = 365 / days
    time_per_cycle_sec = num_certs * time_per_cert
    total_yearly_burden_min = (num_validation_cycles * time_per_cycle_sec) / 60
    return total_yearly_burden_min, num_validation_cycles

# --- Results Calculation ---
current_burden, current_cycles = calculate_dcv_burden(CURRENT_LIFESPAN_DAYS, NUM_CERTS, DCV_TIME_PER_CERT_SEC)
proposed_burden, proposed_cycles = calculate_dcv_burden(PROPOSED_LIFESPAN_DAYS, NUM_CERTS, DCV_TIME_PER_CERT_SEC)

increase_factor = proposed_burden / current_burden
time_saved_per_cert = (398 - 90) * 86400  # Max window of vulnerability reduced in seconds (398 vs 90 days)

# --- Output for Report & Screenshot ---
print("="*60)
print("DCV Automation Feasibility Analysis: Operational Burden Comparison")
print("="*60)
print(f"Scenario: Organization with {NUM_CERTS} Certificates.")
print(f"Assumption: Automated DCV check takes {DCV_TIME_PER_CERT_SEC} seconds per certificate.")
print("-" * 60)

data = [
    ["Certificate Lifespan (Days)", CURRENT_LIFESPAN_DAYS, PROPOSED_LIFESPAN_DAYS],
    ["Validation Cycles Per Year", f"{current_cycles:.2f}x", f"{proposed_cycles:.2f}x"],
    ["Yearly System Burden (Minutes)", f"{current_burden:.2f}", f"{proposed_burden:.2f}"],
    ["Yearly System Burden (Hours)", f"{(current_burden/60):.2f}", f"{(proposed_burden/60):.2f}"]
]

print(tabulate(data, headers=["Metric", "Current (398-Day) Model", "Proposed (90-Day) Model"], tablefmt="fancy_grid"))

print("-" * 60)
print(f"Operational Burden Increase Factor: {increase_factor:.2f}x (The increased system load)")
print("-" * 60)
print("Conclusion: The administrative burden increases by a factor of over 4x, **mandating the automation** of the Domain Control Validation (DCV) process to prevent organizational disruptions.")
