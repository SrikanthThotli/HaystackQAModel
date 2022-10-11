import os

import spacy
#from flask import Flask, render_template, jsonify, request
import streamlit as st
from components import BingSearch

#app = Flask(__name__)
# subscription key
bing_subscription_key = "adca0bb823d44e98a1f14c3c185d7934"

bingSearch = BingSearch(bing_subscription_key)


#@app.route('/')
def welcome():
    return "Welcome all"


def main():
    st.title ("Bing Search API Question and Answer Model")
    html_temp = """
    <h3>Bing Search API Question and Answer Model</h3>
    """
    st. markdown(html_temp,unsafe_allow_html=True)
    question = st.text_input("Question","Type your question here...")
    result = ""
    if st.button("Submit"):
        result = bingSearch.getAnswer(str(question))
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets Learn")
        st.text("Built with Streamlit")

if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=5000)
	main()