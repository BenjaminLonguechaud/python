
import os
print(os.name)

# Current directory 
print(os.getcwd())

print(os.listdir())
os.makedirs("my_first_directory/my_second_directory")
os.removedirs("my_first_directory/my_second_directory")
# Or
returned_value = os.system("mkdir my_first_directory")
returned_value = os.system("removedirs my_first_directory")

print(os.listdir())