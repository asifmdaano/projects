import qrcode 

def qrcode_generator(source:str)-> str:
    img = qrcode.make(source)   # make function create an image
    img.save("google.png")      # created image save as 'google.png' in png format in the same dir

def main():
    data = "https://www.google.com"
    qrcode_generator(data)

main()