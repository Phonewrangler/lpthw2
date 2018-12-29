from sys import argv
script, asciiart = argv

with open(asciiart) as artwork:
    print(artwork.read())
