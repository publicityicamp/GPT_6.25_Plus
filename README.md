# Autonomous Sales Engineer by GPT 6.25 Plus
APU Marathon 2026 "LLM Everywhere" - Preliminary Round Submission
An AI system that helps customers build a complete and compatible setup based on their needs, budget and delivery location. Instead of recommending only one product, the system acts like a real technical sales engineer. It understands customer requests, selects suitable components, checks compatibility, optimizes performance and cost, and generates a full quotation automatically in Gardio Dashboard.

## Project Structure
```
AutoQuote_AI/
├── GPT_6_25_Plus.ipynb            # Full implementation and model training notebook
├── requirements.txt               # Dependencies
├── README.md                      # This file
└── data/ (live from Google Sheets)
    ├── product_catalog.csv
    ├── delivery_locations.csv
    ├── next_buy_history.csv
    └── addon_catalog.csv
```

---
## Highlights / Main Features
**Natural Requirements Extraction**:  
Understand customer requests written in normal language by extracting important details such as budget, delivery location, and intended use automatically.

**Multi-Agent AI Architecture**:  
Use multiple AI agents that work together like a real sales team where ach agent handles a specific task such as product matching, optimization or compatibility checking.

**Deterministic Compatibility Layer**:  
Check whether all selected components can work together properly by validating CPU sockets, RAM generation, PSU power requirements and other hardware constraints.

**Pareto-Optimal Optimization Engine**:  
Generate multiple optimized builds instead of only one recommendation. It supports Max Performance, Optimal Value, and Budget Saver strategies based on user needs.

**Performance Indexing Function**:  
Utilise statistical scoring methods on CPU, GPU, RAM, VRAM, and power usage data to calculate a unified performance score and generate balanced, efficient and budget-optimized system builds.

**Aggregation Heuristics**:  
Detect hardware mismatches that can reduce performance and penalize unbalanced combinations such as a powerful GPU paired with a weak CPU.

**Behavioral Recommendation Layer**:  
Analyze customer preferences, budget behavior and usage needs to generate more personalized recommendations. It can also suggest suitable upgrades, alternative builds and next-best-buy options based on user behavior and priorities.

**Intelligent Upselling & Upgrade Suggestions**:  
Suggests better alternatives and future upgrade paths to help users improve performance while staying within budget.

---
## Build With

| Category | Technology | Version |
| :--- | :---: | ---: |
| Environment | Python | 3.12.13 |
| LLM Framework | Google Gemini API | 3.5 Flash |
| UI Framework | Gardio | Latest |
| Data Processing | Pandas | 2.2.2 |
