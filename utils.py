"""
Shared utilities: constants, data loading, feature engineering,
model loading, policy simulation helpers, and formatting.
"""

from datetime import datetime
import pandas as pd

# ─── Constants ────────────────────────────────────────────────────────────────

LOCATION_MAPPING = {
    # Penang area
    'penang': 'George Town',
    'pg': 'George Town',
    'george town': 'George Town',
    'georgetown': 'George Town',
    'butterworth': 'Butterworth',
    'bukit mertajam': 'Bukit Mertajam',
    'bayan lepas': 'Bayan Lepas',

    # Klang Valley
    'kl': 'Kuala Lumpur',
    'kuala lumpur': 'Kuala Lumpur',
    'putrajaya': 'Putrajaya',
    'selangor': 'Shah Alam',
    'shah alam': 'Shah Alam',
    'petaling jaya': 'Petaling Jaya',
    'subang jaya': 'Subang Jaya',
    'puchong': 'Puchong',
    'cyberjaya': 'Cyberjaya',
    'klang': 'Klang',

    # Johor
    'jb': 'Johor Bahru',
    'johor bahru': 'Johor Bahru',
    'johor': 'Johor Bahru',
    'iskandar puteri': 'Iskandar Puteri',
    'batu pahat': 'Batu Pahat',
    'muar': 'Muar',
    'kluang': 'Kluang',

    # East Malaysia
    'kk': 'Kota Kinabalu',
    'kota kinabalu': 'Kota Kinabalu',
    'sabah': 'Kota Kinabalu',
    'sandakan': 'Sandakan',
    'tawau': 'Tawau',
    'kuching': 'Kuching',
    'sarawak': 'Kuching',
    'sibu': 'Sibu',
    'miri': 'Miri',
    'bintulu': 'Bintulu',

    # Other states
    'ipoh': 'Ipoh',
    'perak': 'Ipoh',
    'taiping': 'Taiping',
    'teluk intan': 'Teluk Intan',
    'alor setar': 'Alor Setar',
    'kedah': 'Alor Setar',
    'sungai petani': 'Sungai Petani',
    'langkawi': 'Langkawi',
    'melaka': 'Malacca City',
    'malacca': 'Malacca City',
    'kuantan': 'Pahang',
    'pahang': 'Kuantan',
    'kota bharu': 'Kota Bharu',
    'kelantan': 'Kota Bharu',
    'kuala terengganu': 'Kuala Terengganu',
    'terengganu': 'Kuala Terengganu',
    'seremban': 'Seremban',
    'negeri sembilan': 'Seremban',
    'port dickson': 'Port Dickson',
    'kangar': 'Kangar',
    'perlis': 'Kangar',
}

# ─── Data Loading & Feature Engineering ───────────────────────────────────────

def normalize_location(user_location: str, delivery_locations: dict) -> str | None:
    """
    Convert raw user location text input to match official database location names.
    
    Args:
        user_location (str): Raw string provided by the user.
        delivery_locations (dict): Active dictionary database of serviceable locations.
        
    Returns:
        str | None: Matched official location title string or None if unserviced.
    """
    if not user_location:
        return None

    user_loc_lower = user_location.lower().strip()

    # Direct match
    for loc in delivery_locations.keys():
        if loc.lower() == user_loc_lower:
            return loc

    # Alias mapping fallback
    if user_loc_lower in LOCATION_MAPPING:
        return LOCATION_MAPPING[user_loc_lower]

    # Partial match fallback
    for loc in delivery_locations.keys():
        if user_loc_lower in loc.lower() or loc.lower() in user_loc_lower:
            return loc

    return None

# ─── Policy Simulation Helpers ────────────────────────────────────────────────

def safe_money(value) -> float:
    """Safely cast incoming arbitrary fields to float values or fall back to 0.0."""
    try:
        return float(value)
    except (ValueError, TypeError):
        return 0.0


