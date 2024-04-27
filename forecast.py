import streamlit as st
import time
import random
from flask import Flask, jsonify

# Initialize Flask app
app = Flask(__name__)

# Function to generate random number between 1 and 100
def generate_random_number():
    return random.randint(1, 100)

# API endpoint to get random number
@app.route('/api/random_number', methods=['GET'])
def get_random_number():
    random_num = generate_random_number()
    return jsonify({'random_number': random_num})

# Streamlit app title
st.title("Random Number Generator")

# Streamlit UI
st.write("Random Number:")

# Placeholder for displaying random number
output_placeholder = st.empty()

# Streamlit loop to continuously update the random number
while True:
    random_num = generate_random_number()
    output_placeholder.text(random_num)
    time.sleep(2)

# Run the Flask app
if __name__ == '__main__':
    app.run()
