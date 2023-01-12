import os
import csv
from PIL import Image

def create_xml_from_csv(csv_file, image_dir):
    # Create the annotations directory if it doesn't exist
    if not os.path.exists("Annotations"):
        os.mkdir("Annotations")

    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader) # Skip the header
        for row in csv_reader:
            class_name, image_path, obj_name, xmax, xmin, ymax, ymin = row
            # Open the image to get size information
            image = Image.open(os.path.join(image_dir, image_path))
            width, height = image.size
            
            # Create the .xml file for the image
            xml_file = os.path.join("Annotations", os.path.splitext(image_path)[0] + ".xml")
            with open(xml_file, 'w') as xml:
                xml.write("<annotation>\n")
                xml.write("\t<folder>{}</folder>\n".format(image_dir))
                xml.write("\t<filename>{}</filename>\n".format(image_path))
                xml.write("\t<path>{}</path>\n".format(os.path.join(image_dir, image_path)))
                xml.write("\t<source>\n\t\t<database>Unknown</database>\n\t</source>\n")
                xml.write("\t<size>\n\t\t<width>{}</width>\n\t\t<height>{}</height>\n\t\t<depth>3</depth>\n\t</size>\n".format(width, height))
                xml.write("\t<segmented>0</segmented>\n")
                xml.write("\t<object>\n\t\t<name>{}</name>\n\t\t<pose>Unspecified</pose>\n\t\t<truncated>0</truncated>\n\t\t<difficult>0</difficult>\n".format(obj_name))
                xml.write("\t\t<bndbox>\n\t\t\t<xmin>{}</xmin>\n\t\t\t<ymin>{}</ymin>\n\t\t\t<xmax>{}</xmax>\n\t\t\t<ymax>{}</ymax>\n\t\t</bndbox>\n\t</object>\n".format(xmin, ymin, xmax, ymax))
                xml.write("</annotation>")
