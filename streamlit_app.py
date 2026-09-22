import streamlit as st
from datetime import datetime

# ---------------------------------------------------------
# IMAD INTELLIGENCE SERVICES — CONTROL ROOM V1
# ---------------------------------------------------------

st.set_page_config(
    page_title="IMAD Intelligence Services | Control Room",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

st.title("🧠 IMAD INTELLIGENCE SERVICES")
st.subheader("CONTROL ROOM")

st.caption(
    "Integrated Market & Development Intelligence — "
    "AI-assisted Construction & Project Intelligence"
)

st.divider()

# ---------------------------------------------------------
# SIDEBAR — RESEARCH CONTROL
# ---------------------------------------------------------

with st.sidebar:
    st.header("🎯 Research Control")

    project_name = st.text_input(
        "Project / Company / Opportunity",
        placeholder="e.g. Hyderabad H-CITI"
    )

    research_type = st.selectbox(
        "Intelligence Type",
        [
            "Construction Intelligence",
            "Company Intelligence",
            "Project Intelligence",
            "Opportunity Intelligence",
            "Subcontractor / Vendor Intelligence",
            "Custom Research",
        ],
    )

    priority = st.selectbox(
        "Priority",
        ["Normal", "High", "Critical"]
    )

    st.divider()

    st.subheader("Research Rule")

    st.info(
        "Before deep research, check whether a comparable "
        "intelligence report already exists publicly."
    )

    start_research = st.button(
        "🚀 START RESEARCH",
        use_container_width=True,
        type="primary",
    )

# ---------------------------------------------------------
# MAIN RESEARCH PROMPT
# ---------------------------------------------------------

st.header("🔎 Research Workspace")

research_prompt = st.text_area(
    "Research Prompt",
    height=140,
    placeholder=(
        "Describe exactly what intelligence you want.\n\n"
        "Example:\n"
        "Identify the Architect → Consultant → Contractor → "
        "Developer/Client relationships for this project, "
        "then identify verified subcontractor/vendor relationships."
    ),
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Research Status", "READY")

with col2:
    st.metric("AI Agents", "4")

with col3:
    st.metric("Information Gaps", "0")

st.divider()

# ---------------------------------------------------------
# AGENT CONTROL
# ---------------------------------------------------------

st.header("🤖 AI Agent Control Room")

agent_cols = st.columns(4)

agents = [
    ("Agent 01", "Discovery", "Public-source discovery"),
    ("Agent 02", "Verification", "Cross-check & evidence"),
    ("Agent 03", "Relationship", "Network mapping"),
    ("Agent 04", "Challenge", "Challenge assumptions"),
]

for col, (agent_id, role, description) in zip(agent_cols, agents):
    with col:
        st.container(border=True)
        st.subheader(f"🟢 {agent_id}")
        st.write(f"**{role}**")
        st.caption(description)
        st.write("Status: **READY**")

st.divider()

# ---------------------------------------------------------
# INFORMATION GAP FRAMEWORK
# ---------------------------------------------------------

st.header("🕳️ Information Gap → IMAD Closure")

st.caption(
    "Every major intelligence finding should preserve a traceable "
    "chain from information gap to verified closure."
)

gap_cols = st.columns(4)

gap_status = [
    ("OPEN", "Information not yet established"),
    ("PARTIALLY CLOSED", "Some evidence available"),
    ("CLOSED", "Evidence independently verified"),
    ("UNKNOWN", "Requires further investigation"),
]

for col, (status, description) in zip(gap_cols, gap_status):
    with col:
        st.metric(status, "0")
        st.caption(description)

st.divider()

# ---------------------------------------------------------
# FINDINGS / EVIDENCE
# ---------------------------------------------------------

st.header("📊 Intelligence Findings")

finding_cols = st.columns([1, 2, 2, 1, 1])

headers = [
    "Finding",
    "Evidence",
    "Source",
    "Verification",
    "Gap Status",
]

for col, header in zip(finding_cols, headers):
    with col:
        st.markdown(f"**{header}**")

st.info(
    "No findings yet. Start a research task to populate the "
    "intelligence workspace."
)

st.divider()

# ---------------------------------------------------------
# RELATIONSHIP MAP
# ---------------------------------------------------------

st.header("🔗 Relationship Intelligence")

relationship_cols = st.columns(5)

relationship_nodes = [
    "🏛️ Architect",
    "📐 Consultant",
    "🏗️ Contractor",
    "🔧 Specialist / Sub",
    "🏢 Developer / Client",
]

for col, node in zip(relationship_cols, relationship_nodes):
    with col:
        st.container(border=True)
        st.markdown(f"### {node}")
        st.caption("No verified relationship yet")

st.divider()

# ---------------------------------------------------------
# RESEARCH LOG
# ---------------------------------------------------------

st.header("📜 Research Log")

if start_research:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if not project_name:
        st.warning("Please enter a Project / Company / Opportunity.")
    elif not research_prompt:
        st.warning("Please enter a Research Prompt.")
    else:
        st.success(
            f"Research task created for **{project_name}**"
        )

        st.write(f"**Type:** {research_type}")
        st.write(f"**Priority:** {priority}")
        st.write(f"**Created:** {timestamp}")

        st.info(
            "V1 Control Room is ready. AI agent execution will be "
            "connected in the next development phase."
        )
else:
    st.caption("No research task started.")

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.divider()

st.caption(
    "IMAD Intelligence Services | Integrated Market & Development Intelligence"
)

st.caption(
    "V1 — Control Room Foundation"
)
