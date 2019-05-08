import pyperclip

while True:

    print("input URL(end:n)")
    photo_url = input(">> ")

    if photo_url == "n":
        break

    paste_code = "<span itemtype=\"http://schema.org/Photograph\" itemscope=\"itemscope\"><img class=\"magnifiable\" src=\"{}\" itemprop=\"image\"></span>".format(photo_url)
    pyperclip.copy(paste_code)
    print(paste_code)
