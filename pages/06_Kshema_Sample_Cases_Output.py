import streamlit as st

# Set page title
st.set_page_config(page_title="Kshema Sample Cases Output", layout="wide")

# Display the title
st.title("Kshema Sample Cases Output")

# Google Sheets embed link
sheets_url = "https://docs.google.com/spreadsheets/d/1D9sg4bz9h-LYKUXhoKwX8TfPsfUkH9wi08ga2vUZ8Y0/edit?usp=sharing"

# Display the Google Sheets document in an iframe
st.markdown(f'<iframe src="{sheets_url}/viewform?embedded=true" width="100%" height="600" frameborder="0" marginheight="0" marginwidth="0">Loading...</iframe>', unsafe_allow_html=True)

# Add a direct link to the sheet
st.markdown(f"[Open Google Sheets Document]({sheets_url})")

# Optional: Add some context or instructions

# Optional: Add a footer
st.markdown("---")
