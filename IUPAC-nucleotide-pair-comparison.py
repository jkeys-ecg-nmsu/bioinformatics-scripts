#constants
INDEL = '-'
BASES = ['A','C','G','T','U']

ERR 			= float('-inf')
MATCH_SCORE 	=  1
MISMATCH_SCORE 	= -1
INDEL_SCORE 	= -1

#create and populate the hash table representing the symbol-base mappings.
symbols = dict()
symbols['A'] = ['A']
symbols['C'] = ['C']
symbols['G'] = ['G']
symbols['T'] = ['T','U']
symbols['U'] = ['U','T']
symbols['R'] = ['A','G']
symbols['Y'] = ['C','T']
symbols['S'] = ['G','C']
symbols['W'] = ['A','T']
symbols['K'] = ['G','T']
symbols['M'] = ['A','C']
symbols['B'] = ['G','C','T']
symbols['D'] = ['A','G','T']
symbols['H'] = ['A','C','T']
symbols['V'] = ['A','C','G']
symbols['N'] = ['A','C','G','T','U']
symbols['.'] = '-'
symbols['-'] = '-'



#score function; let 'a' be the first nucleotide and 'b' be the second.
def pair_score(a,b):
	#fix lower-case input
	a = a.upper()
	b = b.upper() 
	
	#handle invalid inputs
	if a not in symbols or b not in symbols:
		print("	One of the symbols is not encoded in the hash table!")
		return ERR
	
	#if one is an indel, return -1
	if(symbols[a] == INDEL or symbols[b] == INDEL):
		return -1
		
	#non-indel case:
	a_bases = symbols[a];
	b_bases = symbols[b];
	
	#search for a shared base, and return 1 if we have it
	for x in a_bases:
		for y in b_bases:
			if x == y:
				return 1
			
	#if we enumerated all possible base pairs but found no shared base
	return -1
	
#test cases

#match; should print one
a1 = 'a'
b1 = 'a'

if(pair_score(a1,b1) == 1):
	print("Test case 1 passed!")

#mismatch; -1
a2 = 'a'
b2 = 't'

if(pair_score(a2,b2) == -1):
	print("Test case 2 passed!")

#match (shared 'A' base)
a3 = 'd'
b3 = 'm'

if(pair_score(a3,b3) == 1):
	print("Test case 3 passed!")

#indel; -1
a4 = '.'
b4 = 'n'


if(pair_score(a4,b4) == -1):
	print("Test case 4 passed!")

#doesn't exist in table; ERR
a5 = 'x'
b5 = '2'
	
if(pair_score(a5,b5) == ERR):
	print("Test case 5 passed!")
