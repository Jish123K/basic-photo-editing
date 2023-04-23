import os

import sys

import time

import random

import PIL

import pyexif

import wand
class PhotoEditor:

    def __init__(self):

        self.app_dir = os.path.dirname(os.path.realpath(__file__))

        self.temp_dir = os.path.join(self.app_dir, "temp")

        self.edited_photos_dir = os.path.join(self.app_dir, "edited_photos")

    def open_photo(self, photo_path):

        with open(photo_path, "rb") as f:

            photo = PIL.Image.open(f)

        return photo

    def edit_photo(self, photo, **kwargs):

        for key, value in kwargs.items():

            setattr(photo, key, value)

        return photo

    def save_photo(self, photo, save_path):

        photo.save(save_path)

    def delete_photo(self, photo_path):

        os.remove(photo_path)

    def get_exif_data(self, photo_path):

        with open(photo_path, "rb") as f:

            exif_data = pyexif.Exif(f)

        return exif_data

    def remove_exif_data(self, photo_path):

        exif_data = self.get_exif_data(photo_path)

        for tag in exif_data:

            exif_data.remove(tag)

        with open(photo_path, "wb") as f:

            exif_data.write(f)

    def main(self):

        while True:

            print("1. Open photo")

            print("2. Edit photo")

            print("3. Save photo")

            print("4. Delete photo")

            print("5. Remove EXIF data")

            print("6. Exit")

            option = input("Enter your choice: ")

            if option == "1":

                photo_path = input("Enter the path of the photo to open: ")

                photo = self.open_photo(photo_path)

                print("Photo opened successfully.")

            elif option == "2":

                kwargs = {}

                for key, value in input("Enter the key-value pairs for editing the photo: ").split(", "):

                    key, value = key.strip(), value.strip()

                    kwargs[key] = value

                edited_photo = self.edit_photo(photo, **kwargs)

                print("Photo edited successfully.")

            elif option == "3":

                save_path = input("Enter the path to save the edited photo: ")

                self.save_photo(edited_photo, save_path)

                print("Photo saved successfully.")

            elif option == "4":

                photo_path = input("Enter the path of the photo to delete: ")

                self.delete_photo(photo_path)

                print("Photo deleted successfully.")

            elif option == "5":

                photo_path = input("Enter the path of the photo to remove EXIF data from: ")

                self.remove_exif_data(photo_path)

                print("EXIF data removed successfully.")

            elif option == "6":

                break

            else:

                print("Invalid option.")

        print("Exiting...")

# Add a new method to the PhotoEditor class that blurs the photo

def blur_photo(self, photo, radius):

    photo = photo.filter("GaussianBlur", radius=radius)

    return photo

# Add a new method to the PhotoEditor class that sharpens the photo

def sharpen_photo(self, photo, radius):

    photo = photo.filter("UnsharpMask", radius=radius)

    return photo

# Add a new method to the PhotoEditor class that adds a border to the photo

def add_border(self, photo, width, color):

    photo = photo.convert("RGBA")

    border = PIL.Image.new("RGBA", (width, width), color)

    photo.paste(border, (0, 0))

    photo = photo.convert("RGB")

    return photo

# Add a new method to the PhotoEditor class that rotates the photo

# Add a new method to the PhotoEditor class that flips the photo horizontally
def flip_photo_horizontally(self, photo):
    photo = photo.transpose(Image.FLIP_LEFT_RIGHT)
    return photo


# Add a new method to the PhotoEditor class that flips the photo vertically
def flip_photo_vertically(self, photo):
    photo = photo.transpose(Image.FLIP_TOP_BOTTOM)
    return photo


# Add a new method to the PhotoEditor class that crops the photo
def crop_photo(self, photo, x1, y1, x2, y2):
    photo = photo.crop((x1, y1, x2, y2))
    return photo


# Add a new method to the PhotoEditor class that resizes the photo
def resize_photo(self, photo, width, height):
    photo = photo.resize((width, height))
    return photo


# Add a new method to the PhotoEditor class that converts the photo to grayscale
def convert_to_grayscale(self, photo):
    photo = photo.convert("L")
    return photo


# Add a new method to the PhotoEditor class that converts the photo to black and white
def convert_to_black_and_white(self, photo):
    photo = photo.convert("1")
    return photo


# Add a new method to the PhotoEditor class that adjusts the brightness of the photo
def adjust_brightness(self, photo, brightness):
    photo = photo.point(lambda x: x * brightness)
    return photo


