# from functions.get_file_content import get_file_content

# out = get_file_content("./calculator", "lorem.txt")
# print(len(out))
# print(out[-200:])

from functions.write_file import write_file

print(write_file("./calculator", "scratch.txt", "hello"))
