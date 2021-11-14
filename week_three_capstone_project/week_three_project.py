#CAPSTONE PROJECT for weeek 3
import string
from random import sample #importing the sample library
puc = string.punctuation+string.ascii_lowercase+string.ascii_uppercase + string.digits#Generating the possible characcters as a string
list(puc) #converting to a list

pas = sample(puc,15) #picks a sample list of 15 characters at random
password = ''.join(pas) #coverts the list to string
print(password) #prints the password