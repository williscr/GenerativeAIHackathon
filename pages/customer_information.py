import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json

with open('data/ACME_all_files.json') as f:
    data = json.load(f)

# Display company info
st.header("Company Information")
for key, value in data["files"][0]["company_info"].items():
    if key == 'business_information':
        for key2, value2 in data["files"][0]["company_info"]['business_information'].items():
            if key2 == 'partners':
                for partner in data["files"][0]["company_info"]['business_information']['partners']:
                    for key3, value3 in partner.items():
                        st.write(f"""{' '.join(key3.split("_")).title()} : {value3}""")
    elif key == 'business_plan':
        for key4, value4 in data["files"][0]["company_info"]['business_plan'].items():
            if key4 == 'financial_projections':
                st.write("Financial Projections can be seen in below table.")
                st.table(data["files"][0]["company_info"]['business_plan']['financial_projections'])
            else:
                st.write(f"""{' '.join(key4.split("_")).title()} : {value4}""")
    else:
        st.write(f"""{' '.join(key.split("_")).title()} : {value}""")
st.write("")


# Display balance sheet chart
yearly_summary = data["files"][1]["balance_sheet"]["yearly_summary"]
years = list(yearly_summary.keys())
assets = [sum([yearly_summary[year]["assets"][asset] for year in years]) for asset in yearly_summary[years[0]]["assets"]]
liabilities = [sum([yearly_summary[year]["liabilities"][liability] for year in years]) for liability in yearly_summary[years[0]]["liabilities"]]
equity = [yearly_summary[year]["equity"] for year in years]


def get_balance_sheet_data(year):
    return data['files'][1]['balance_sheet']['yearly_summary'][year]

def plot_balance_sheet(year):
    balance_sheet_data = get_balance_sheet_data(year)
    df = pd.DataFrame(balance_sheet_data)
    df = df[['assets', 'liabilities', 'equity']]
    st.bar_chart(df)

#st.set_page_config(page_title='Balance Sheet Chart')
st.title('Balance Sheet Chart')

year = st.slider('Select year', 2017, 2022)
plot_balance_sheet(str(year))



# progress_bar.empty()

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")