# Add a new method to the PhotoEditor class that adjusts the contrast of the photo
def adjust_contrast(self, photo, contrast):
    photo = photo.point(lambda x: (x - 0.5) * contrast + 0.5)
    return photo


# Add a new method to the PhotoEditor class that adjusts the saturation of the photo
def adjust_saturation(self, photo, saturation):
    photo = photo.convert("RGB")
    photo = photo.filter("ColorLookup", PIL.Image.open("saturation.lut"))
    photo = photo.convert("L")
    return photo


# Add a new method to the PhotoEditor class that adjusts the hue of the photo
def adjust_hue(self, photo, hue):
    photo = photo.convert("RGB")
    photo = photo.filter("ColorLookup", PIL.Image.open("hue.lut"))
    photo = photo.convert("L")
    return photo


# Add a new method to the PhotoEditor class that adds a text watermark to the photo
def add_text_watermark(self, photo, text, x, y, size, color):
    font = ImageFont.truetype("arial.ttf", size)
    draw = ImageDraw.Draw(photo)
    draw.text((x, y), text, fill=color, font=font)
    return photo


# Add a new method to the PhotoEditor class that adds an image watermark to the photo
def add_image_watermark(self, photo, watermark, x, y, opacity):
    watermark = watermark.resize((photo.width, photo.height))
    photo.paste(watermark, (x, y), mask=watermark)
    return photo
# Add a new method to the PhotoEditor class that adjusts the opacity of the watermark

def adjust_watermark_opacity(self, photo, watermark, opacity):

    watermark = watermark.resize((photo.width, photo.height))

    photo.paste(watermark, (x, y), mask=watermark)

    return photo

# Add a new method to the PhotoEditor class that rotates the watermark

def rotate_watermark(self, photo, watermark, angle):

    watermark = watermark.rotate(angle)

    photo.paste(watermark, (x, y), mask=watermark)

    return photo

# Add a new method to the PhotoEditor class that flips the watermark horizontally

def flip_watermark_horizontally(self, photo, watermark):

    watermark = watermark.transpose(Image.FLIP_LEFT_RIGHT)

    photo.paste(watermark, (x, y), mask=watermark)

    return photo

# Add a new method to the PhotoEditor class that flips the watermark vertically

def flip_watermark_vertically(self, photo, watermark):

    watermark = watermark.transpose(Image.FLIP_TOP_BOTTOM)

    photo.paste(watermark, (x, y), mask=watermark)

    return photo

# Add a new method to the PhotoEditor class that crops the watermark

def crop_watermark(self, photo, watermark, x1, y1, x2, y2):

    watermark = watermark.crop((x1, y1, x2, y2))

    photo.paste(watermark, (x, y), mask=watermark)

    return photo

# Add a new method to the PhotoEditor class that resizes the watermark

def resize_watermark(self, photo, watermark, width, height):

    watermark = watermark.resize((width, height))

    photo.paste(watermark, (x, y), mask=watermark)

    return photo

# Add a new method to the PhotoEditor class that converts the watermark to grayscale

def convert_watermark_to_grayscale(self, photo, watermark):

    watermark = watermark.convert("L")

    photo.paste(watermark, (x, y), mask=watermark)

    return photo

# Add a new method to the PhotoEditor class that converts the watermark to black and white

def convert_watermark_to_black_and_white(self, photo, watermark):

    watermark = watermark.convert("1")

    photo.paste(watermark, (x, y), mask=watermark)

    return photo

# Add a new method to the PhotoEditor class that adjusts the brightness of the watermark

def adjust_watermark_brightness(self, photo, watermark, brightness):

    watermark = watermark.point(lambda x: x * brightness)

    photo.paste(watermark, (x, y), mask=watermark)

    return photo

# Add a new method to the PhotoEditor class that adjusts the contrast of the watermark

def adjust_watermark_contrast(self, photo, watermark, contrast):

    watermark = watermark.point(lambda x: (x - 0.5) * contrast + 0.5)

    photo.paste(watermark, (x, y), mask=watermark)

    return photo

# Add a new method to the PhotoEditor class that adjusts the saturation of the watermark

def adjust_watermark_saturation(self, photo, watermark, saturation):

    watermark = watermark.convert("RGB")

    watermark = watermark.filter("ColorLookup", PIL.Image.open("saturation.lut"))

    watermark = watermark.convert("L")

    photo.paste(watermark, (x, y), mask=watermark)

    return photo

# Add a new method to the PhotoEditor class that adjusts the hue of the watermark

