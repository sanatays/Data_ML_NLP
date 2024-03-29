# import pandas as pd
# import requests

# import streamlit as st

# text = st.text_input(label = "Enter your question : ")
# res = requests.get("https://app-api-imlp5.herokuapp.com/api/text=" + ''.join(text))

# res = pd.read_json(res.content.decode('utf-8')).loc[0, 'tags']

# st.write(res)

import requests
import pandas as pd
import streamlit as st

text = st.text_input(label="Enter your question:")

if text:
    res = requests.get("https://app-api-imlp5.herokuapp.com/api/text=" + ''.join(text))

    if res.status_code == 200:
        res = pd.read_json(res.content.decode('utf-8'), orient='records').loc[0, 'tags']
        st.write(res)
    else:
        st.write("Error: Unable to fetch data from the API.")
else:
    st.write("Please enter a question.")