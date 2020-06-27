import os
#print(os.listdir())
files = os.listdir()
# print(type(files))
# print(files)
for f in files:
    print(type(f))
    
for f in files:
    file_size = os.path.getsize(f) #cuanto pesa en bites
    print(f'The file {f} is {file_size}')
