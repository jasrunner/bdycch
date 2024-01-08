# Description: This is the main entry point for the application.

import pytesseract

from title_functions import capture_text_and_cropped_image, get_meal_type, get_title, get_new_image_filename
from title_functions import capture_ingredients, capture_method

from constants import default_data_dir
# from write_pdf import create_pdf
from pdf_a5 import A5_pdf

# Recipe Data Dictionary
recipe_data = {}

# Set the path to the Tesseract executable (replace with your actual path)
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'



# ============================================================================
# ============================================================================
#  Entry Point
def main(title_path, ingredient_path, method_path):



    captured_text, cropped_sub_image = capture_text_and_cropped_image(title_path)

    meal_type = get_meal_type(captured_text)
    title = get_title(captured_text, meal_type)

    # Display the cropped sub-image
    # cropped_sub_image.show()

    # save the cropped sub-image to a file
    new_image_name = get_new_image_filename(title_path, title)
    cropped_sub_image.save(new_image_name)


    recipe_data["title"] = title
    recipe_data["meal_type"] = meal_type
    recipe_data["image_path"] = new_image_name

    # print(recipe_data)

    # get the ingredients
    ingredients = capture_ingredients(ingredient_path)

    # get the method
    method = capture_method(method_path)

    # make a pdf
    pdf = A5_pdf(recipe_data["title"])
    pdf.add_image(recipe_data["image_path"])
    pdf.chapter_body_titles('Ingredients', 'Method')
    pdf.chapter_body(ingredients, method)
    pdf.save_to_file(recipe_data["title"])




# 
if __name__ == "__main__":

    title_path = default_data_dir + 'Screenshot_20240105-173155.png'
    ingredient_path = default_data_dir + 'Screenshot_20240105-173204.png'
    method_path = default_data_dir + 'Screenshot_20240105-173212.png'
    main(title_path, ingredient_path, method_path)



# TODO:
    #  - add time
    #  - add servings
    #  - add other tags (Batch cooking, etc.)
    #  - cleanup (c) and ) Method
    #  - Try image left-aligned and tage to the right
    #  - Reduce size of image slightly
    #  - Work out how to store individual recipes then add to a pdf

