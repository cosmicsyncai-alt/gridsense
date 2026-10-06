import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="GridSense", layout="wide", page_icon="⚡")

# ─────────────────────────────────────────────────────────────────────────────
# GLOBAL STYLES
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;0,600;1,400&display=swap');

:root {
    --bg:       #08090f;
    --surface:  #0d1018;
    --card:     #111520;
    --card2:    #0f1319;
    --border:   #1c2333;
    --border2:  #232d42;
    --accent:   #00d68f;
    --accent2:  #00aacc;
    --warn:     #f59e0b;
    --danger:   #ef4444;
    --text:     #dce4f0;
    --text2:    #a8b4c8;
    --muted:    #5e6e88;
    --fh:       'Syne', sans-serif;
    --fb:       'DM Sans', sans-serif;
    --r:        12px;
}

html, body, [data-testid="stAppViewContainer"] {
    background: var(--bg) !important;
    color: var(--text);
    font-family: var(--fb);
}
.block-container {
    padding: 1.5rem 2.5rem 4rem !important;
    max-width: 1380px;
}
header[data-testid="stHeader"], [data-testid="stToolbar"],
[data-testid="stDecoration"], footer { display: none !important; }
[data-testid="stVerticalBlock"] { gap: 0 !important; }
h1,h2,h3 { font-family: var(--fh) !important; color: var(--text) !important; }
hr { border-color: var(--border) !important; margin: 1.2rem 0 !important; }

/* ── BUTTON ── */
.stButton > button {
    background: var(--accent) !important;
    color: #060a0f !important;
    border: none !important;
    border-radius: 9px !important;
    font-family: var(--fh) !important;
    font-weight: 700 !important;
    font-size: 14px !important;
    padding: 0.6rem 1.6rem !important;
    transition: all .2s ease !important;
    letter-spacing: .2px;
}
.stButton > button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 18px rgba(0,214,143,.25) !important;
}

/* ── INPUTS ── */
[data-testid="stMultiSelect"] div[data-baseweb="select"] > div,
[data-testid="stNumberInput"] input {
    background: var(--card) !important;
    border: 1px solid var(--border2) !important;
    color: var(--text) !important;
    border-radius: 9px !important;
    font-family: var(--fb) !important;
    font-size: 14px !important;
}
[data-testid="stNumberInput"] input:focus {
    border-color: var(--accent) !important;
    box-shadow: 0 0 0 2px rgba(0,214,143,.12) !important;
}
div[data-baseweb="tag"] {
    background: rgba(0,214,143,.15) !important;
    border: 1px solid rgba(0,214,143,.3) !important;
    color: var(--accent) !important;
    border-radius: 5px !important;
    font-size: 12px !important;
}
[data-testid="stSlider"] [role="slider"] { background: var(--accent) !important; }

/* ── METRIC CARDS ── */
[data-testid="stMetric"] {
    background: var(--card) !important;
    border: 1px solid var(--border2) !important;
    border-top: 2px solid var(--accent) !important;
    border-radius: var(--r) !important;
    padding: 16px 18px !important;
}
[data-testid="stMetricValue"] {
    font-family: var(--fh) !important;
    color: var(--text) !important;
    font-size: 22px !important;
    font-weight: 800 !important;
}
[data-testid="stMetricLabel"] {
    color: var(--muted) !important;
    font-size: 11px !important;
    font-weight: 600 !important;
    text-transform: uppercase;
    letter-spacing: .9px;
}

/* ── SHARED ── */
.gs-label {
    font-size: 10px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1.6px;
    color: var(--accent);
    margin-bottom: 6px;
    display: block;
}
.gs-section { margin-top: 28px; margin-bottom: 6px; }
.gs-section-head {
    font-family: var(--fh);
    font-size: .95rem;
    font-weight: 700;
    color: var(--text);
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 14px;
}
.gs-section-head::after {
    content: '';
    flex: 1;
    height: 1px;
    background: var(--border);
}

