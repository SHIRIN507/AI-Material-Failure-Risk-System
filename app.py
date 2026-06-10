import streamlit as st
import base64

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="AI Material Failure Risk System",
    page_icon="⚙️",
    layout="wide"
)

# =========================
# BACKGROUND IMAGE
# =========================
def add_bg(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    .block-container {{
        background: rgba(0,0,0,0.55);
        padding: 20px;
        border-radius: 15px;
    }}
    </style>
    """, unsafe_allow_html=True)

add_bg("background.png")

# =========================
# UI STYLE
# =========================
# =========================
# UI STYLE
# =========================
st.markdown("""
<style>

/* =========================
   GLOBAL
========================= */
html, body, [class*="css"] {
    font-family: "Amaze Script S11", cursive;
    letter-spacing: 1px;
    color: white !important;
}

/* =========================
   MAIN BACKGROUND TEXT
========================= */
h1, h2, h3 {
    color: #00d9ff !important;
    text-shadow: 0 0 10px #00d9ff;
}

/* =========================
   SIDEBAR
========================= */
section[data-testid="stSidebar"] {
    background: rgba(0,0,0,0.88) !important;
    border-right: 2px solid #00d9ff;
}

/* Sidebar labels */
section[data-testid="stSidebar"] label {
    color: white !important;
    font-weight: bold;
}

/* =========================
   SELECTBOX MAIN AREA
========================= */
.stSelectbox div[data-baseweb="select"] > div {
    background-color: white !important;
    color: black !important;
    border-radius: 12px !important;
    border: 1px solid #00d9ff !important;
}

/* Selected text */
.stSelectbox div[data-baseweb="select"] span {
    color: black !important;
    font-weight: 600 !important;
}

/* Dropdown menu */
div[role="listbox"] {
    background-color: white !important;
}

/* Dropdown options */
div[role="option"] {
    color: black !important;
    background-color: white !important;
    font-weight: 600 !important;
}

/* Hover option */
div[role="option"]:hover {
    background-color: #d9f7ff !important;
    color: black !important;
}

/* =========================
   NUMBER INPUTS
========================= */
.stNumberInput input {
    background-color: white !important;
    color: black !important;
    border-radius: 10px !important;
    font-weight: bold !important;
}

/* =========================
   TEXT INPUTS
========================= */
input, textarea {
    background-color: white !important;
    color: black !important;
    border: 1px solid #00d9ff !important;
}

/* =========================
   BUTTONS
========================= */
div.stButton > button {
    background: rgba(0,217,255,0.1);
    color: #00d9ff;
    border: 1px solid #00d9ff;
    border-radius: 10px;
    font-weight: bold;
}

div.stButton > button:hover {
    background: #00d9ff;
    color: black;
    box-shadow: 0 0 15px #00d9ff;
}

/* =========================
   FAILURE BOX
========================= */
.risk-box {
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    font-size: 24px;
    font-weight: bold;
    background: rgba(0,0,0,0.6);
    border: 2px solid #00d9ff;
    box-shadow: 0 0 25px #00d9ff;
}

/* =========================
   RISK COLORS
========================= */
.low {
    color: #00ff99;
}

.medium {
    color: #ffcc00;
}

.high {
    color: #ff4d4d;
}

/* =========================
   PROGRESS BAR
========================= */
.stProgress > div > div > div > div {
    background-color: #00d9ff;
}

/* =========================
   METRIC COLORS
========================= */
[data-testid="stMetricLabel"] {
    color: white !important;
}

[data-testid="stMetricValue"] {
    color: white !important;
}

/* =========================
   GENERAL TEXT
========================= */
div[data-testid="stMarkdownContainer"] p {
    color: white !important;
}
/* =========================
   RANKING TEXT FIX
========================= */

div[data-testid="stMarkdownContainer"] p {
    color: #ffffff !important;
    font-weight: bold !important;
    opacity: 1 !important;
}

/* Ranking material names */
div[data-testid="stMarkdownContainer"] strong {
    color: #ffffff !important;
}

/* Ranking lines */
.stMarkdown {
    color: #ffffff !important;
}
</style>
""", unsafe_allow_html=True)

# =========================
# TITLE
# =========================
st.title("⚙️ AI-Based Failure Risk Material System")
st.markdown("### SMART ENGINEERING DECISION + FAILURE PREDICTION ENGINE")
st.divider()

# =========================
# INPUTS
# =========================
st.sidebar.header("📥 ENGINEERING INPUT PARAMETERS")

requirement = st.sidebar.selectbox(
    "Material Requirement",
    [
        "High Strength",
        "Lightweight",
        "Wear Resistance",
        "High Toughness",
        "Corrosion Resistance",
        "Thermal Resistance"
    ]
)

load = st.sidebar.number_input("Applied Load (kN)", 1.0, 10000.0, 500.0)

temperature = st.sidebar.slider(
    "Operating Temperature (°C)",
    0,
    1600,
    400
)

budget = st.sidebar.number_input(
    "Total Budget (₹)",
    100,
    500000,
    50000
)

environment = st.sidebar.selectbox(
    "Environment",
    [
        "Normal",
        "Industrial",
        "Marine",
        "Corrosive",
        "High Pressure"
    ]
)

yield_strength = st.sidebar.slider(
    "Yield Strength (MPa)",
    50,
    2000,
    250
)

tensile_strength = st.sidebar.slider(
    "Tensile Strength (MPa)",
    100,
    2500,
    400
)

hardness = st.sidebar.slider(
    "Hardness (HB)",
    50,
    1000,
    200
)

fatigue_resistance = st.sidebar.slider(
    "Fatigue Resistance (Million Cycles)",
    1,
    100,
    20
)

thermal_resistance = st.sidebar.slider(
    "Thermal Resistance Index",
    1,
    10,
    5
)

# =========================
# MATERIAL DATABASE
# =========================
materials = {

    "Lightweight": {

        "Aluminum 6061": (320, 300),
        "Aluminum 7075": (450, 350),
        "Magnesium AZ31": (600, 250),
        "Titanium Grade 2": (3200, 600),
        "Titanium Grade 5": (4500, 900),

        "Carbon Fiber Composite": (1500, 300),
        "Glass Fiber Composite": (2800, 250),
        "Kevlar Composite": (4200, 280),

        "ABS Plastic": (180, 100),
        "Polycarbonate": (250, 120)
    },

    "High Strength": {

        "AISI 4140 Alloy Steel": (450, 850),
        "AISI 4340 Alloy Steel": (550, 900),
        "EN24 Steel": (600, 950),
        "EN31 Steel": (650, 800),

        "Tool Steel D2": (1200, 1000),
        "Tool Steel H13": (1500, 1100),

        "Maraging Steel": (4000, 1200),

        "Nickel Alloy 625": (6500, 1100),
        "Nickel Alloy 718": (7000, 1200),

        "Chromium Steel": (850, 850),

        "Duplex Stainless Steel": (900, 950),
        "Super Duplex Steel": (1500, 1000)
    },

    "Wear Resistance": {

        "Tungsten Carbide": (7000, 1200),
        "Silicon Carbide": (5500, 1400),
        "Ceramic Composite": (6000, 1300),

        "Cobalt Alloy Stellite": (8000, 1200),

        "Hardened Tool Steel": (1400, 950),

        "Boron Carbide": (9000, 1500),

        "Inconel 625": (7500, 1200),
        "Inconel 718": (8200, 1250)
    },

    "High Toughness": {

        "Mild Steel IS2062": (150, 700),

        "Stainless Steel 304": (500, 850),
        "Stainless Steel 316": (650, 900),

        "Duplex Stainless Steel": (950, 950),

        "Nickel Titanium Alloy": (5000, 700),

        "Bronze Alloy": (850, 500),
        "Brass Alloy": (600, 450),

        "Copper Alloy C110": (750, 400),

        "Monel 400": (4500, 900)
    },

    "Corrosion Resistance": {

        "Stainless Steel 304": (500, 850),
        "Stainless Steel 316": (650, 900),

        "Duplex Stainless Steel": (1000, 950),

        "Titanium Grade 2": (3200, 600),
        "Titanium Grade 5": (4500, 900),

        "Inconel 625": (7500, 1200),

        "Monel 400": (4500, 900),

        "Copper Nickel Alloy": (2200, 500),

        "Hastelloy C276": (8500, 1250)
    },

    "Thermal Resistance": {

        "Inconel 718": (8500, 1250),
        "Inconel 625": (7800, 1200),

        "Molybdenum Alloy": (9000, 1500),

        "Tungsten Alloy": (10000, 1600),

        "Silicon Nitride": (6500, 1400),

        "Graphite Composite": (4200, 1000),

        "Hastelloy X": (9200, 1300),

        "Ceramic Matrix Composite": (9500, 1500)
    }
}

# =========================
# APPLICATIONS
# =========================
applications = {

    # LIGHTWEIGHT
    "Aluminum 6061": [
        "Car body panels",
        "Bike frames",
        "Window frames"
    ],

    "Aluminum 7075": [
        "Aircraft fittings",
        "Drone structures",
        "Sports equipment"
    ],

    "Magnesium AZ31": [
        "Laptop bodies",
        "Camera frames",
        "Portable devices"
    ],

    "Titanium Grade 2": [
        "Marine parts",
        "Medical implants",
        "Chemical tanks"
    ],

    "Titanium Grade 5": [
        "Aircraft parts",
        "Racing components",
        "Surgical implants"
    ],

    "Carbon Fiber Composite": [
        "Drone frames",
        "Sports rackets",
        "Vehicle panels"
    ],

    "Glass Fiber Composite": [
        "Boat panels",
        "Electrical covers",
        "Wind turbine blades"
    ],

    "Kevlar Composite": [
        "Bulletproof jackets",
        "Protective gloves",
        "Helmet layers"
    ],

    "ABS Plastic": [
        "Toy components",
        "3D printing",
        "Electronic housings"
    ],

    "Polycarbonate": [
        "Helmet visors",
        "Machine covers",
        "Safety shields"
    ],

    # HIGH STRENGTH
    "AISI 4140 Alloy Steel": [
        "Gears",
        "Shafts",
        "Automobile parts"
    ],

    "AISI 4340 Alloy Steel": [
        "Landing gears",
        "Heavy shafts",
        "Crankshafts"
    ],

    "EN24 Steel": [
        "Axles",
        "Gear systems",
        "Bolts"
    ],

    "EN31 Steel": [
        "Bearings",
        "Rollers",
        "Machine tools"
    ],

    "Tool Steel D2": [
        "Cutting dies",
        "Industrial cutters",
        "Punch tools"
    ],

    "Tool Steel H13": [
        "Forging dies",
        "Casting moulds",
        "Extrusion tools"
    ],

    "Maraging Steel": [
        "Rocket casings",
        "Defense equipment",
        "High stress shafts"
    ],

    "Nickel Alloy 625": [
        "Heat exchangers",
        "Chemical vessels",
        "Marine systems"
    ],

    "Nickel Alloy 718": [
        "Gas turbines",
        "Jet engine parts",
        "High temp bolts"
    ],

    "Chromium Steel": [
        "Bearings",
        "Industrial rollers",
        "Machine shafts"
    ],

    "Duplex Stainless Steel": [
        "Marine pipelines",
        "Chemical tanks",
        "Oil pipes"
    ],

    "Super Duplex Steel": [
        "Offshore structures",
        "Marine pumps",
        "Desalination plants"
    ],

    # WEAR RESISTANCE
    "Tungsten Carbide": [
        "Drill bits",
        "Mining tools",
        "Cutting tools"
    ],

    "Silicon Carbide": [
        "Grinding wheels",
        "Brake discs",
        "High temp linings"
    ],

    "Ceramic Composite": [
        "Heat shields",
        "Industrial liners",
        "Engine insulation"
    ],

    "Cobalt Alloy Stellite": [
        "Valve seats",
        "Cutting blades",
        "Turbine surfaces"
    ],

    "Hardened Tool Steel": [
        "Machine cutters",
        "Punches",
        "Industrial dies"
    ],

    "Boron Carbide": [
        "Armor plates",
        "Protective shields",
        "Abrasive nozzles"
    ],

    "Inconel 625": [
        "Gas pipes",
        "Exhaust systems",
        "Heat exchangers"
    ],

    "Inconel 718": [
        "Jet engines",
        "Turbines",
        "High heat bolts"
    ],

    # TOUGHNESS
    "Mild Steel IS2062": [
        "Building frames",
        "Bridges",
        "Fabrication work"
    ],

    "Stainless Steel 304": [
        "Kitchen equipment",
        "Pipelines",
        "Water tanks"
    ],

    "Stainless Steel 316": [
        "Marine fittings",
        "Food processing units",
        "Chemical containers"
    ],

    "Nickel Titanium Alloy": [
        "Medical stents",
        "Flexible devices",
        "Robotic joints"
    ],

    "Bronze Alloy": [
        "Bushings",
        "Bearings",
        "Marine fittings"
    ],

    "Brass Alloy": [
        "Pipe fittings",
        "Valves",
        "Musical instruments"
    ],

    "Copper Alloy C110": [
        "Electrical wires",
        "Switch contacts",
        "Heat exchangers"
    ],

    "Monel 400": [
        "Marine pumps",
        "Chemical tanks",
        "Saltwater valves"
    ],

    "Copper Nickel Alloy": [
        "Sea water pipes",
        "Condensers",
        "Marine systems"
    ],

    # THERMAL
    "Molybdenum Alloy": [
        "Furnace parts",
        "Aircraft components",
        "Heating systems"
    ],

    "Tungsten Alloy": [
        "Rocket nozzles",
        "High heat tools",
        "Furnace electrodes"
    ],

    "Silicon Nitride": [
        "Turbochargers",
        "Engine rotors",
        "Bearings"
    ],

    "Graphite Composite": [
        "Thermal shields",
        "Electrical brushes",
        "Heat systems"
    ],

    "Hastelloy C276": [
        "Acid pipelines",
        "Chemical reactors",
        "Industrial tanks"
    ],

    "Hastelloy X": [
        "Gas turbines",
        "Combustion chambers",
        "Heat exchangers"
    ],

    "Ceramic Matrix Composite": [
        "Thermal barriers",
        "Aircraft insulation",
        "High heat structures"
    ]
}

# =========================
# ENGINE
# =========================
def evaluate(req, temp, budget):

    candidates = materials[req]
    results = []

    for mat, (cost, tmax) in candidates.items():

        if cost <= budget:

            risk = (temp / tmax) * 100

            score = (100 - risk) - (cost / budget) * 50

            results.append((mat, cost, tmax, risk, score))

    results.sort(key=lambda x: x[4], reverse=True)

    return results

# =========================
# OUTPUT
# =========================
if st.button("RUN FAILURE RISK ANALYSIS ⚙️"):

    results = evaluate(requirement, temperature, budget)

    st.divider()

    st.subheader("ENGINEERING OUTPUT")

    if results:

        mat, cost, tmax, risk, score = results[0]

        st.success(f"""
SELECTED MATERIAL: {mat}
""")

        # FAILURE RISK
        st.markdown("### 🚨 FAILURE RISK ANALYSIS")

        if risk < 30:
            cls = "low"
            status = "LOW FAILURE RISK"

        elif risk < 60:
            cls = "medium"
            status = "MODERATE FAILURE RISK"

        else:
            cls = "high"
            status = "HIGH FAILURE RISK ⚠️"

        st.markdown(f"""
        <div class="risk-box {cls}">
        FAILURE RISK: {round(risk,2)}% <br>
        {status}
        </div>
        """, unsafe_allow_html=True)

        st.progress(min(int(risk), 100))

        # REASON
        st.write("### REASON")

        st.info(f"""
✔ Requirement: {requirement}

✔ Temperature: {temperature}°C vs limit {tmax}°C

✔ Cost: ₹{cost} within ₹{budget}

✔ Load: {load} kN

✔ Environment: {environment}

✔ Yield Strength: {yield_strength} MPa

✔ Tensile Strength: {tensile_strength} MPa

✔ Hardness: {hardness} HB

✔ Fatigue: {fatigue_resistance} million cycles

✔ Thermal: {thermal_resistance} index
        """)

        # RANKING
        st.write("### RANKING")

        for i, r in enumerate(results[:5], 1):

            st.write(
                f"{i}. {r[0]} | ₹{r[1]} | {r[2]}°C | Risk {round(r[3],2)}%"
            )

        # APPLICATIONS
        st.write("### APPLICATIONS")

        for app in applications.get(mat, ["Basic engineering use"]):

            st.write("✔ " + app)

        # MAX KG
        st.metric(
            "MAX KG YOU CAN BUY",
            round(budget / cost, 2)
        )

    else:

        st.error("NO MATERIAL FOUND")