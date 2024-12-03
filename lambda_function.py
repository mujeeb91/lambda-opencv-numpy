import base64
import cv2
import json
import numpy as np
import os


def process_image(base64_image):
    # Decode the Base64 image
    image_data = base64.b64decode(base64_image)
    # Convert it into a NumPy array
    np_array = np.frombuffer(image_data, np.uint8)
    # Decode the image using OpenCV
    img = cv2.imdecode(np_array, cv2.IMREAD_COLOR)

    # Convert the image to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Encode the processed image back to Base64
    _, buffer = cv2.imencode('.jpg', gray_img)
    base64_gray = base64.b64encode(buffer).decode("utf-8")

    return base64_gray

def lambda_handler(event, context):
    # Extract the Authorization header
    headers = event.get("headers", {})
    auth_header = headers.get("authorization")

    # Validate the token (replace with your logic)
    valid_token = f'Bearer {os.environ.get("AUTH_TOKEN")}'
    if auth_header != valid_token:
        return {
            "statusCode": 401,
            "body": json.dumps({"message": "Unauthorized"})
        }
    
    # Extract Base64 image data from the payload
    base64_images = json.loads(event.get("body", '{}')).get('images')
    if not base64_images:
        return {
            "statusCode": 400,
            "body": "No images provided"
        }

    processed_images = []
    for base64_image in base64_images:
        processed_images.append(process_image(base64_image))

    return {
        "statusCode": 200,
        "body": {
            "message": "Image(s) processed successfully",
            "images": processed_images,
        }
    }
