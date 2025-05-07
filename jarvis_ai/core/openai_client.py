import google.generativeai as gemini

# Set your Gemini API key
gemini.configure(api_key="your_gemini_api_key_here")

# Function to get a response from the Gemini model
def get_response_from_ai(user_input):
    try:
        # Making a request to Gemini's chat model
        response = gemini.generate_text(
            model="models/text-bison-001",  # Use the correct Gemini model name
            prompt=user_input,
            temperature=0.7,
            max_output_tokens=100,
        )
        # Extract and return the response text
        return response['candidates'][0]['output'].strip()
    except Exception as e:
        return f"Sorry, I couldn't get an answer. Error: {str(e)}"