/* ── HERO ── */
.gs-hero { text-align: center; padding: 28px 0 8px; }
.gs-hero h1 {
    font-family: var(--fh);
    font-size: 2.4rem;
    font-weight: 800;
    background: linear-gradient(120deg, var(--accent) 0%, var(--accent2) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin: 0;
}
.gs-hero p { color: var(--muted); font-size: .95rem; margin-top: 6px; }

/* ── SAVINGS BANNER ── */
.gs-banner {
    background: #091a13;
    border: 1px solid rgba(0,214,143,.2);
    border-left: 3px solid var(--accent);
    border-radius: var(--r);
    padding: 16px 20px;
    margin: 14px 0 20px;
    display: flex;
    align-items: center;
    gap: 14px;
}
.gs-banner-title {
    font-family: var(--fh);
    font-size: 1.05rem;
    font-weight: 700;
    color: var(--accent);
}
.gs-banner-sub { font-size: .82rem; color: #6ab898; margin-top: 3px; line-height: 1.5; }

/* ── TOP ACTION CARD ── */
.gs-top-action {
    background: linear-gradient(135deg, #0b2018, #0d1815);
    border: 1px solid rgba(0,214,143,.28);
    border-left: 3px solid var(--accent);
    border-radius: var(--r);
    padding: 18px 22px;
    margin-bottom: 10px;
}
.gs-top-action-label {
    font-size: 10px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1.4px;
    color: var(--accent);
    margin-bottom: 8px;
    display: block;
}
.gs-top-action-main {
    font-family: var(--fh);
    font-size: 1.05rem;
    font-weight: 800;
    color: var(--text);
    margin-bottom: 6px;
}
.gs-top-action-detail { font-size: .83rem; color: var(--text2); line-height: 1.5; }
.gs-top-action-saving {
    display: inline-block;
    margin-top: 10px;
    background: rgba(0,214,143,.12);
    border: 1px solid rgba(0,214,143,.25);
    color: var(--accent);
    font-family: var(--fh);
    font-size: .78rem;
    font-weight: 700;
    padding: 4px 12px;
    border-radius: 20px;
}

/* ── FINANCIAL CARDS ── */
.gs-fin-row {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 10px;
    margin: 14px 0 20px;
}
.gs-fin-card {
    background: var(--card2);
    border: 1px solid var(--border);
    border-radius: var(--r);
    padding: 14px 10px 12px;
    text-align: center;
    min-width: 0;
    overflow: hidden;
}
.gs-fin-val {
    font-family: var(--fh);
    font-size: 1rem;
    font-weight: 800;
    color: var(--text);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    line-height: 1.25;
}
.gs-fin-lbl {
    font-size: .68rem;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: .6px;
    margin-top: 5px;
}
.gs-fin-sub { font-size: .7rem; color: var(--accent); margin-top: 3px; font-weight: 600; }

/* ── SOLAR CTA ── */
.gs-solar-cta {
    background: #0b1a10;
    border: 1px solid rgba(0,214,143,.22);
    border-radius: var(--r);
    padding: 18px 20px;
    margin: 4px 0 20px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 14px;
    flex-wrap: wrap;
}
.gs-solar-cta-title {
    font-family: var(--fh);
    font-size: .98rem;
    font-weight: 800;
    color: var(--text);
    margin-bottom: 4px;
}
.gs-solar-cta-sub { font-size: .81rem; color: #6ab898; }
.gs-solar-btn {
    display: inline-block;
    background: var(--accent);
    color: #060a0f !important;
    font-family: var(--fh);
    font-weight: 800;
    font-size: .85rem;
    padding: 10px 18px;
    border-radius: 9px;
    text-decoration: none !important;
    white-space: nowrap;
    cursor: pointer;
    transition: all .2s;
}
.gs-solar-btn:hover { opacity: .9; }

/* ── LOSS BREAKDOWN ── */
.gs-loss-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px 14px;
    border-radius: 8px;
    margin-bottom: 6px;
    background: var(--card2);
    border: 1px solid var(--border);
    gap: 10px;
}
.gs-loss-name { font-size: .85rem; color: var(--text2); font-weight: 500; flex: 1; min-width: 0; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.gs-loss-bar-wrap { flex: 2; height: 5px; background: #1a2236; border-radius: 3px; overflow: hidden; min-width: 40px; }
.gs-loss-bar { height: 5px; border-radius: 3px; background: linear-gradient(90deg, var(--warn), var(--danger)); }
.gs-loss-val { font-family: var(--fh); font-size: .88rem; font-weight: 700; color: var(--text); min-width: 52px; text-align: right; }

/* ── CARBON CARD ── */
.gs-carbon {
    background: var(--card2);
    border: 1px solid var(--border2);
    border-radius: var(--r);
    padding: 18px 20px;
    display: flex;
    align-items: center;
    gap: 20px;
    margin-bottom: 6px;
    flex-wrap: wrap;
}
.gs-carbon-val { font-family: var(--fh); font-size: 1.9rem; font-weight: 800; color: var(--accent2); line-height: 1; }
.gs-carbon-lbl { font-size: .75rem; color: var(--muted); margin-top: 4px; }
.gs-carbon-divider { width: 1px; height: 44px; background: var(--border); flex-shrink: 0; }
.gs-trees-val { font-family: var(--fh); font-size: 1.5rem; font-weight: 800; color: #4ade80; line-height: 1; }
.gs-trees-lbl { font-size: .75rem; color: var(--muted); margin-top: 4px; }

/* ── RECOMMENDATION CARDS ── */
.gs-rec {
    background: linear-gradient(135deg, #0b2018, #0e1916);
    border: 1px solid rgba(0,214,143,.24);
    border-radius: var(--r);
    padding: 14px 18px;
    margin-bottom: 9px;
    display: flex;
    align-items: flex-start;
    gap: 12px;
    transition: border-color .15s;
}
.gs-rec:hover { border-color: rgba(0,214,143,.55); box-shadow: 0 4px 18px rgba(0,214,143,.08); }
.gs-rec-icon { font-size: 1.25rem; flex-shrink: 0; margin-top: 1px; }
.gs-rec-title {
    font-family: var(--fh);
    font-weight: 700;
    font-size: .87rem;
    color: var(--text);
    display: flex;
    align-items: center;
    gap: 8px;
    flex-wrap: wrap;
}
.gs-rec-body { font-size: .79rem; color: var(--text2); margin-top: 4px; line-height: 1.55; }
.gs-badge {
    font-size: .62rem;
    font-weight: 700;
    padding: 2px 8px;
    border-radius: 20px;
    letter-spacing: .5px;
    text-transform: uppercase;
    flex-shrink: 0;
}
.bw { background: rgba(245,158,11,.12); color: var(--warn);   border: 1px solid rgba(245,158,11,.25); }
.bi { background: rgba(0,170,204,.10);  color: var(--accent2); border: 1px solid rgba(0,170,204,.2); }
.bg { background: rgba(0,214,143,.10);  color: var(--accent);  border: 1px solid rgba(0,214,143,.2); }

/* ── EMPTY STATE ── */
.gs-empty {
    background: var(--card);
    border: 1px dashed var(--border2);
    border-radius: var(--r);
    padding: 52px 28px;
    text-align: center;
}
.gs-empty-title { font-family: var(--fh); font-size: 1.05rem; font-weight: 800; color: var(--text); margin-top: 12px; }
.gs-empty-sub { font-size: .84rem; color: var(--muted); margin-top: 8px; line-height: 1.6; }

/* ── LEFT PANEL ── */
.gs-panel-title { font-family: var(--fh); font-size: 1.1rem; font-weight: 800; color: var(--text); margin-bottom: 18px; }

/* ── RESPONSIVE ── */
@media (max-width: 900px) {
    .gs-fin-row { grid-template-columns: repeat(2, 1fr); }
    .gs-solar-cta { flex-direction: column; }
    .gs-carbon { gap: 14px; }
    .block-container { padding: 1rem 1rem 3rem !important; }
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# APPLIANCE DATA — unchanged logic
# ─────────────────────────────────────────────────────────────────────────────
appliance_db = {
    "Ceiling Fan":           {"watt": 75,   "type": "continuous"},
    "LED Light":             {"watt": 15,   "type": "continuous"},
    "TV":                    {"watt": 120,  "type": "continuous"},
    "Air Conditioner":       {"type": "ac"},
    "Refrigerator":          {"type": "refrigerator"},
    "Air Cooler":            {"watt": 200,  "type": "continuous"},
    "Table Fan":             {"watt": 50,   "type": "continuous"},
    "Electric Kettle":       {"watt": 1500, "type": "fixed", "hours": 0.5},
    "Hair Dryer":            {"watt": 1200, "type": "fixed", "hours": 0.5},
    "Water Pump Motor":      {"watt": 750,  "type": "fixed", "hours": 0.5},
    "CCTV Camera":           {"watt": 10,   "type": "fixed", "hours": 24},
    "Wi-Fi Router":          {"watt": 10,   "type": "fixed", "hours": 24},
    "Washing Machine":       {"watt": 500,  "type": "fixed", "hours": 0.5},
    "Microwave Oven":        {"watt": 1200, "type": "fixed", "hours": 0.3},
    "Water Heater (Geyser)": {"watt": 2000, "type": "fixed", "hours": 1},
    "Iron":                  {"watt": 1000, "type": "fixed", "hours": 0.2},
    "Mixer Grinder":         {"watt": 750,  "type": "fixed", "hours": 0.2},
    "Induction Cooktop":     {"watt": 1800, "type": "fixed", "hours": 1},
}

# Per-appliance action tips (tip text, saving fraction)
action_tips = {
    "Air Conditioner":       ("Use ISEER from the label to compare models; set to 24°C, clean filters, and use a fan to manage demand", 0.20),
    "Water Heater (Geyser)": ("Reduce shower time; consider a solar water heater for long-term savings", 0.30),
    "Induction Cooktop":     ("Batch cook and use a pressure cooker to cut cooking time significantly", 0.20),
    "Microwave Oven":        ("Use microwave instead of oven whenever possible — 3× more efficient", 0.15),
    "Washing Machine":       ("Only run full loads in cold water — saves water and electricity", 0.20),
    "Refrigerator":          ("Compare annual kWh/year labels for similar capacity and type; keep door seals clean and temperatures appropriate", 0.12),
    "Iron":                  ("Iron in bulk batches and use an auto-shutoff iron", 0.15),
    "TV":                    ("Enable eco/energy-saving mode and reduce brightness by 30%", 0.20),
    "Ceiling Fan":           ("Upgrade to a 5-star rated BLDC fan — 65% more efficient", 0.30),
    "LED Light":             ("Install motion sensors or smart timers to avoid idle usage", 0.25),
    "Mixer Grinder":         ("Grind in batches to reduce total motor runtime", 0.15),
    "Electric Kettle":       ("Boil only the amount of water you need and descale the kettle regularly", 0.10),
    "Hair Dryer":            ("Use the lowest suitable heat setting and switch the dryer off between uses", 0.10),
    "Water Pump Motor":      ("Check for leaks and avoid running the pump longer than needed to fill the tank", 0.15),
    "Air Cooler":            ("Keep the cooler pads clean and provide ventilation so humid air can leave the room", 0.15),
    "Table Fan":             ("Switch the fan off when the room is empty and compare rated wattage when replacing it", 0.10),
    "CCTV Camera":           ("Check camera and recorder power ratings and disable unneeded features where appropriate", 0.05),
    "Wi-Fi Router":          ("Use energy-saving settings if available and turn off guest networks when not needed", 0.05),
}

# ─────────────────────────────────────────────────────────────────────────────
# HEADER
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="gs-hero">
    <h1>⚡ GridSense</h1>
    <p>Smart Energy Intelligence &amp; Carbon Insights Platform</p>
</div>
""", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# LAYOUT
# ─────────────────────────────────────────────────────────────────────────────
col1, col2 = st.columns([1, 1.65], gap="large")

# ═══════════════════════════════ LEFT PANEL ═══════════════════════════════
with col1:
    st.markdown('<span class="gs-label">Configure</span>', unsafe_allow_html=True)
    # ── STATE SELECTION ──
    state_tariff = {
        "Bihar": 7.5,
        "Delhi": 8,
        "Maharashtra": 9,
        "Karnataka": 8.5,
        "Uttar Pradesh": 7,
    }

    state = st.selectbox("Select your State", list(state_tariff.keys()))
    rate = state_tariff[state]

    # ── OPTIONAL BILL INPUT ──
    use_bill = st.toggle("Use last 3 months bill (optional)")

    if use_bill:
        st.markdown('<span class="gs-label">Last 3 Months Electricity Bill</span>', unsafe_allow_html=True)

        b1 = st.number_input("Month 1 (₹)", min_value=0)
        b2 = st.number_input("Month 2 (₹)", min_value=0)
        b3 = st.number_input("Month 3 (₹)", min_value=0)

        avg_bill = (b1 + b2 + b3) / 3 if (b1 + b2 + b3) > 0 else None
    else:
        avg_bill = None
    st.markdown('<div class="gs-panel-title">Select Appliances</div>', unsafe_allow_html=True)

    selected_appliances = st.multiselect(
        "Appliances",
        list(appliance_db.keys()),
        placeholder="Pick one or more…",
        label_visibility="collapsed",
    )

    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
    avg_hours = st.slider("Average daily usage for standard appliances (hours)", 1, 24, 6)
    st.caption("CCTV camera and Wi-Fi router are set to 24 hours/day.")

    appliance_inputs = {}
    if "Air Conditioner" in selected_appliances:
        st.markdown('<span class="gs-label" style="margin-top:18px;display:block;">Air Conditioner details</span>', unsafe_allow_html=True)
        ac_type = st.selectbox("AC type", ["Split", "Window"], key="ac_type")
        ac_tons = st.selectbox("AC capacity (tonnes)", [0.75, 1.0, 1.5, 2.0, 2.5], index=2, key="ac_tons")
        ac_stars = st.selectbox("AC BEE star rating", [1, 2, 3, 4, 5], index=2, key="ac_stars")
        ac_iseer = st.number_input("AC ISEER (from label)", min_value=1.0, max_value=10.0, value=3.5, step=0.1, key="ac_iseer")
        ac_hours = st.slider("AC daily usage (hours)", 0, 24, 6, key="ac_hours")
        appliance_inputs["Air Conditioner"] = {"type": ac_type, "tons": ac_tons, "stars": ac_stars, "iseer": ac_iseer, "hours": ac_hours}

    if "Refrigerator" in selected_appliances:
        st.markdown('<span class="gs-label" style="margin-top:18px;display:block;">Refrigerator details</span>', unsafe_allow_html=True)
        fridge_type = st.selectbox("Refrigerator type", ["Direct Cool", "Frost Free"], key="fridge_type")
        fridge_capacity = st.number_input("Refrigerator capacity (litres)", min_value=50, max_value=1000, value=300, step=10, key="fridge_capacity")
        fridge_stars = st.selectbox("Refrigerator BEE star rating", [1, 2, 3, 4, 5], index=2, key="fridge_stars")
        fridge_annual = st.number_input("Annual energy consumption from label (kWh/year)", min_value=1.0, max_value=10000.0, value=300.0, step=10.0, key="fridge_annual")
        appliance_inputs["Refrigerator"] = {"type": fridge_type, "litres": fridge_capacity, "stars": fridge_stars, "annual_kwh": fridge_annual}

    quantities = {}
    if selected_appliances:
        st.markdown('<span class="gs-label" style="margin-top:18px;display:block;">Quantity per appliance</span>', unsafe_allow_html=True)
        for a in selected_appliances:
            quantities[a] = st.number_input(a, min_value=1, value=1, key=f"qty_{a}")

    st.markdown("<div style='height:14px'></div>", unsafe_allow_html=True)
    calculate = st.button("🚀 Analyse My Usage", use_container_width=True)

# ═══════════════════════════════ RIGHT PANEL ═══════════════════════════════
with col2:

    if not calculate:
        st.markdown("""
        <div class="gs-empty">
            <div style="font-size:2.6rem">⚡</div>
            <div class="gs-empty-title">Stop Guessing Your Electricity Bill</div>
            <div class="gs-empty-sub">
                Select appliances → set usage hours →
                hit <strong style="color:#00d68f;">Analyse My Usage</strong><br>
                to see real cost, carbon impact &amp; solar savings.
            </div>
        </div>
        """, unsafe_allow_html=True)

    elif calculate and not selected_appliances:
        st.markdown("""
        <div class="gs-empty">
            <div style="font-size:2.6rem">🔌</div>
            <div class="gs-empty-title">No Appliances Selected</div>
            <div class="gs-empty-sub">Please pick at least one appliance from the left panel to begin your analysis.</div>
        </div>
        """, unsafe_allow_html=True)

    else:
        # ── CORE CALCULATIONS — unchanged ─────────────────────────────────
        appliance_kwh = {}
        total = 0
        for a in selected_appliances:
            qty = quantities[a]
            model = appliance_db[a]["type"]
            if model == "ac":
                info = appliance_inputs[a]
                kwh = info["tons"] * 3.517 / info["iseer"] * info["hours"] * 30 * qty
            elif model == "refrigerator":
                kwh = appliance_inputs[a]["annual_kwh"] / 12 * qty
            else:
                watt = appliance_db[a]["watt"]
                hours = avg_hours if model == "continuous" else appliance_db[a]["hours"]
                kwh = watt * qty * hours * 30 / 1000
            appliance_kwh[a] = kwh
            total += kwh

        if use_bill and avg_bill:
            bill = avg_bill
            total = bill / rate
        else:
            bill = total * rate
        carbon        = total * 0.82
        solar         = total / 120
        install       = solar * 60000
        subsidy       = solar * 15000
        effective     = install - subsidy
        payback       = effective / (bill * 12)
        savings       = bill * 0.15
        trees         = int((carbon * 12) / 20)
        annual_saving = savings * 12

        # Appliance cost (sorted desc)
        appliance_cost = {a: round(kwh * rate) for a, kwh in appliance_kwh.items()}
        sorted_costs   = sorted(appliance_cost.items(), key=lambda x: x[1], reverse=True)
        top_appliance, top_cost = sorted_costs[0]
        tip, saving_pct         = action_tips.get(top_appliance, ("Reduce daily usage", 0.20))
        top_saving              = round(top_cost * saving_pct)

        # ── 1. KPI METRICS ────────────────────────────────────────────────
        st.markdown('<span class="gs-label">This Month\'s Snapshot</span>', unsafe_allow_html=True)
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("⚡ Usage",  f"{total:.0f} kWh")
        m2.metric("💰 Bill",   f"₹{bill:.0f}")
        m3.metric("🌍 CO₂e / month", f"{carbon:.0f} kg")
        m4.metric("☀ Solar",  f"{solar:.1f} kW")
        st.markdown(f"""
        <div class="gs-banner">
            <div>
                <div class="gs-banner-title">Smart Insight</div>
                <div class="gs-banner-sub">
                    Based on {state} tariff (₹{rate}/kWh) ·
                    {'Real bill data used' if use_bill else 'Estimated usage model'}
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        # ── 2. SAVINGS BANNER ─────────────────────────────────────────────
        st.markdown(f"""
        <div class="gs-banner">
            <div style="font-size:1.7rem;flex-shrink:0">💸</div>
            <div>
                <div class="gs-banner-title">You could save ₹{savings:.0f}/month · ₹{savings*12:,.0f}/year</div>
                <div class="gs-banner-sub">
                    Estimated 15% reduction through smart usage habits and appliance upgrades.
                    Scroll down for your personalised action plan.
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # ── 3. FINANCIAL BREAKDOWN ────────────────────────────────────────
        st.markdown('<div class="gs-section"><div class="gs-section-head">💰 Solar Financial Breakdown</div></div>', unsafe_allow_html=True)

        # Format large numbers in Lakhs to keep cards single-line
        def fmt_inr(val):
            if val >= 100000:
                return f"₹{val/100000:.1f}L"
            return f"₹{val:,.0f}"

        st.markdown(f"""
        <div class="gs-fin-row">
            <div class="gs-fin-card">
                <div class="gs-fin-val">{fmt_inr(install)}</div>
                <div class="gs-fin-lbl">Install Cost</div>
                <div class="gs-fin-sub">Gross est.</div>
            </div>
            <div class="gs-fin-card">
                <div class="gs-fin-val">{fmt_inr(subsidy)}</div>
                <div class="gs-fin-lbl">Govt Subsidy</div>
                <div class="gs-fin-sub">PM Surya Yojana</div>
            </div>
            <div class="gs-fin-card">
                <div class="gs-fin-val">{fmt_inr(effective)}</div>
                <div class="gs-fin-lbl">Net Cost</div>
                <div class="gs-fin-sub">After subsidy</div>
            </div>
            <div class="gs-fin-card">
                <div class="gs-fin-val">{payback:.1f} yrs</div>
                <div class="gs-fin-lbl">Payback</div>
                <div class="gs-fin-sub">Break-even</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # ── SOLAR CTA ─────────────────────────────────────────────────────
        st.markdown(f"""
        <div class="gs-solar-cta">
            <div style="flex:1;min-width:180px;">
                <div class="gs-solar-cta-title">☀ Ready to eliminate your electricity bill?</div>
                <div class="gs-solar-cta-sub">
                    Save up to <strong style="color:#00d68f;">₹{annual_saving:,.0f}/year</strong>
                    with a {solar:.1f} kW rooftop system — break-even in {payback:.1f} years.
                </div>
            </div>
            <a class="gs-solar-btn" href="https://solarrooftop.gov.in" target="_blank">
                ☀ Get Free Quote →
            </a>
        </div>
        """, unsafe_allow_html=True)

        # ── 4. ENVIRONMENTAL IMPACT ───────────────────────────────────────
        st.markdown('<div class="gs-section"><div class="gs-section-head">🌍 Environmental Impact</div></div>', unsafe_allow_html=True)

        st.markdown(f"""
        <div class="gs-carbon">
            <div>
                <div class="gs-carbon-val">{carbon * 12 / 1000:.2f}</div>
               <div class="gs-carbon-lbl">estimated annual CO₂e (tonnes)</div>
            </div>
            <div class="gs-carbon-divider"></div>
            <div>
                <div class="gs-carbon-val" style="color:#6b7a99;font-size:1.1rem;">{carbon:.0f} kg</div>
                <div class="gs-carbon-lbl">CO₂e per month</div>
            </div>
            <div class="gs-carbon-divider"></div>
            <div>
                <div class="gs-trees-val">🌱 {trees}</div>
                <div class="gs-trees-lbl">
                    trees equivalent / year<br>
                    <span style="font-size:.68rem;color:#3d4d63">(1 tree absorbs ≈ 20 kg CO₂/yr)</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # ── APPLIANCE EFFICIENCY DETAILS ───────────────────────────────────
        if "Air Conditioner" in appliance_inputs or "Refrigerator" in appliance_inputs:
            st.markdown('<div class="gs-section"><div class="gs-section-head">🔎 Appliance Efficiency Details</div></div>', unsafe_allow_html=True)
            detail_cols = st.columns(2)
            if "Air Conditioner" in appliance_inputs:
                d = appliance_inputs["Air Conditioner"]
                detail_cols[0].metric("Air Conditioner", f"{d['tons']} ton · {d['stars']} Star", f"{d['type']} · ISEER {d['iseer']:.1f}")
                detail_cols[0].caption(f"Estimated AC electricity: {appliance_kwh['Air Conditioner']:.1f} kWh/month. Estimate = cooling capacity × 3.517 ÷ ISEER × hours/day × 30 × quantity; actual use varies.")
            if "Refrigerator" in appliance_inputs:
                d = appliance_inputs["Refrigerator"]
                detail_cols[1].metric("Refrigerator", f"{d['litres']} L · {d['stars']} Star", d["type"])
                detail_cols[1].caption(f"Label use: {d['annual_kwh']:.0f} kWh/year ÷ 12 = {appliance_kwh['Refrigerator'] / quantities['Refrigerator']:.1f} kWh/month per unit.")

        # ── 5. USAGE BREAKDOWN CHART ──────────────────────────────────────
        st.markdown('<div class="gs-section"><div class="gs-section-head">📊 Usage Breakdown</div></div>', unsafe_allow_html=True)

        df = pd.DataFrame({
            "Appliance": list(appliance_kwh.keys()),
            "kWh":       list(appliance_kwh.values()),
        })
        palette = ["#00d68f","#00aacc","#f59e0b","#ef4444",
                   "#a78bfa","#fb923c","#34d399","#60a5fa",
                   "#f472b6","#facc15","#4ade80"]
        fig = px.pie(df, names="Appliance", values="kWh",
                     color_discrete_sequence=palette, hole=0.42)
        fig.update_traces(
            textposition="outside",
            textinfo="percent+label",
            marker=dict(line=dict(color="#08090f", width=2)),
        )
        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor ="rgba(0,0,0,0)",
            font=dict(family="DM Sans", color="#a8b4c8", size=11),
            showlegend=False,
            margin=dict(t=10, b=10, l=10, r=10),
            height=280,
        )
        st.plotly_chart(fig, use_container_width=True)

        # ── 6. LOSS BREAKDOWN ─────────────────────────────────────────────
        st.markdown('<div class="gs-section"><div class="gs-section-head">💸 Where You\'re Losing Money</div></div>', unsafe_allow_html=True)

        max_cost = sorted_costs[0][1] if sorted_costs else 1
        for name, cost in sorted_costs:
            bar_pct = int((cost / max_cost) * 100)
            st.markdown(f"""
            <div class="gs-loss-row">
                <div class="gs-loss-name">{name}</div>
                <div class="gs-loss-bar-wrap">
                    <div class="gs-loss-bar" style="width:{bar_pct}%"></div>
                </div>
                <div class="gs-loss-val">₹{cost:,}</div>
            </div>
            """, unsafe_allow_html=True)

        # ── 7. RECOMMENDATIONS ────────────────────────────────────────────
        st.markdown('<div class="gs-section"><div class="gs-section-head">🧠 Smart Recommendations</div></div>', unsafe_allow_html=True)

        # 🎯 TOP ACTION CARD
        st.markdown(f"""
        <div class="gs-top-action">
            <span class="gs-top-action-label">🎯 Top Action to Reduce Your Bill</span>
            <div class="gs-top-action-main">
                Reduce {top_appliance} usage → Save ₹{top_saving}/month
            </div>
            <div class="gs-top-action-detail">
                <strong style="color:#dce4f0">{top_appliance}</strong> is your single biggest cost at
                ₹{top_cost:,}/month. {tip}.
            </div>
            <span class="gs-top-action-saving">💰 ₹{top_saving}/month saved · ₹{top_saving*12:,}/year</span>
        </div>
        """, unsafe_allow_html=True)

        # Additional recommendation cards
        recs = []

        if total > 500:
            recs.append({
                "icon": "⚠️",
                "title": "High Consumption Detected",
                "badge": ("HIGH USAGE", "bw"),
                "body": f"Your {total:.0f} kWh monthly usage exceeds the average Indian household. Start by tackling the appliances in the loss breakdown above.",
            })

        if "Air Conditioner" in appliance_kwh:
            ac_cost = appliance_kwh["Air Conditioner"] * rate
            recs.append({
                "icon": "❄️",
                "title": "Optimise Air Conditioner",
                "badge": ("QUICK WIN", "bi"),
                "body": f"Estimated AC cost is ₹{ac_cost:.0f}/month using the entered capacity, ISEER, and hours. Compare label details for similar models; clean filters and consider a 24°C setting.",
            })

        if "Refrigerator" in appliance_kwh:
            fridge_info = appliance_inputs["Refrigerator"]
            fridge_cost = appliance_kwh["Refrigerator"] * rate
            recs.append({
                "icon": "🧊",
                "title": "Review Refrigerator Label Use",
                "badge": ("LABEL BASED", "bi"),
                "body": f"Estimated refrigerator cost is ₹{fridge_cost:.0f}/month from {fridge_info['annual_kwh']:.0f} kWh/year on the label. Compare annual kWh for refrigerators with similar capacity and type.",
            })

        if payback < 5:
            recs.append({
                "icon": "☀️",
                "title": "Solar ROI Looks Excellent",
                "badge": ("RECOMMENDED", "bg"),
                "body": f"At {payback:.1f}-year payback, your solar investment pays off well within the 25-year panel lifespan. A {solar:.1f} kW system covers most of your usage.",
            })

        recs.append({
            "icon": "💡",
            "title": "Upgrade to BEE 5-Star Appliances",
            "badge": ("LONG-TERM", "bi"),
            "body": "Compare BEE label energy figures for similar types and capacities. Actual savings depend on usage, model, and tariff.",
        })

        recs.append({
            "icon": "⏰",
            "title": "Shift to Off-Peak Hours",
            "badge": ("EASY", "bg"),
            "body": "Run your washing machine, geyser, and EV charging after 10 PM if you're on a time-of-use tariff — same usage, lower cost.",
        })

        for r in recs:
            badge_text, badge_cls = r["badge"]
            st.markdown(f"""
            <div class="gs-rec">
                <div class="gs-rec-icon">{r['icon']}</div>
                <div style="flex:1;min-width:0">
                    <div class="gs-rec-title">
                        {r['title']}
                        <span class="gs-badge {badge_cls}">{badge_text}</span>
                    </div>
                    <div class="gs-rec-body">{r['body']}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
        st.button("⚡ Optimise My Usage Plan", use_container_width=True)

# ─────────────────────────────────────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align:center;color:#3d4d63;font-size:.76rem;padding:6px 0 20px;">
    Powered by <strong style="color:#00d68f;">GridSense</strong>
    &nbsp;·&nbsp; Energy Intelligence Platform
    &nbsp;·&nbsp; Data is indicative. Consult a certified solar installer for exact quotes.
</div>
""", unsafe_allow_html=True)
