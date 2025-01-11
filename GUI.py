import streamlit as st

def apply_theme():
    """
    Applies a selected theme to the Streamlit app with refined and extensive CSS injection.
    """
    themes = {
        "Light": {"primary": "#4CAF50", "background": "#ffffff", "text": "#000000"},
        "Dark": {"primary": "#1E1E1E", "background": "#333333", "text": "#ffffff"},
        "Blue": {"primary": "#2196F3", "background": "#E3F2FD", "text": "#000000"},
    }

    # Sidebar UI for theme selection
    st.sidebar.title("Customize UI")
    selected_theme = st.sidebar.selectbox("Choose Theme", list(themes.keys()))
    theme = themes[selected_theme]

    # Apply custom CSS to multiple components
    st.markdown(
        f"""
        <style>
        /* Global body styling */
        body {{
            background-color: {theme['background']};
            color: {theme['text']};
            font-family: 'Arial', sans-serif;
        }}

        /* Customize Streamlit's header */
        header {{
            background-color: {theme['primary']};
            color: {theme['text']};
        }}

        /* Sidebar customization */
        section[data-testid="stSidebar"] {{
            background-color: {theme['primary']};
            color: {theme['text']};
        }}
        section[data-testid="stSidebar"] .css-1d391kg {{
            color: {theme['text']};
        }}

        /* Buttons styling */
        div.stButton > button {{
            background-color: {theme['primary']};
            color: {theme['text']};
            border: none;
            padding: 10px;
            border-radius: 5px;
            font-weight: bold;
        }}
        div.stButton > button:hover {{
            background-color: {theme['text']};
            color: {theme['primary']};
        }}

        /* Table styling */
        div[data-testid="stDataFrame"] {{
            background-color: {theme['background']};
            border: 1px solid {theme['primary']};
        }}
        div[data-testid="stDataFrame"] table {{
            color: {theme['text']};
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

    return theme
