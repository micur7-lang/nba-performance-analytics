# NBA Career Performance Analytics Engine

An automated, modular Extract, Transform, Load (ETL) pipeline written in Python designed to process and analyze ~4,000 historical professional athlete career records.

## Project Architectural Overview
This project implements a structured data engineering pipeline that automates the ingestion, sanitization, and structured reporting of player performance metrics. By breaking the pipeline into specialized, decoupled functions, the engine enforces strict data integrity and transformations—enabling seamless analytical computation of athlete career trajectories.

### Key Software Engineering Patterns Featured:
* **Modular ETL Pipeline Architecture:** Separates data operations into distinct functional stages (Ingestion, Cleaning, Transformation, Filtering, and Reporting).
* **Defensive Data Handling:** Integrates validation checks to handle missing data values, data anomalies, and mathematical type errors safely.
* **Algorithmic Profiling:** Implements efficient data filtering logic to isolate top-tier performance tiers across vast historical records.

## Tech Stack & Technical Domain
* **Language:** Python 3.x
* **Core Paradigms:** Functional programming, functional decomposition, stream processing concepts.
* **Domains Addressed:** Data Engineering, Predictive Analytics, Sports Informatics.

## Structural Layout
```text
nba-performance-analytics/
│
├── src/
│   ├── __init__.py      <-- Package initialization file
│   └── pipeline.py      <-- Main logic script
│
├── .gitignore           <-- Excludes compilation and system cache files
└── README.md            <-- Professional system documentation
```

## Installation and Execution
1. Clone the clean code repository:
   ```bash
   git clone https://github.com/micur7-lang/nba-performance-analytics.git
   ```
2. Step inside the application scope:
   ```bash
   cd nba-performance-analytics
   ```
3. Boot up the data pipeline via CLI:
   ```bash
   python3 src/pipeline.py
   ```