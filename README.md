# Streamlit CV

This project provides a CV viewer built with [Streamlit](https://streamlit.io/).

## Setup

1. Ensure Python 3.8 or newer is installed.
2. Install the required packages:
   ```bash
   pip install streamlit PyYAML
   ```
3. Run the application:
   ```bash
   streamlit run app.py
   ```

## Editing your CV

All data is stored in YAML format inside the `data/` directory. Edit
`data/cv.yaml` to update experience, education, skills, achievements and
contact information. Refresh the running Streamlit page to see changes.
