#This is the start of my file for ARE hunting.
import re
from nltk.tokenize import regexp_tokenize
filename = 'E:/OneDrive/Research/Rockwell_Lab/Python/ARE_hunter/hNQO1_from_ECR.txt'

#file = open(filename, mode = 'r')
with open(filename, 'r') as file:
    text = file.read()
    cased_text = text.upper()
    #Tokenize the txt file.  The first token will be the entire gene, and each subsequent token will be an evolutionarily conserved region.
    tokenized_string = regexp_tokenize(cased_text, r'>[A-Za-z\d\s\-\:\(\)]+')
    for token in tokenized_string:
        print(token)
    #ARE = TGACxxxGC
    #regex to find this ARE: TGAC\w\w\wGC
    ARE_regex = (r'TGAC\w\w\wGC')
    #print(re.search(ARE_regex, cased_text))
    #Reverse ARE = CGxxxGTCA
    #regex to find reverse ARE: CG\w\w\wGTCA
#print(cased_text)



#file.close()