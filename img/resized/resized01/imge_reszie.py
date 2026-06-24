import os
from PIL import Image

def resize_images():
  """Resizes all images in the current directory and saves them to a new directory called 'resized'."""

  # Create a new directory called 'resized' if it doesn't exist already.
  if not os.path.exists('resized01'):
    os.mkdir('resized01')

  # Iterate over all the files in the current directory.
  for filename in os.listdir('.'):
    # Only resize image files.
    if filename.endswith('.jpg') or filename.endswith('.jpeg'):
      # Open the image file in read mode.
      image = Image.open(filename)

      # Resize the image to 200x200 pixels.
      image = image.resize((800, 1000))

      # Save the resized image to the 'resized' directory.
      image.save(os.path.join('resized', filename))

if __name__ == '__main__':
  resize_images()
