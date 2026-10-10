
# CloudSpend Guardian

A Python-based cloud cost monitoring and budget alert platform.

## Overview

CloudSpend Guardian helps users analyze cloud service costs, monitor budget usage, and identify when spending reaches or exceeds a defined budget.

The project currently uses sample billing data and a configurable USD-to-INR conversion rate.

## Features

- Cloud service cost calculation
- USD-to-INR conversion for demo data
- Budget usage percentage calculation
- Warning when budget usage reaches 80%
- Alert when spending exceeds the budget
- Validation for invalid and negative cost values
- Automated unit tests using Python's unittest framework

## Technology Stack

- Python
- Git and GitHub
- Python unittest
- GitHub Actions (planned)

## Project Structure

```text
CloudSpend-Guardian/
├── app/
│   ├── main.py
│   └── cost_analyzer.py
├── tests/
│   └── test_cost_analyzer.py
├── docs/
├── .gitignore
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/riya2724/CloudSpend-Guardian.git
cd CloudSpend-Guardian
```

### 2. Create and activate a virtual environment

On Ubuntu or WSL:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Run the cost analyzer

```bash
python3 app/cost_analyzer.py
```

### 4. Run the unit tests

```bash
python3 -m unittest tests/test_cost_analyzer.py
```

## Currency Note

The current demo uses a fixed conversion rate of ₹85 per USD. This is an example rate, not a live exchange rate or an official billing conversion.

## Current Limitations

- Uses sample cloud cost data rather than live AWS billing data.
- Does not yet connect to AWS Cost Explorer.
- Does not automatically modify or delete cloud resources.

## Future Improvements

- Integrate AWS Cost Explorer.
- Add configurable budgets and improved cost reports.
- Automate tests using GitHub Actions.
- Add Docker support and Terraform infrastructure.
- Explore safe cloud cost optimization recommendations.

## Project Status

Core cost analysis, budget alerts, input validation, and five unit tests are implemented. Further development is in progress.

## Safety

Cost recommendations and infrastructure changes should be reviewed before any cloud resources are modified or deleted.
