#This is the start of my file for ARE hunting.

filename = 'E:/OneDrive/Research/Rockwell_Lab/Python/ARE_hunter/hIFNg_from_ECR.txt'

#file = open(filename, mode = 'r')
with open(filename, 'r') as file:
    text = file.read()
    cased_text = text.upper()
print(cased_text)

#file.close()