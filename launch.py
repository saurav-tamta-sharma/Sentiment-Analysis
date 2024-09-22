import joblib
import streamlit as st 

# Load model and vectorizer
model = joblib.load('sentiment_model.pkl')
tfidf = joblib.load('tfidf_vectorizer.pkl')

st.title("Sentiment Analysis")
st.markdown("### Enter a text to analyze its sentiment (e.g., product reviews, social media posts).")

# User input
user_input = st.text_area('Enter your text here:', height=150)

# Button to analyze sentiment
if st.button("Analyze Sentiment"):
    if user_input:
        # Transform the input text
        input_tfidf = tfidf.transform([user_input])
        sentiment = model.predict(input_tfidf)
        
        #displaying content
        st.success(f"Predicted Sentiment: **{sentiment[0]}**")

        if sentiment[0] == 'negative':
            st.text('👎🏻👎🏻👎🏻')
        else:
            st.text('👍🏻👍🏻👍🏻')
    else:
        st.warning("Please enter some text to analyze.")

