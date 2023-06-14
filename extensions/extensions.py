text = input("File name: ")
text = text.strip(' ').lower()
splitText = text.split('.')[-1]

if splitText == "gif":
    print("image/gif")
elif splitText == "jpg":
    print("image/jpeg")
elif splitText == "jpeg":
    print("image/jpeg")
elif splitText == "png":
    print("image/png")
elif splitText == "pdf":
    print("application/pdf")
elif splitText == "txt":
    print("text/plain")
elif splitText == "zip":
    print("application/zip")
else:
    print("application/octet-stream")