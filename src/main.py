# Description: This is the main entry point for the application.

import pytesseract

from title_functions import capture_text_and_cropped_image, get_meal_type, get_title, get_new_image_filename



# Recipe Data Dictionary
recipe_data = {}

# Set the path to the Tesseract executable (replace with your actual path)
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'



# ============================================================================
# ============================================================================
#  Entry Point
def main(image_path):

    captured_text, cropped_sub_image = capture_text_and_cropped_image(image_path)

    meal_type = get_meal_type(captured_text)
    title = get_title(captured_text, meal_type)

    # Display the cropped sub-image
    # cropped_sub_image.show()

    # save the cropped sub-image to a file
    new_image_name = get_new_image_filename(image_path, title)
    cropped_sub_image.save(new_image_name)


    recipe_data["title"] = title
    recipe_data["meal_type"] = meal_type
    recipe_data["image_path"] = new_image_name

    print(recipe_data)



if __name__ == "__main__":
    image_path = '/Users/j.wilden/github/bdycch/data/title.png'
    main(image_path)



# TODO:
    #  - add time
    #  - add servings
    #  - add other tags (Batch cooking, etc.)
