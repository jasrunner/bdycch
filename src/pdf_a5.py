from fpdf import FPDF



class A5_pdf(FPDF):

    def __init__(self, title):
        super().__init__(format='A5')
        self.title = title
        # self.image_path = image_path
        # self.ingredients = ingredients
        # self.method = method

        self.add_page()
        # self.set_font('Arial', 'B', 10)

    def header(self):
        # Add a central title
        self.set_font('Arial', 'B', 10)
        self.set_y(20)
        self.cell(0, 10, self.title, ln=True, align='C')
        # self.ln(4)  # Add some space after the title

    def add_image(self, image_path):
        # Add a central image
        self.image(image_path, x=45, y=self.get_y(), w=60, h=0,)
        # Add some space after the image
        self.ln(60) 


    # def chapter_title(self, title):
    #     # Add a chapter title
    #     self.set_font('Arial', 'B', 12)
    #     self.cell(0, 10, title, 0, 1, 'C')
    #     self.ln(4)  # Add some space after the title

    def chapter_body_titles(self, left_column, right_column):
        # Set A5 page dimensions
        a5_width = 148    
        column_width = a5_width / 2 - 5  # Subtracting some padding

        self.set_font('Arial', 'B', 10)
        self.cell(column_width , 10, left_column, 0, 0, 'L')

        self.cell(column_width , 10, right_column, 0, 0, 'L')  
        self.ln(10)  # Add some space after the title

    def chapter_body(self, left_column, right_column):

        self.set_font('Arial', '', 8)
        # Set A5 page dimensions
        a5_width = 148  # Width in mm
        a5_height = 210  # Height in mm

        # Calculate the width and height of each column
        column_width = a5_width / 2 - 15  # Subtracting some padding
        # column_height = a5_height
        column_spacing = 10
        height = 5
        
        # Here we save what will be the top of each columns
        ybefore = self.get_y()
        
        # First column
        
        self.multi_cell (
            column_width, 
            height, 
            left_column,
        )
            # 'LRTB',
            # 'L',
            # 0)
        
        # Notice we have to account for the left margin to get the spacing between
        # columns right.
        
        self.set_xy(column_width + self.l_margin + column_spacing, ybefore)
        
        # Second column
        
        self.multi_cell(
            column_width, 
            height, 
            right_column)
        

    def save_to_file(self, title):
        # replace and spaces with underscores
        title = title.replace(' ', '_')
        self.output(title + '.pdf', 'F')
        