def adjust_watermark_hue(self, photo, watermark, hue):

    watermark = watermark.convert("RGB")

    watermark = watermark.filter("ColorLookup", PIL.Image.open("hue.lut"))

    watermark = watermark.convert("L")

    photo.paste(watermark, (x, y), mask=watermark)

    return photo
# Add a new method to the PhotoEditor class that adjusts the watermark's position

def adjust_watermark_position(self, photo, watermark, x, y):

    watermark = watermark.resize((photo.width, photo.height))

    photo.paste(watermark, (x, y), mask=watermark)

    return photo

# Add a new method to the PhotoEditor class that adds a border to the watermark

def add_border_to_watermark(self, photo, watermark, width, color):

    watermark = watermark.convert("RGBA")

    border = PIL.Image.new("RGBA", (width, width), color)

    watermark.paste(border, (0, 0))

    watermark = watermark.convert("RGB")

    photo.paste(watermark, (x, y), mask=watermark)

    return photo

# Add a new method to the PhotoEditor class that blurs the watermark

def blur_watermark(self, photo, watermark, radius):

    watermark = watermark.filter("GaussianBlur", radius=radius)

    photo.paste(watermark, (x, y), mask=watermark)

    return photo

# Add a new method to the PhotoEditor class that sharpens the watermark

def sharpen_watermark(self, photo, watermark, radius):

    watermark = watermark.filter("UnsharpMask", radius=radius)

    photo.paste(watermark, (x, y), mask=watermark)

    return photo

# Add a new method to the PhotoEditor class that converts the watermark to grayscale

def convert_watermark_to_grayscale(self, photo, watermark):

    watermark = watermark.convert("L")

    photo.paste(watermark, (x, y), mask=watermark)

    return photo

# Add a new method to the PhotoEditor class that converts the watermark to black and white

def convert_watermark_to_black_and_white(self, photo, watermark):

    watermark = watermark.convert("1")

    photo.paste(watermark, (x, y), mask=watermark)

    return photo

# Add a new method to the PhotoEditor class that adjusts the brightness of the watermark

def adjust_watermark_brightness(self, photo, watermark, brightness):

    watermark = watermark.point(lambda x: x * brightness)

    photo.paste(watermark, (x, y), mask=watermark)

    return photo

# Add a new method to the PhotoEditor class that adjusts the contrast of the watermark

def adjust_watermark_contrast(self, photo, watermark, contrast):

    watermark = watermark.point(lambda x: (x - 0.5) * contrast + 0.5)

    photo.paste(watermark, (x, y), mask=watermark)

    return photo

# Add a new method to the PhotoEditor class that adjusts the saturation of the watermark

def adjust_watermark_saturation(self, photo, watermark, saturation):

    watermark = watermark.convert("RGB")

    watermark = watermark.filter("ColorLookup", PIL.Image.open("saturation.lut"))

    watermark = watermark.convert("L")

    photo.paste(watermark, (x, y), mask=watermark)

    return photo

# Add a new method to the PhotoEditor class that adjusts the hue of the watermark

def adjust_watermark_hue(self, photo, watermark, hue):

    watermark = watermark.convert("RGB")

    watermark = watermark.filter("ColorLookup", PIL.Image.open("hue.lut"))

    watermark = watermark.convert("L")

    photo.paste(watermark, (x, y), mask=watermark)

    return photo

# Add a new method to the PhotoEditor class that saves the edited photo to a file

def save_photo(self, photo, save_path):

    photo.save(save_path)

    return photo
# Add a new method to the PhotoEditor class that resizes the watermark to the size of the photo

def resize_watermark_to_photo_size(self, photo, watermark):

    watermark = watermark.resize((photo.width, photo.height))

    photo.paste(watermark, (x, y), mask=watermark)

    return photo

# Add a new method to the PhotoEditor class that adds a watermark to the center of the photo

def add_watermark_to_center(self, photo, watermark):

    watermark = watermark.resize((photo.width, photo.height))

    photo.paste(watermark, (int(photo.width / 2) - int(watermark.width / 2), int(photo.height / 2) - int(watermark.height / 2)), mask=watermark)

    return photo

# Add a new method to the PhotoEditor class that adds a watermark to the top left corner of the photo

def add_watermark_to_top_left_corner(self, photo, watermark):

    watermark = watermark.resize((photo.width, photo.height))

    photo.paste(watermark, (0, 0), mask=watermark)

    return photo

