# phrase.py
import word
import random
def output( number_of_outputs:int ):
    my_outputs = set()
    determining_output = True
    while determining_output:
        try:
            for i in range( number_of_outputs ):
                random_phrase_length = random.randint( 2, 5 )
                normal_spread = random.randint( 2, 18 )
                tight_spread = random.randint( 2, 3 )
                output_options = [
                    tag( random_chars( random_phrase_length ) ),
                    tag( decreasing_word_length( random_phrase_length, normal_spread  )  ),
                    tag( increasing_word_length( random_phrase_length, normal_spread, tight_spread ) ),
                    tag( reverse( random_chars( random_phrase_length ) ) ),
                    tag( reverse( decreasing_word_length( random_phrase_length, normal_spread  ) ) ),
                    tag( reverse( increasing_word_length( random_phrase_length, normal_spread, tight_spread ) ) ),
                ]
                output = random.choice( output_options )
                my_outputs.update( { output } )
            if len( my_outputs ) > 0:
                determining_output = False
                print('Done.')
                return list(my_outputs)
        except:
            word.data_not_in_source( normal_spread )
    
def tag( phrase:str ):
    ''' Tags phrase with SAMO® stamp '''
    output = f'**SAMO® { phrase.title() }**'
    return output
def random_chars( phrase_length_in_words:int=2 ):
    print(f'Building a phrase that is { phrase_length_in_words } words in length.')
    phrase = ''
    alphabets = word.ALPHABETS
    for i in range( phrase_length_in_words ):
        rand_char = random.choice(alphabets)
        data = word.begins_with( rand_char ) 
        phrase_element = random.choice( data )
        phrase += f'{ phrase_element } '
    return phrase
def decreasing_word_length( phrase_length_in_words:int=2, max_word_length:int=26 ):
    print(f'Building a phrase that is { phrase_length_in_words } words in length.')
    phrase = ''
    alphabets = word.ALPHABETS
    max_word_length_exceeded = ( max_word_length > 25 )
    min_word_length_not_met = ( max_word_length < 2 )
    if max_word_length_exceeded:
        print('Resetting value to accomodate for wordlist limits.')
        max_word_length = random.randint( 3, 24 )
    elif min_word_length_not_met:
        print('Resetting value to accomodate for minimum requirements.')
        max_word_length = random.randomint( 3, 24 )
    for i in range( phrase_length_in_words ):
        data = word.of_length( round( max_word_length / ( 1 + i ) ) ) 
        phrase_element = random.choice( data )
        phrase += f'{ phrase_element } '
    return phrase
def increasing_word_length( phrase_length_in_words:int=2, min_word_length:int=2, close_random:int=2 ):
    print(f'Building a phrase that is { phrase_length_in_words } words in length.')
    phrase = ''
    alphabets = word.ALPHABETS
    min_word_length_exceeded = ( min_word_length > 25 )
    min_word_length_not_met = ( min_word_length < 2  )
    if min_word_length_exceeded:
        print('Resetting value to accomodate for wordlist limits.')
        max_word_length = random.randint( 2, 24 )
    elif min_word_length_not_met:
        print('Resetting value to meet minimum requirements.')
        min_word_length = random.randint( 2, 4 )
    for i in range( phrase_length_in_words ):
        data = word.of_length( min_word_length + ( close_random * i ) ) 
        phrase_element = random.choice( data )
        phrase += f'{ phrase_element } '
    return phrase
def reverse( phrase:str ):
    phrase = phrase.split(' ')
    phrase = ' '.join( reversed( phrase ) ).strip()
    return phrase
