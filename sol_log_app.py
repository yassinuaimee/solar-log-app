import streamlit as st
import requests
import pandas as pd

def fetch_and_save_table(auth_key):
    url = "https://agrola.enerest.world/api/error-detection/errors/fleets/1ee839c2-341d-6178-89a4-4385f83513e4/plants/overview"
    headers = {"Authorization": f"Bearer {auth_key}"}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        df.to_excel("Suisse_Romande_YA.xlsx", index=False)
        return "File saved successfully: Suisse_Romande_YA.xlsx"
    else:
        return f"Error: {response.status_code}"

st.title("Fetch and Save Table")
st.write("Input the Authorization Key to fetch the latest table.")

auth_key = st.text_input("Authorization Key", type="password")

if st.button("Run Script"):
    if auth_key:
        result = fetch_and_save_table(auth_key)
        st.write(result)
        with open("Suisse_Romande_YA.xlsx", "rb") as file:
            st.download_button(
                label="Download Excel File",
                data=file,
                file_name="Suisse_Romande_YA.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
    else:
        st.warning("Please enter the Authorization Key.")
