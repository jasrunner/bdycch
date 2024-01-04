from PIL import Image
import pytesseract
import cv2
import numpy as np

from constants import meal_types, time_symbol


# ----------------------------------------------------------------------------
def capture_text_and_cropped_image(image_path):
    # Open the image using Pillow
    original_image = Image.open(image_path)

    # Use pytesseract to extract text from the image
    text = pytesseract.image_to_string(original_image)


    # Convert the Pillow image to a NumPy array for OpenCV processing
    image_np = np.array(original_image)

    # Replace 'path/to/your/sub_image.png' with the actual path to your sub-image file
    # sub_image_path = 'path/to/your/sub_image.png'
    sub_image = cv2.imread(image_path)

    # Match the sub-image in the original image using template matching
    result = cv2.matchTemplate(image_np, sub_image, cv2.TM_CCOEFF_NORMED)
    _, _, _, max_loc = cv2.minMaxLoc(result)

    # Extract the top 40% of the sub-image vertically
    h, w, _ = sub_image.shape
    top_45_percent = int(h * 0.45)
    sub_image_region = original_image.crop((max_loc[0], max_loc[1], max_loc[0] + w, max_loc[1] + top_45_percent))

    return text, sub_image_region


# ----------------------------------------------------------------------------
# get meal type
def get_meal_type(text_in) :
    # lets get the meal type from the captured text
    meal_type = ""

    for meal_type in meal_types:
        if meal_type in text_in:
            meal_type = meal_type
            return meal_type

    return meal_type  


# ----------------------------------------------------------------------------
# extract all text from after "General Meal" or "Refuel Meal" and before the time symbol
def get_title(text_in, meal_type) :
    
    title = text_in.split(meal_type)[1].strip()
    # strip everything after the time symbol
    title = title.split(time_symbol)[0].strip()
    # remove line returns
    title = title.replace("\n", " ")

    return title


# ----------------------------------------------------------------------------
# get the new image filename
def get_new_image_filename(image_path, title) :

    # separate the path and the filename
    filename = image_path.split("/")[-1]

    path = image_path.replace(filename, "")

    new_image_name = title + ".png"
    new_image_name = new_image_name.replace(" ", "_")
    new_image_name = path + new_image_name
    return new_image_name