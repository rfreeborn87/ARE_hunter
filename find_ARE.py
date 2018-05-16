#This is the start of my file for ARE hunting.
import re
from nltk.tokenize import regexp_tokenize
filename = 'E:/OneDrive/Research/Rockwell_Lab/Python/ARE_hunter/hNQO1_from_ECR.txt'

with open(filename, 'r') as file:
    #Read the file.
    text = file.read()
    #Change all letters to upper case.
    cased_text = text.upper()
    #Tokenize the txt file.  The first token will be the entire gene, and each subsequent token will be an evolutionarily conserved region.
    tokenized_string = regexp_tokenize(cased_text, r'>[A-Za-z\d\s\-\:\(\)]+')

    #ARE = TGACxxxGC
    #regex to find this ARE: TGAC\w\w\wGC
    ARE_regex = (r'TGAC\w\w\wGC')
    #Instantiate an empty list to be used for storing the found AREs.
    listicle = []
    #For each token from the txt file, find AREs and store them in listicle.  Each token will have its own list stored in listicle.
    for token in tokenized_string:
        #print(re.findall(ARE_regex, token))
        listicle.append(re.findall(ARE_regex, token))
    print(listicle)

    #Iterate through the lists made for each token. 
    for item in listicle:
        #If the list for a specific token is empty, continue on.
        if not item:
            continue
        #If a token contains one or more AREs, print each ARE.
        for ARE in item:
            print(ARE)
            #find the ARE so I can see its location.  This eventually will help me locate its position in the genome.
            for token in tokenized_string:
                if re.search(ARE,token) is not None:
                    print(re.search(ARE,token))
    #Reverse ARE = CGxxxGTCA
    #regex to find reverse ARE: CG\w\w\wGTCA




