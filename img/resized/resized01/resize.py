from PIL import Image

def resize_images(images, target_size):
    resized_images = []
    for img_path in images:
        image = Image.open(img_path)
        resized_image = image.resize(target_size)
        resized_images.append(resized_image)
    return resized_images

# Example usage
image_files = ['img-0104.jpeg']  # List of image file paths
target_size = (800, 10	00)  # Target size for resizing

resized_images = resize_images(image_files, target_size)

# Saving the resized images
for i, image in enumerate(resized_images):
    image.save(f"resized_image{i+1}.jpg")
