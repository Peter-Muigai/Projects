import requests

image_url = "https://google.com/image.jpg"
save_as = "downloaded_image.jpg"

response = requests.get(image_url)

if response.status_code == 200:
    with open(save_as, "wb") as f:
        f.write(response.content)
    print("Image downloaded successfully")
else:
    print("Failed to download image")