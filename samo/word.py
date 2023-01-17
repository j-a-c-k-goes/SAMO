# word.py
import random
import datetime
day = datetime.datetime.today().day
SOURCE_FILE = './wordlist' or '/usr/share/dict/web2'
print(f'Using { SOURCE_FILE }')
ALPHABETS = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
RANDOM_WORD_LENGTH = random.randint( 2, 25 );
RANDOM_CHAR = random.choice( ALPHABETS )
def data_not_in_source(value):
     print( f'Data is empty. Length of word ({value}) likely exceeds any source options.' )
def includes( word:str ):
    ''' 
        Source file based on if word in sourced_words.
        Write as a for loop, convert to binary search ( the word-list is sorted ).
    '''
    data = list()
    with open( SOURCE_FILE ) as source:
        for line in source:
            if word.lower() in line.lower():
                included_word = line.strip()
                data.append( included_word )
        data_not_empty = ( ( abs( len( data ) ) ) != ( 0 ) )
        if data_not_empty:
            print( f'Found { len( data ) } words which include "{ word }."' )
            return sorted( data )
        else:
            data_not_in_source( word )
            return False
def of_length( n:int ):
    data = list()
    with open( SOURCE_FILE ) as source:
        for line in source:
            passing_condition = ( ( len(line.lower().strip()) == (n) ) )
            if passing_condition:
                content = line.strip()
                data.append( content )
        data_not_empty = ( ( abs( len( data ) ) ) != ( 0 ) )
        if data_not_empty:
            print( f'Found { len(data) } words of { n } letters.')
            return sorted( data )
        else:
            data_not_in_source( n )
            return False
def differences_between( data_a, data_b ):
    pass
def similarites_across( data_a, data_b ):
    pass
def begins_with( character:str ):
    data = list()
    with open( SOURCE_FILE ) as source:
        for line in source:
            relational_case = ( character.lower() == line.lower().strip()[ 0:len(character) ] )
            if relational_case:
                expected_content = line.strip()
                data.append( expected_content )
        data_not_empty = ( ( abs( len( data ) ) ) != ( 0 ) )
        if data_not_empty:
            print( f'Found { len( data ) } words beginning with { character }' )
            return data
        else:
            print(f'Data is empty. Could not find "{ character }" in source file.')
            return False
def ends_in( character:str ):
    data = list()
    character = character[ 0 ] # forces use of string's first; if entered 'help', assume 'h'.
    with open( SOURCE_FILE ) as source:
        for line in source:
            relational_case = ( character.lower() == line.lower().strip()[ -1 ] )
            if relational_case:
                expected_content = line.strip()
                data.append( expected_content )
        data_not_empty = ( ( abs( len( data ) ) ) != ( 0 ) )
        if data_not_empty:
            print('Found:', len( data ))
            return data
        else:
            print(f'Data is empty. Could not find "{ character }" in source file.')
            return False
