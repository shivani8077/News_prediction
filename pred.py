import streamlit as st
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.naive_bayes import MultinomialNB
import pickle

# Load trained model and vectorizer (these need to be saved beforehand)
model = pickle.load(open("pred_model.pk1", "rb"))
vectorizer = pickle.load(open("Count_Vectorizer.pk1", "rb"))

# Streamlit UI
st.title("News Classification App")
st.write("Enter the news content below to check if it's REAL or FAKE.")

# User input
user_input = st.text_area("News Content", height=200)

# Predict
if st.button("Classify"):
    if user_input.strip():
        # Transform the input text
        input_vector = vectorizer.transform([user_input])
        prediction = model.predict(input_vector)[0]
        if prediction==0:
                st.error("This is a FAKE News")
        else:
                st.success("This is a REAL News")
    else:
        st.error("Please enter some News content to classify.")
