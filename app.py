import os

import spacy
import streamlit as st
from components import BingSearch

# subscription key
bing_subscription_key = "adca0bb823d44e98a1f14c3c185d7934"
bingSearch = BingSearch(bing_subscription_key)

def welcome():
    return "Welcome all"

@st.cache(allow_output_mutation = True)
def get_model(self):
    reader_bert = FARMReader(model_name_or_path="distilbert-base-uncased-distilled-squad", use_gpu=True)
    return reader_bert

def main():
    st.title ("Bing Search API QA Model")
    html_temp = """
    <h3>Ask me anything</h3>
    """
    st. markdown(html_temp,unsafe_allow_html=True)
    question = st.text_input("Question","")
    result = ""
    reader_bert = get_model()
    if st.button("Submit"):
        result = bingSearch.getAnswer(str(question),reader_bert)
    st.success('{}'.format(result))
    if st.button("About"):
        st.text("Lets Learn")
        st.text("Built with Streamlit")

if __name__ == '__main__':
	main()