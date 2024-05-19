
#ODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

#ODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas as p

data=p.read_csv('nato_phonetic_alphabet.csv')

# for i,r in data.iterrows():
#     print(r)

credic={r.letter:r.code for i,r in data.iterrows()}
# print(credic)

instr=input("Enter a Word: ").upper()

codeword=[credic[l] for l in instr]
print(codeword)


# cr=[]
# for i in instr:
#     for k,v in credic.items():
#         if i==k:
#             cr.append(v)
# print(cr)
