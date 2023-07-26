# import pandas as pd
# import requests

# import streamlit as st

# text = st.text_input(label = "Enter your question : ")
# res = requests.get("https://app-api-imlp5.herokuapp.com/api/text=" + ''.join(text))

# res = pd.read_json(res.content.decode('utf-8')).loc[0, 'tags']

# st.write(res)

import pandas as pd
import requests

import streamlit as st

st.title("My Streamlit Application")

try:
    user_input = st.text_input(label="Enter your question:")

    if not user_input:
        raise ValueError("Text cannot be empty")

    api_url = "http://127.0.0.1:5000/api/text=" + user_input

    response = requests.get(api_url)

    if response.ok:
	    data = response.json()
	    tags = data["tags"]
	    tag_names = [tag.strip("#") for tag in tags]
	    st.write("Tags:", ", ".join(tag_names))
    else:
        raise ValueError("API request failed")

except ValueError as e:
    st.error(str(e))