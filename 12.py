
from PIL import Image, ImageFilter, ImageEnhance

class ImageConverter:

    def __init__(self, filename):
        self.image = Image.open(filename)

    def grayscale(self):
        self.image = self.image.convert("L")

    def blur(self):
        self.image = self.image.filter(ImageFilter.BLUR)

    def sharpen(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)

    def brightness(self):
        tool = ImageEnhance.Brightness(self.image)
        self.image = tool.enhance(1.5)

    def rgb(self):
        self.image = self.image.convert("RGB")

    def hsv(self):
        self.image = self.image.convert("HSV")

    def save_image(self):
        self.image.save("output_image.png")
        self.image.show()
        print("Image saved successfully!")

    def run(self):

        operations = {
            "1": self.grayscale,
            "2": self.blur,
            "3": self.sharpen,
            "4": self.brightness,
            "5": self.rgb,
            "6": self.hsv
        }

        print("\n--- Image Filter and Color Converter ---")
        print("1. Grayscale")
        print("2. Blur")
        print("3. Sharpen")
        print("4. Brightness")
        print("5. RGB Conversion")
        print("6. HSV Conversion")

        choice = input("Select an operation: ")

        if choice in operations:
            operations[choice]()
            self.save_image()
        else:
            print("Invalid selection!")


try:
    file = input("Enter image file path: ")
    converter = ImageConverter(file)
    converter.run()

except Exception as error:
    print("Error:", error)
