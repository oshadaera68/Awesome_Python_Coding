import easyocr


def is_text_present(image_path):
    reader = easyocr.Reader(['en'])
    result = reader.readtext('images/1.jpg')
    return len(result) > 0


print(is_text_present('images/1.jpg'))
print(is_text_present('images/2.jpg'))
