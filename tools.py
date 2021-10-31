alphabet_dictionary={"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,
                     "J":9,"K":10,"L":11,"M":12,"N":13,"O":14,"P":15, "Q":16,
                     "R":17,"S":18,"T":19,"U":20 ,"V":21,"W":22,"X":23,"Y":24,
                     "Z":25,"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,
                     "i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,
                     "q":16,"r":17,"s":18,"t":19,"u":20 ,"v":21,"w":22,"x":23,
                     "y":24,"z":25," ":" "}

alphabet={"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,
           "J":9,"K":10,"L":11,"M":12,"N":13,"O":14,"P":15, "Q":16,
           "R":17,"S":18,"T":19,"U":20 ,"V":21,"W":22,"X":23,"Y":24,
           "Z":25, " ":" "}


def type_str_error(letters:str):
    """
    Raises type error if the format isn't a string
    """
    # ensures that the cipher_text is a string
    if type(letters) != str:
        raise TypeError("CipherText must be type string")


def type_alphabet_error(letters:str):
    """
    Raise type error if letter is not in the alphabet
    """
    alphabet = ["A","B","C","D","E","F","G","H",
                "I","J","K","L","M","N","O","P",
                "Q","R","S","T","U" ,"V","W","X",
                "Y","Z","a","b","c","d","e","f",
                "g","h","i","j","k","l","m","n",
                "o","p","q","r","s","t","u" ,"v",
                "w","x","y","z"]
    for letter in letters:
        if letter not in alphabet and letter != " ":
                raise TypeError("""Letter in CipherText must be 
                                letter between A-Z""", letter)
    
    
def get_pos_alphabet(letters:str)->list:

    alpha_positions=[alphabet_dictionary[letter] for letter in letters]

    return alpha_positions 

def get_atbashed_pos_alphabet(numbers):
    
    new_position = [(25-alpha_position) %26 for alpha_position in numbers if alpha_position!=" "] 
    
    return new_position

def get_key(val):
   for key, value in alphabet.items():
      
       if value == val:
          return key
   return "key doesn't exist"

def get_alphabet_from_pos(letter_pos):
    
    alpha=[get_key(letter) for letter in letter_pos]
    
    return alpha
    
    