def calculate_selected_build_total(components: list, requirements: dict) -> float:
    """
    Accumulates base configuration pricing metrics plus dynamic active logistics fees.
    """
    component_total = 0.0
    for item in components:
        component_total += safe_money(item.get("price", 0))

    shipping_fee = 0.0
    for key in ["delivery_fee", "shipping_fee", "delivery_cost"]:
        if key in requirements:
            shipping_fee = safe_money(requirements.get(key, 0))
            break

    return component_total + shipping_fee

# ─── Formatting & Component Matrix Builders ──────────────────────────────────

def format_price(value, prefix: str = "RM") -> str:
    """Formats raw numeric parameters into standardized regional accounting currency tokens."""
    try:
        return f"{prefix} {int(value):,}"
    except (ValueError, TypeError):
        return f"{prefix} 0"


def build_strategy_summary(strategies: dict) -> pd.DataFrame:
    """Constructs a high-level pandas DataFrame row summary for alternative optimization strategies."""
    rows = []
    if not strategies:
        return pd.DataFrame(
            columns=["Setup Option", "Total Price (RM)", "Estimated Speed Rating", "Value Efficiency"]
        )

    for strategy_name, info in strategies.items():
        rows.append({
            "Setup Option": strategy_name.replace("_", " ").title(),
            "Total Price (RM)": f"RM {info.get('total_cost', 0):,}",
            "Estimated Speed Rating": f"{round(info.get('performance_score', 0), 1)} / 500",
            "Value Efficiency": f"{round(info.get('value_ratio', 0), 4)} points/RM"
        })

    return pd.DataFrame(rows)


def build_component_matrix(strategies: dict) -> pd.DataFrame:
    """Flattens nested multi-strategy hardware builds into an inventory data tracking matrix."""
    rows = []
    if not strategies:
        return pd.DataFrame(
            columns=["Build Profile", "Part Category", "Component Model", "Price", "Warehouse Status"]
        )

    for strategy_name, info in strategies.items():
        display_strategy = strategy_name.replace("_", " ").title()

        for item in info.get("components", []):
            stock_num = item.get("stock", 0)
            stock_str = (
                "✅ In Stock" if stock_num > 10
                else ("⚠️ Low Stock" if stock_num > 0 else "❌ Reserved")
            )

            rows.append({
                "Build Profile": display_strategy,
                "Part Category": item.get("type", "-"),
                "Component Model": item.get("name", "-"),
                "Price": f"RM {item.get('price', 0):,}",
                "Warehouse Status": stock_str
            })

    return pd.DataFrame(rows)


def build_compatibility_markdown(compat: dict) -> str:
    """Parses structural safety alerts and renders clean technical markdown notes."""
    status = compat.get("status", "Unknown")
    messages = compat.get("messages", [])

    md = f"### System Health Status: **Verified {status}**\n\n"
    if messages:
        for msg in messages:
            md += f"✅ {msg}\n"
    else:
        md += "✅ Component compatibility validated across selected system parts.\n"

    return md


def build_requirement_markdown(requirements: dict) -> str:
    """Generates a scannable dashboard summary layout row displaying structured client requests."""
    if not requirements:
        return "No active customer profile analyzed yet."

    return f"""
<div class="profile-summary">
    <div class="profile-item">
        <span class="profile-label">Budget</span>
        <span class="profile-value">RM {requirements.get("budget", "-")}</span>
    </div>
    <div class="profile-item">
        <span class="profile-label">Delivery Target</span>
        <span class="profile-value">{requirements.get("location", "-")}</span>
    </div>
    <div class="profile-item">
        <span class="profile-label">Main Use Case</span>
        <span class="profile-value">{str(requirements.get("use_case", "-")).title()}</span>
    </div>
</div>
"""


