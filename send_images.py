import base64
import requests


image_paths = [
    'character.png',
]

base64_images = []
for image_path in image_paths:
    with open(image_path, "rb") as img_file:
        # Read and encode the image
        base64_string = base64.b64encode(img_file.read()).decode("utf-8")
        base64_images.append(base64_string)

# Prepare the payload
body = {
    "images": base64_images,
    "other_data": "optional information"
}

url = 'https://facskwv2mcrkzobwdfmcycok440ifdmf.lambda-url.ca-central-1.on.aws/'
headers = {
    'Authorization': 'Bearer ZMIje2ZLkXhsi21b04pKHzIobxEQRG3SiuVwyj3izu84GQKsuE74dtiOtIIdXpMY'
}
response = requests.post(url, json=body, headers=headers)
print(response.__dict__)
response_data = response.json()
print(response_data)

if "images" in response_data:
    processed_images = response_data["images"]
    for idx, base64_image in enumerate(processed_images):
        # Save the processed images
        with open(f'output_{idx + 1}.jpg', "wb") as img_file:
            img_file.write(base64.b64decode(base64_image))
else:
    print('no processed images')