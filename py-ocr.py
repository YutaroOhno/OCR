from PIL import Image
import sys

import pyocr
import pyocr.builders

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
tool = tools[0]

text = tool.image_to_string(
    Image.open('画像パス'),
    lang="jpn",
    builder=pyocr.builders.TextBuilder()
)

print(text)
