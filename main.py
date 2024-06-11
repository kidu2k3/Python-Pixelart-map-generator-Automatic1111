import requests
import json
import base64

# Function to generate a custom map based on user input
def generate_custom_map(api_url, api_key, prompt, width, height):
    data = {
        "prompt": prompt,
        "width": width,
        "height": height,
        "num_inference_steps": 50
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    response = requests.post(f"{api_url}/sdapi/v1/txt2img", headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        result = response.json()
        image_base64 = result['images'][0]
        return base64.b64decode(image_base64)
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")

# Main function
def main():
    api_url = "http://127.0.0.1:7860"  # Update if your Automatic1111 instance is running on a different address
    api_key = "your_api_key_here"  # Replace with your actual API key

    width = 1920  # Full HD width
    height = 1080  # Full HD height

    # Generate a custom map based on user input
    custom_prompt = input("Enter a custom prompt for the map (e.g., 'pixel art game map with landscapes, mountains, seaside, ports, castles, cartoonish style'): ")
    custom_map = generate_custom_map(api_url, api_key, custom_prompt, width, height)
    with open("custom_map.png", "wb") as f:
        f.write(custom_map)

    print("Map generated and saved as 'custom_map.png'")

if __name__ == "__main__":
    main()
