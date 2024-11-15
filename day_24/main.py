with open("my_text.txt") as file:
    contents = file.read()
    print(contents)

# with open("my_text.txt", mode="a") as file:
#   file.write("\nNew text.")

# mode = "a" means append (It adds to the text)
# mode = "r" means read (it replaces with the inputted text)
# mode = "w" means write (it creates new file)
