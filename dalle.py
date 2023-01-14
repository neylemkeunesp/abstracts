import requests

def generate_image(prompt):
  api_key = "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"
  model = "image-alpha-001"
  data = {
    "prompt": prompt,
    "num_images":1,
    "size":"512x512",
    "response_format":"url"
  }
  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
  }
  r = requests.post(f"https://api.openai.com/v1/images/generations", json=data, headers=headers)
  if r.status_code == 200:
    response_text = r.json()
    return response_text['data'][0]['url']
  else:
    print("Failed to generate image")

prompt = "Generate an image of a person riding a bicycle on a beach"
image_url = generate_image(prompt)
print(image_url)