# Add a new method to the PhotoEditor class that adds a watermark to the top right corner of the photo

def add_watermark_to_top_right_corner(self, photo, watermark):

    watermark = watermark.resize((photo.width, photo.height))

    photo.paste(watermark, (photo.width - watermark.width, 0), mask=watermark)

    return photo

# Add a new method to the PhotoEditor class that adds a watermark to the bottom left corner of the photo

def add_watermark_to_bottom_left_corner(self, photo, watermark):

    watermark = watermark.resize((photo.width, photo.height))

    photo.paste(watermark, (0, photo.height - watermark.height), mask=watermark)

    return photo

# Add a new method to the PhotoEditor class that adds a watermark to the bottom right corner of the photo

def add_watermark_to_bottom_right_corner(self, photo, watermark):

    watermark = watermark.resize((photo.width, photo.height))

    photo.paste(watermark, (photo.width - watermark.width, photo.height - watermark.height), mask=watermark)

    return photo

# Add a new method to the PhotoEditor class that rotates the watermark by 90 degrees

def rotate_watermark_90_degrees(self, photo, watermark):

    watermark = watermark.rotate(90)

    photo.paste(watermark, (x, y), mask=watermark)

    return photo

# Add a new method to the PhotoEditor class that rotates the watermark by 180 degrees

def rotate_watermark_180_degrees(self, photo, watermark):

    watermark = watermark.rotate(180)

    photo.paste(watermark, (x, y), mask=watermark)

    return photo

# Add a new method to the PhotoEditor class that rotates the watermark by 270 degrees

def rotate_watermark_270_degrees(self, photo, watermark):

    watermark = watermark.rotate(270)

    photo.paste(watermark, (x, y), mask=watermark)

    return photo
# Add a new method to the PhotoEditor class that adds a watermark to the photo at a specific position

def add_watermark_at_position(self, photo, watermark, x, y):

    watermark = watermark.resize((photo.width, photo.height))

    photo.paste(watermark, (x, y), mask=watermark)

    return photo

# Add a new method to the PhotoEditor class that adds a watermark to the photo at a specific opacity

def add_watermark_at_opacity(self, photo, watermark, opacity):

    watermark = watermark.resize((photo.width, photo.height))

    photo.paste(watermark, (x, y), mask=watermark, alpha=opacity)

    return photo

# Add a new method to the PhotoEditor class that adds a watermark to the photo at a specific rotation

def add_watermark_at_rotation(self, photo, watermark, rotation):

    watermark = watermark.resize((photo.width, photo.height))

    photo.paste(watermark, (x, y), mask=watermark, rotation=rotation)

    return photo

# Add a new method to the PhotoEditor class that adds a watermark to the photo at a specific scale

def add_watermark_at_scale(self, photo, watermark, scale):

    watermark = watermark.resize((photo.width * scale, photo.height * scale))

    photo.paste(watermark, (x, y), mask=watermark)

    return photo

# Add a new method to the PhotoEditor class that adds a watermark to the photo at a specific translation

def add_watermark_at_translation(self, photo, watermark, x, y):

    watermark = watermark.resize((photo.width, photo.height))

    photo.paste(watermark, (x, y), mask=watermark)

    return photo

# Add a new method to the PhotoEditor class that adds a watermark to the photo at a specific shear

def add_watermark_at_shear(self, photo, watermark, shear):

    watermark = watermark.resize((photo.width, photo.height))

    photo.paste(watermark, (x, y), mask=watermark, shear=shear)

    return photo

# Add a new method to the PhotoEditor class that adds a watermark to the photo at a specific transform

def add_watermark_at_transform(self, photo, watermark, transform):

    watermark = watermark.resize((photo.width, photo.height))

    photo.paste(watermark, (x, y), mask=watermark, transform=transform)

    return photo
# Add a new method to the PhotoEditor class that adds a watermark to the photo at a specific position and opacity

def add_watermark_at_position_and_opacity(self, photo, watermark, x, y, opacity):

    watermark = watermark.resize((photo.width, photo.height))

    photo.paste(watermark, (x, y), mask=watermark, alpha=opacity)

    return photo

# Add a new method to the PhotoEditor class that adds a watermark to the photo at a specific position and rotation

def add_watermark_at_position_and_rotation(self, photo, watermark, x, y, rotation):

    watermark = watermark.resize((photo.width, photo.height))

    photo.paste(watermark, (x, y), mask=watermark, rotation=rotation)

    return photo

