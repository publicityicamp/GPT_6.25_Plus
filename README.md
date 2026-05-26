# Autonomous Sales Engineer by GPT 6.25 Plus
**APU Marathon 2026 "LLM Everywhere" - Preliminary Round Submission**  
An AI system that helps customers build a complete and compatible setup based on their needs, budget and delivery location. Instead of recommending only one product, the system acts like a real technical sales engineer. It understands customer requests, selects suitable components, checks compatibility, optimizes performance and cost, and generates a full quotation automatically in Gardio Dashboard.

## Project Structure
```
Autonomous-sales-engineer/
├── GPT_6_25_Plus.ipynb          # Full implementation and and Gardio dashboard launcher    
│
├── data/ (live from Google Sheets)
│   └── PRODUCT_CATALOG.csv      
│   ├── DELIVERY_LOCATIONS.csv
│   ├── NEXT_BUY_HISTORY.csv
│   └── ADDON_CATALOG.csv
├── utils/                    # Shared helper functions, calculations and compatibility rules
├── requirements.txt          # List of required Python libraries and dependencies
└── README.md                 # Project documentation and setup guide
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
| Environment | Python in Google Collab | 3.12.13 |
| LLM Framework | Google Gemini API | 3.5 Flash |
| UI Framework | Gardio | Latest |
| Data Processing | Pandas | 2.2.2 |

---
## Getting Started
### Prerequisites
- Python 3.10+ installed on your system or Google Collab
- Google Gemini API Key obtained from Google AI Studio
  
&nbsp;
### Installation and Run The Project
**Option A: Google Colab (Recommended due to Zero Setup)**
> 1. Open in Google Colab:  
(https://colab.research.google.com/drive/1cuiSnphHkgvd-ymwei7dHHOOVzATHcIj?usp=sharing)
> 2. Configuration  
>   i) Click Secrets in left sidebar  
>  ii) Add secret: `GEMINI_API_KEY`  
> iii) Insert your GEMINI API Key  
>  iv) Toggle "Notebook access" to ON   
> 3. Run all cells:  
> Runtime → Run all  
> 4. Access the dashboard:  
> Click the Gradio public link (`https://xxxx.gradio.live`) after running  

**Option B: Local Machine**
```bash
# Clone repository  
git clone (https://github.com/publicityicamp/GPT_6.25_Plus)  
cd autonomous-sales-engineer  
# Install dependencies
pip install -r requirements.txt  
# Set API key
export GEMINI_API_KEY="your-api-key-here"  # Linux/Mac
set GEMINI_API_KEY="your-api-key-here"     # Windows  
# Launch Jupyter  
jupyter notebook GPT_6_25_Plus.ipynb  
# Run all cells in the notebook  
```
&nbsp;
### Usage Example
#### User Input
> What do you want this PC setup to do? :  
> I want a smooth AAA gaming PC for 1440p gameplay. Deliver to Petaling Jaya.  
> 
> Comfort Budget (RM):  
> 4000  
> 
> Strategy Focus:  
> Optimal Value

#### System Response (30 seconds generating time)
> **Part 1: Quotation**
>     
>  OFFICIAL COMMERCIAL QUOTATION  
> CLIENT LOCATION: Petaling Jaya  
> ORDER DATE STAMP: 2026-05-26 03:01:20  
>  
> LOGISTICS NETWORK BREAKDOWN:  
>  
> ✓ Delivery Verified to Petaling Jaya  
> Estimated Delivery Transit window: 3 business days  
>  
> SPECIFIED PROCUREMENT ITEMIZATION:  
>  [CPUs        ] Ryzen 5 5600X                    RM   800  
>  [GPUs        ] GTX 1650                         RM   550  
>  [Motherboards] B450M Motherboard                RM   350  
>  [RAM         ] 16GB DDR4 RAM                    RM   250  
>  [Storage     ] 512GB NVMe SSD                   RM   180  
>  [PSU         ] 450W PSU                         RM   180  
>  [Cases       ] Budget mATX Case                 RM   120  
>  [Coolers     ] Stock Cooler                     RM     0  
>   
> SUBTOTAL BASE PACKAGE COST:                     RM   2,430  
> Shipping Logistic Fee (to Petaling Jaya)        RM       0  
>  
> TOTAL COMMERCIAL BILL COST:                     RM   2,430   
> 
> **Part 2: Your Recommended Build**
>   
> **Part 3: Carefully Picked Extras**
>   
> **Part 4: Strategy Comparison**
>   
> **Part 5: Trust & Verification**
>   
> Run our dashboard to know more about Part 2 to Part 5.
>

---
## Agent Architecture
**1. Requirement Agent**  
Extracts customer requirements such as budget, delivery location, use case, and performance needs from natural language prompts.
**2. Search Agent**  
Searches the product catalog to identify suitable and compatible PC components based on user requirements.  
**3. Compatibility Agent**    
Validates hardware compatibility including CPU sockets, RAM generation, PSU requirements and system constraints.  
**4. Optimization Agent** 
Optimizes system builds using Max Performance, Optimal Value, and Budget Saver strategies with statistical performance scoring and Pareto optimization.  
**5. Next Best Buy and Value Upsell Agent** 
Suggests upgrade paths, better-value alternatives and intelligent upsell opportunities based on customer budget behavior and performance goals.  
**6. Commercial Quotation Agent** 
Generates complete quotations including total pricing, component breakdowns and delivery-related calculations.  
**7. Explaination Agent** 
Explains recommendation reasoning, optimization decisions compatibility checks and performance trade-offs in a user-friendly format.  

---
## Recommendation Strategies
| Strategy | Description | 
| :--- | :---: | 
| Max Performance | Highest possible performance within budget | 
| Optimal Value | Best performance-to-cost ratio | 
| Budget Saver | Lowest possible cost while remaining functional | 
	
---
## Scalability & Future Potential
The current multi-agent architecture and optimization pipeline make the platform suitable for future real-world deployment and scalable technical sales automation. This system can be expanded with:  
- live retailer and e-commerce API integration
- real-time inventory and price tracking
- cloud-based deployment
- larger product catalog scaling
- enterprise procurement and technical sales support systems for businesses with bulk hardware purchasing
  
---
## Support & Contributions  
We welcome contributions to help improve the Autonomous Sales Engineer. Please follow these steps to contribute:  
1. Report Bugs & Open Issues: File an issue in the GitHub issue tracker detailing the bug behavior and replication steps.  
2. Submit Pull Requests (PRs): Fork the repository, create a new feature branch, make your modifications, ensure all agent pipelines run without exceptions and submit a detailed pull request.
---
## Contact
For questions or collaboration:  
Team: GPT 6.25 Plus  
APU Marathon 2026  
