
def vowel_counter(string):
    """Counts the number of vowels in given string."""

    vowel_count = 0

    #iterate ovr given string
    for char in string:
        #check if char is vowel
        if char in 'aeiou':
            vowel_count += 1

    return vowel_count

def word_counter(sentence):
    """Counts the number of words in a given sentence."""

    sentence = sentence.strip() #removes white space from beginning and end of the sentence

    space_count = 0
    for char in sentence:
        #check if character is single space
        if char in ' ':
            space_count += 1

    word_count = space_count + 1

    return word_count

def count_instance_of_str(string1, string2):
    """Counts char in string1 that are also in string2."""

    count = 0

    
    #for each char in string1, check if it's in string2
    for char in string1:
        if char in string2:
            count += 1

    return count


def main():

    while 1 == 1:

        input_string = input("enter a string: ")

        if input_string == '-1':
            break

        print(vowel_counter(input_string), "vowels in", input_string)
        print(word_counter(input_string), "words in", input_string)

#to execute main function
if __name__ == '__main__':
    main()

    
        
