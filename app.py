import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="PickModelAI.com — AI Advisory & Architecture",
    page_icon="🤖",
    layout="wide"
)

# Hero Section
st.title("PickModelAI.com")
st.subheader("Eliminate Analysis Paralysis in LLM Integration")
st.markdown("""
Welcome to **PickModelAI**, a productized, human-led AI advisory service. We deliver rapid-turnaround 
strategic architecture, financial blueprints, and custom tech stacks for startup founders and businesses.
""")

st.divider()

# Service Tiers Overview
st.header("Our Service Tiers")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🆓 Free Tier")
    st.markdown("**Price:** $0")
    st.markdown("500-word idea intake, competitor lookup, and a structured 3-option tech stack comparison (OpenAI vs. Anthropic vs. Hugging Face).")

with col2:
    st.markdown("### 🛠️ DIY Blueprint")
    st.markdown("**Price:** $50")
    st.markdown("Step-by-step guidance on building your idea using LangChain, LangGraph, and AWS integration steps with estimated costs.")

with col3:
    st.markdown("### 🚀 Enterprise Sprint")
    st.markdown("**Price:** $1,000")
    st.markdown("Comprehensive architectural blueprint, team sizing, specialized roles, milestone timelines, and operational expense modeling.")

st.divider()

# Interactive Free Tier Intake Demo
st.header("Try the Free Tier Idea Intake")
st.markdown("Enter your product concept below to see how our structured intake works:")

user_idea = st.text_area("Describe your AI product or business idea:", placeholder="e.g., A legal document summarizer using RAG...")

if st.button("Generate Tech Stack Comparison"):
    if user_idea.strip():
        st.success("Analysis Complete!")
        st.subheader("Recommended Architecture Options")
        
        tab1, tab2, tab3 = st.tabs(["Option A: OpenAI API", "Option B: Anthropic Claude", "Option C: Open Source (Hugging Face)"])
        
        with tab1:
            st.markdown("**Primary Model:** `gpt-4o`")
            st.markdown("**Pros:** Fastest integration, robust structured output (Pydantic support), excellent reasoning.")
            st.markdown("**Cons:** Higher recurring token costs at scale.")
            st.markdown("**Estimated Token Cost:** ~$0.03 per 1k tokens")
            
        with tab2:
            st.markdown("**Primary Model:** `claude-3-5-sonnet`")
            st.markdown("**Pros:** Exceptional nuance in long-form text generation and code generation.")
            st.markdown("**Cons:** Strict rate limits on lower tiers.")
            st.markdown("**Estimated Token Cost:** ~$0.015 per 1k tokens")
            
        with tab3:
            st.markdown("**Primary Model:** `Llama-3-70B-Instruct`")
            st.markdown("**Pros:** Full data privacy, zero recurring API usage fees if self-hosted.")
            st.markdown("**Cons:** Requires heavy cloud GPU hosting (AWS EC2 / RunPod).")
            st.markdown("**Estimated Token Cost:** Fixed GPU instance cost (~$200/mo)")
    else:
        st.warning("Please enter a product idea first.")
