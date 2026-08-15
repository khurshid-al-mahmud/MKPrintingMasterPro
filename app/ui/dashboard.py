import streamlit as st

st.set_page_config(
    page_title="MK Graphics ERP",
    page_icon="🖨️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
        html, body, [data-testid="stAppViewContainer"] {
            margin: 0;
            padding: 0;
        }

        [data-testid="stHeader"] {
            display: none;
        }

        [data-testid="stToolbar"] {
            display: none;
        }

        [data-testid="stSidebar"] {
            display: none;
        }

        .block-container {
            max-width: 100%;
            padding: 0;
            margin: 0;
        }

        .mk-clean-reset {
            min-height: 100vh;
            width: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
            background: #f5f7fa;
            font-family: Arial, sans-serif;
        }

        .mk-clean-reset-inner {
            text-align: center;
            padding: 48px;
        }

        .mk-clean-reset-title {
            font-size: 32px;
            font-weight: 800;
            color: #111827;
            margin-bottom: 12px;
        }

        .mk-clean-reset-subtitle {
            font-size: 15px;
            color: #6b7280;
        }
    </style>

    <div class="mk-clean-reset">
        <div class="mk-clean-reset-inner">
            <div class="mk-clean-reset-title">
                MK Graphics ERP
            </div>
            <div class="mk-clean-reset-subtitle">
                Clean Homepage Foundation — STEP-68
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)
