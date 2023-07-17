from PIL import Image

def extract_metadata(image_path):
    try:
        with Image.open(image_path) as img:
            # Extract metadata
            metadata = img.info

            # Print metadata
            for key, value in metadata.items():
                print(f"{key}: {value}")
    except FileNotFoundError:
        print("Image file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Provide the path to your image file
image_path = "static/reels/2023-06-22_09-57-15_UTC.jpg"
extract_metadata(image_path)

import exifread

def extract_metadata(image_path):
    try:
        with open(image_path, 'rb') as file:
            tags = exifread.process_file(file)

            # Print EXIF metadata
            for tag, value in tags.items():
                if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
                    print(f"{tag}: {value}")
    except FileNotFoundError:
        print("Image file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Provide the path to your image file
image_path = "static/reels/2023-06-22_09-57-15_UTC.jpg"
print(extract_metadata(image_path))

