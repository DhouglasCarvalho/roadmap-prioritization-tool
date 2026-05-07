import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Roadmap Prioritization Tool",
    page_icon="📊",
    layout="wide"
)

st.title("Roadmap Prioritization Tool")
st.write(
    "A product management decision-support tool that ranks features based on "
    "impact, effort, confidence, risk, and strategic alignment."
)

# Load feature data
features = pd.read_csv("data/features.csv")

st.subheader("Input Feature Data")
st.dataframe(features, use_container_width=True)

# Calculate priority score
features["Priority_Score"] = (
    features["Impact"] * features["Confidence"] * features["Strategic_Alignment"]
) / (features["Effort"] + features["Risk"])

features["Priority_Score"] = features["Priority_Score"].round(2)

# Create recommendation labels
def get_recommendation(score):
    if score >= 75:
        return "Prioritize"
    elif score >= 50:
        return "Evaluate"
    else:
        return "Defer"

features["Recommendation"] = features["Priority_Score"].apply(get_recommendation)

# Add rank
features = features.sort_values(by="Priority_Score", ascending=False)
features.insert(0, "Rank", range(1, len(features) + 1))

st.subheader("Prioritized Roadmap")
st.dataframe(
    features[
        [
            "Rank",
            "Feature",
            "Impact",
            "Effort",
            "Confidence",
            "Risk",
            "Strategic_Alignment",
            "Priority_Score",
            "Recommendation"
        ]
    ],
    use_container_width=True
)

st.subheader("Executive Summary")

total_features = len(features)
prioritize_count = len(features[features["Recommendation"] == "Prioritize"])
evaluate_count = len(features[features["Recommendation"] == "Evaluate"])
defer_count = len(features[features["Recommendation"] == "Defer"])

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Features", total_features)
col2.metric("Prioritize", prioritize_count)
col3.metric("Evaluate", evaluate_count)
col4.metric("Defer", defer_count)

st.subheader("Top Recommendation")

top_feature = features.iloc[0]

st.success(
    f"Highest priority: {top_feature['Feature']} "
    f"with a score of {top_feature['Priority_Score']}."
)

st.subheader("Scoring Model")

st.code(
    "Priority Score = (Impact × Confidence × Strategic Alignment) / (Effort + Risk)",
    language="text"
)