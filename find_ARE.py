#This is the start of my file for ARE hunting.
import re
from nltk.tokenize import regexp_tokenize
filename = input('Please enter the name of your file, including the path and extension (i.e. C:/Desktop/Rockwell_Lab/ARE_file.txt): \n')

with open(filename, 'r') as file:
    #Read the file.
    text = file.read()
    #Change all letters to upper case.
    cased_text = text.upper()
    #Tokenize the txt file.  The first token will be the entire gene, and each subsequent token will be an evolutionarily conserved region.
    tokenized_string = regexp_tokenize(cased_text, r'>[A-Za-z\d\s\-\:\(\)]+')

    #ARE = TGACxxxGC
    #regex to find this ARE: TGAC\w\w\wGC
    #Reverse ARE = CGxxxGTCA
    #regex to find reverse ARE: CG\w\w\wGTCA
    ARE_regex = (r'TGAC\w\w\wGC|CG\w\w\wGTCA')


    #regex to find the chromosome number and where the gene(or ECR) is on the chromosome.
    genome_position_regex = (r'CHR\d+:\d+')
    #Ask user for base genome species.
    species_identification = input('What species is your base genome?')
    #Make a regex based on the user's input.
    species_regex = (species_identification)
    ECR_identifier = '> ECR'
    #Instantiate an empty list to be used for storing the found AREs.
    listicle = []
    #For each token from the txt file, find AREs and store them in listicle.  Each token will have its own list stored in listicle.
    for token in tokenized_string:
        #Get the species and genome position for each token. 
        #print(token)
        genome_position = re.finditer(genome_position_regex, token)
        genome_species = re.finditer(species_regex, token, flags = re.IGNORECASE)
        #Split the genome position so we can use the chromosome number and base positions separately.
        for position in genome_position:
            genome_position_split = re.split(r':', position.group())
        #Make the species found in the token useable for printing later.
        for species in genome_species:
            use_species = species.group()
            use_species = use_species.lower()
        #Split the token so we can calculate the ARE position in the string without including the header.
        new_tokens = re.sub('\n', '', token)
        split_tokens = re.split(r'\-\d+', new_tokens)

        #Find the AREs in a token.
        for split_token in split_tokens:
            if split_token == split_tokens[0]:
                continue
            all_AREs = re.finditer(ARE_regex, split_tokens[1])
            #For each ARE, print the ARE sequence and position within the genome.
            for ARE in all_AREs:
                #Determine if the ARE is in an evolutionarily conserved region.
                if ECR_identifier in split_tokens[0]:
                    print('The following ARE is in an evolutionarily conserved region.')
                #ARE.start() returns the position within the token.
                ARE_in_string = ARE.start()
                #This allows us to determine where the ARE is in the gene.
                ARE_in_genome = int(ARE.start()) + int(genome_position_split[1])
                print('ARE sequence: [' + ARE.group() + '] \n   ARE Location in ' + str(use_species) + ' genome -- ' + str(genome_position_split[0]) + ': ' + str(ARE_in_genome))