# Add a new method to the PhotoEditor class that adds a watermark to the photo at a specific position and scale

def add_watermark_at_position_and_scale(self, photo, watermark, x, y, scale):

    watermark = watermark.resize((photo.width * scale, photo.height * scale))

    photo.paste(watermark, (x, y), mask=watermark)

    return photo

# Add a new method to the PhotoEditor class that adds a watermark to the photo at a specific position and translation

def add_watermark_at_position_and_translation(self, photo, watermark, x, y):

    watermark = watermark.resize((photo.width, photo.height))

    photo.paste(watermark, (x, y), mask=watermark)

    return photo

# Add a new method to the PhotoEditor class that adds a watermark to the photo at a specific position and shear

def add_watermark_at_position_and_shear(self, photo, watermark, x, y, shear):

    watermark = watermark.resize((photo.width, photo.height))

    photo.paste(watermark, (x, y), mask=watermark, shear=shear)

    return photo

# Add a new method to the PhotoEditor class that adds a watermark to the photo at a specific position and transform

def add_watermark_at_position_and_transform(self, photo, watermark, x, y, transform):

    watermark = watermark.resize((photo.width, photo.height))

    photo.paste(watermark, (x, y), mask=watermark, transform=transform)

    return photo
# Add a new method to the PhotoEditor class that crops the photo to a specific size

def crop_photo_to_size(self, photo, width, height):

    photo = photo.crop((0, 0, width, height))

    return photo

# Add a new method to the PhotoEditor class that resizes the photo to a specific size

def resize_photo_to_size(self, photo, width, height):

    photo = photo.resize((width, height))

    return photo

# Add a new method to the PhotoEditor class that rotates the photo by a specific number of degrees

def rotate_photo_by_degrees(self, photo, degrees):

    photo = photo.rotate(degrees)

    return photo

# Add a new method to the PhotoEditor class that flips the photo horizontally

def flip_photo_horizontally(self, photo):

    photo = photo.transpose(Image.FLIP_LEFT_RIGHT)

    return photo

# Add a new method to the PhotoEditor class that flips the photo vertically

def flip_photo_vertically(self, photo):

    photo = photo.transpose(Image.FLIP_TOP_BOTTOM)

    return photo

# Add a new method to the PhotoEditor class that blurs the photo

def blur_photo(self, photo, radius):

    photo = photo.filter("GaussianBlur", radius=radius)

    return photo

# Add a new method to the PhotoEditor class that sharpens the photo

def sharpen_photo(self, photo, radius):

    photo = photo.filter("UnsharpMask", radius=radius)

    return photo

# Add a new method to the PhotoEditor class that converts the photo to grayscale

def convert_photo_to_grayscale(self, photo):

    photo = photo.convert("L")

    return photo

# Add a new method to the PhotoEditor class that converts the photo to black and white

def convert_photo_to_black_and_white(self, photo):

    photo = photo.convert("1")

    return photo

# Add a new method to the PhotoEditor class that adjusts the brightness of the photo

def adjust_photo_brightness(self, photo, brightness):

    photo = photo.point(lambda x: x * brightness)

    return photo

# Add a new method to the PhotoEditor class that adjusts the contrast of the photo

def adjust_photo_contrast(self, photo, contrast):

    photo = photo.point(lambda x: (x - 0.5) * contrast + 0.5)

    return photo

# Add a new method to the PhotoEditor class that adjusts the saturation of the photo

def adjust_photo_saturation(self, photo, saturation):

    photo = photo.convert("RGB")

    photo = photo.filter("ColorLookup", PIL.Image.open("saturation.lut"))

    photo = photo.convert("L")

    return photo

# Add a new method to the PhotoEditor class that adjusts the hue of the photo

def adjust_photo_hue(self, photo, hue):

    photo = photo.convert("RGB")

    photo = photo.filter("ColorLookup", PIL.Image.open("hue.lut"))

    photo = photo.convert("L")

    return photo

# Add a new method to the PhotoEditor class that adds text to the photo

def add_text_to_photo(self, photo, text, x, y, size, color):

    font = ImageFont.truetype("arial.ttf", size)

    draw = ImageDraw.Draw(photo)

    draw.text((x, y), text, fill=color, font=font)

    return photo

# Add a new method to the PhotoEditor class that adds an image to the photo

def add_image_to_photo(self, photo, image, x, y, opacity):

    image = image.resize((photo.width, photo.height))

    photo.paste(image, (x, y), mask=image, alpha=opacity)

    return photo
  







   

