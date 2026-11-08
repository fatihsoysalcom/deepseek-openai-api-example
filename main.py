import os
import requests
import json

# This script demonstrates how to use the DeepSeek API with an OpenAI-compatible endpoint.
# It assumes you have an OpenAI-compatible API endpoint running and accessible.

# --- Configuration ---
# Replace with your actual API endpoint URL
# Example: "http://localhost:8000/v1"
API_BASE_URL = os.environ.get("DEEPSEEK_API_URL", "YOUR_API_BASE_URL_HERE")

# Replace with your actual API key if required by your endpoint
# If your endpoint doesn't require an API key, you can set this to "None" or an empty string.
API_KEY = os.environ.get("DEEPSEEK_API_KEY", "YOUR_API_KEY_HERE")

# The model name as exposed by your OpenAI-compatible API
# This might be "deepseek-coder" or a similar identifier.
MODEL_NAME = os.environ.get("DEEPSEEK_MODEL_NAME", "YOUR_MODEL_NAME_HERE")

# --- API Call Function ---
def call_deepseek_api(prompt):
    """Sends a prompt to the DeepSeek API and returns the response."""
    if API_BASE_URL == "YOUR_API_BASE_URL_HERE":
        print("Error: Please set the DEEPSEEK_API_URL environment variable or update the script.")
        return None
    if MODEL_NAME == "YOUR_MODEL_NAME_HERE":
        print("Error: Please set the DEEPSEEK_MODEL_NAME environment variable or update the script.")
        return None

    headers = {
        "Content-Type": "application/json",
    }
    if API_KEY and API_KEY != "YOUR_API_KEY_HERE":
        headers["Authorization"] = f"Bearer {API_KEY}"

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 150,
        "temperature": 0.7,
    }

    try:
        response = requests.post(f"{API_BASE_URL}/chat/completions", headers=headers, json=payload)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")
        return None

# --- Main Execution ---
if __name__ == "__main__":
    user_prompt = "Explain the concept of a large language model in simple terms."
    print(f"Sending prompt: '{user_prompt}' to {API_BASE_URL}...")

    api_response = call_deepseek_api(user_prompt)

    if api_response and 'choices' in api_response and api_response['choices']:
        # Extract and print the assistant's reply
        assistant_reply = api_response['choices'][0]['message']['content']
        print("\n--- DeepSeek Response ---")
        print(assistant_reply)
    elif api_response:
        print("\nAPI returned an empty or unexpected response.")
        print(json.dumps(api_response, indent=2))
    else:
        print("\nFailed to get a response from the API.")
