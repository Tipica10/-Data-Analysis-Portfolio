# Citi Markets Quantitative Analyst — Forage Job Simulation

A simulated derivatives desk task from Citi's Quantitative Analyst virtual experience program, covering futures pricing, options valuation, and risk management strategy for a hypothetical coffee trading scenario.

## Overview

The task involved advising a client on pricing and risk management around a coffee futures contract, using core quantitative finance concepts: cost-of-carry futures pricing, digital option valuation, and scenario-based risk assessment.

## 1. Fair Value of a Coffee Futures Contract

Priced the futures contract using the cost-of-carry model:

```
Fₜ = Sₜ · e^((r + d) · T)
```

Where:
- **Sₜ** = spot price of coffee ($1.20)
- **r** = risk-free rate (2%)
- **d** = storage/carry cost (1%)
- **T** = time to expiry (0.5 years)

**Result:** Fₜ = 1.2 · e^(0.03 × 0.5) ≈ **$1.22** (2 d.p.)

## 2. Digital (Binary) Option — High-Risk Investor Scenario

For a high-risk investor, recommended a **digital call option** rather than a standard option. Unlike a standard option, its payoff doesn't scale gradually with the underlying price — it pays a fixed amount if a specific condition is met at expiration, and nothing otherwise.

**Structure priced:** a digital call paying out if coffee closes above **$1.25** at expiration.

```
V = e^(−rT) × N(d₂)
V = e^(−0.02 × 0.5) × 0.396 ≈ 0.392
```

**Result:** the digital call is worth approximately **$0.39 per $1 of payout**, implying roughly a **39–40% probability** that coffee closes above $1.25 by expiration.

**Risk assessment approach:**
- Scenario analysis by varying volatility (e.g. 20%, 30%) to test how sensitive the probability is to market conditions
- Stress-testing against geopolitical scenarios (e.g. an export ban) to show concrete conditions under which the position pays off

## 3. Risk Management Across Three Scenarios

**Scenario 1 — Hedging Market Risk**
Expecting prices to rise, recommended a **call option** to lock in a buy price for the team. Paired with **stress-testing** to model how the position would perform under extreme market moves.

**Scenario 2 — Credit Risk with a New Supplier**
Recommended a **Credit Default Swap** to cover losses in the event of counterparty default, supported by **credit scoring models** to assess the supplier's default likelihood and inform the sizing of that protection.

**Scenario 3 — Operational Risk in Trade Execution**
Recommended addressing this through **staff training and development** to reduce execution error, alongside **regular audit checks** to catch process failures early.

## Skills Demonstrated
- Derivatives pricing (futures, digital options)
- Risk-neutral valuation and probability interpretation
- Scenario and sensitivity analysis
- Credit, market, and operational risk management frameworks

## Files
- `Risk_Management_Analysis.docx` — full write-up of the three risk scenarios
- `Fair_Price_Coffee_Futures.docx` — futures pricing calculation
- `Digital_Option_Scenario.docx` — digital option valuation and risk assessment
