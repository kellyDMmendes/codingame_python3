''' Have you ever asked yourself how it might be possible to simulate this
display on a good old terminal? We have: with ASCII art! '''
width = int(input())
height = int(input())
TEXT = str(input())

alphabet = [str(input()) for i in range(height)]

for i in range(height):
    for character in TEXT:
        if 'a' <= character <= 'z':
            code = ord(character) - ord('a')
        elif 'A' <= character <= 'Z':
            code = ord(character) - ord('A')
        else:
            code = ord('z') - ord('a') + 1

        for j in range(width):
            print(alphabet[i][code * width + j], end="")

    print("")