def build_value_recommendation_cards(upsell_data: dict) -> str:
    """
    Transforms auxiliary cross-sell items and budget upsize options into premium grid layout cards.
    """
    def _get_first_item(items):
        return items[0] if items and len(items) > 0 else {}

    you_may_need = _get_first_item(upsell_data.get("frequently_bought_next", []))
    complete_setup = _get_first_item(upsell_data.get("complete_your_setup", []))
    better_value = _get_first_item(upsell_data.get("smart_budget_upsize", []))

    # Card 1 Allocation Logic
    if you_may_need:
        card_1_title = you_may_need.get("recommendation", "Suggested Item")
        card_1_price = you_may_need.get("price", 0)
        card_1_reason = you_may_need.get("reason", "Often selected by similar customers.")
        card_1_signal = you_may_need.get("similarity_signal", "Strong match")
    else:
        card_1_title, card_1_price = "No immediate extra item needed", 0
        card_1_reason = "Your selected setup already covers the core requirement."
        card_1_signal = "No strong pattern detected"

    # Card 2 Allocation Logic
    if complete_setup:
        card_2_title = complete_setup.get("recommendation", "Suggested Add-on")
        card_2_price = complete_setup.get("price", 0)
        card_2_reason = complete_setup.get("reason", "Helps improve the full setup experience.")
        card_2_priority = complete_setup.get("priority", "Recommended")
    else:
        card_2_title, card_2_price = "Setup already feels complete", 0
        card_2_reason = "No essential add-on is required for this configuration."
        card_2_priority = "Optional"

    # Card 3 Allocation Logic
    if better_value:
        card_3_title = better_value.get("recommended_upgrade", "Better Option")
        card_3_price = better_value.get("extra_cost", 0)
        card_3_reason = better_value.get("benefit", "Provides stronger long-term value.")
        card_3_current = better_value.get("current_item", "Current choice")
    else:
        card_3_title, card_3_price = "No value upgrade needed", 0
        card_3_reason = "The selected setup already gives a balanced value profile."
        card_3_current = "Current setup"

    return f"""
<div class="recommendation-grid">
    <div class="value-card blue-card">
        <div class="card-eyebrow">💡 You May Also Need</div>
        <div class="card-title">{card_1_title}</div>
        <div class="card-price">{format_price(card_1_price, "RM")}</div>
        <div class="card-body">{card_1_reason}</div>
        <div class="card-tag">Customer Match: {card_1_signal}</div>
    </div>

    <div class="value-card green-card">
        <div class="card-eyebrow">🧩 Make Your Setup Complete</div>
        <div class="card-title">{card_2_title}</div>
        <div class="card-price">{format_price(card_2_price, "RM")}</div>
        <div class="card-body">{card_2_reason}</div>
        <div class="card-tag">Priority: {card_2_priority}</div>
    </div>

    <div class="value-card amber-card">
        <div class="card-eyebrow">📈 Better Value Option</div>
        <div class="card-title">{card_3_title}</div>
        <div class="card-price"> Top up RM {int(card_3_price):,}</div>
        <div class="card-body">{card_3_reason}</div>
        <div class="card-tag">Current: {card_3_current}</div>
    </div>
</div>
"""


def build_recommendation_detail_df(upsell_data: dict) -> pd.DataFrame:
    """Compiles secondary recommendation details across sections into an reviewable DataFrame."""
    rows = []

    for item in upsell_data.get("frequently_bought_next", []):
        rows.append({
            "Section": "You May Also Need",
            "Suggestion": item.get("recommendation", "-"),
            "Price": f"RM {item.get('price', 0):,}",
            "Why": item.get("reason", "-")
        })

    for item in upsell_data.get("complete_your_setup", []):
        rows.append({
            "Section": "Make Your Setup Complete",
            "Suggestion": item.get("recommendation", "-"),
            "Price": f"RM {item.get('price', 0):,}",
            "Why": item.get("reason", "-")
        })

    for item in upsell_data.get("smart_budget_upsize", []):
        rows.append({
            "Section": "Better Value Option",
            "Suggestion": item.get("recommended_upgrade", "-"),
            "Price": f"+RM {item.get('extra_cost', 0):,}",
            "Why": item.get("benefit", "-")
        })

    if not rows:
        return pd.DataFrame(columns=["Section", "Suggestion", "Price", "Why"])

    return pd.DataFrame(rows)
