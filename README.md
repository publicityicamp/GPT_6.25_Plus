# Autonomous Sales Engineer by GPT 6.25 Plus
APU Marathon 2026 "LLM Everywhere" - Preliminary Round Submission
An AI system that helps customers build a complete and compatible setup based on their needs, budget and delivery location. Instead of recommending only one product, the system acts like a real technical sales engineer. It understands customer requests, selects suitable components, checks compatibility, optimizes performance and cost, and generates a full quotation automatically in Gardio Dashboard.

## Project Structure
AutoQuote_AI/
├── notebook.ipynb                 # Full implementation and model training notebook
├── requirements.txt               # Dependencies
├── README.md                      # This file
└── data/ (live from Google Sheets)
    ├── product_catalog.csv
    ├── delivery_locations.csv
    ├── next_buy_history.csv
    └── addon_catalog.csv

## Highlights / Main Features
**Natural Requirements Extraction**
The system understands customer requests written in normal language. It extracts important details such as budget, delivery location, and intended use automatically.

**Multi-Agent AI Architecture**
The platform uses multiple AI agents that work together like a real sales team. Each agent handles a specific task such as product matching, optimization, or compatibility checking.

**Deterministic Compatibility Layer**
The system checks whether all selected components can work together properly. It validates CPU sockets, RAM generation, PSU power requirements, and other hardware constraints.

**Pareto-Optimal Optimization Engine**
The system generates multiple optimized builds instead of only one recommendation. It supports Max Performance, Optimal Value, and Budget Saver strategies based on user needs.

**Performance Indexing Function**
The platform calculates a unified performance score using CPU, GPU, RAM, VRAM, and power usage data. This helps the AI generate balanced and efficient system builds.

**Bottleneck Mitigation Heuristics**
The system detects hardware mismatches that can reduce performance. It penalizes unbalanced combinations such as a powerful GPU paired with a weak CPU.

**Interactive Recommendation Layer**
The system presents recommendations in a clear and user-friendly format. Users can compare setups, view compatibility checks, and understand quotation breakdowns easily.

**Intelligent Upselling & Upgrade Suggestions**
The Recommendation Agent suggests better alternatives and future upgrade paths. This helps users improve performance while staying within budget.
