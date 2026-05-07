# Roadmap Prioritization Tool

A Python-based product management tool that scores and ranks product roadmap items using impact, effort, confidence, risk, and strategic alignment.

## Overview

This project simulates how a Product Manager can use Python to evaluate and prioritize product features based on structured decision criteria.

The tool reads feature data from a CSV file, calculates a priority score, ranks each feature, and assigns a recommendation label.

## Product Management Use Case

Product teams often need to decide which features should be prioritized first. This tool supports that decision by creating a transparent scoring model.

The scoring model considers:

- Impact
- Effort
- Confidence
- Risk
- Strategic Alignment

## Scoring Formula

Priority Score = (Impact × Confidence × Strategic Alignment) / (Effort + Risk)

## Recommendation Logic

| Score Range | Recommendation |
|---|---|
| 75 or higher | Prioritize |
| 50 to 74.99 | Evaluate |
| Below 50 | Defer |

## Technologies Used

- Python
- Pandas
- CSV data analysis

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt