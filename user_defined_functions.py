def count_vowels(quote):
    # count the number of vowels and print
    quote = quote.lower()    # convert to lower case
    number_of_vowels = 0
    for character in quote:   # for each character in the quote
        if character in "aeiou":    # if character is a, e, i, o or u
            number_of_vowels += 1    # add 1 to number of vowels

    return number_of_vowels


def main():    # main function
    quote = "All we have to decide is what to do with the time that is given to us."
    number_of_vowels = count_vowels(quote)
    print(f"Number of vowels is: {number_of_vowels}")

    quote_two = "You only Live Once"
    number_of_vowels_two = count_vowels(quote_two)
    print(f"Number of vowels is: {number_of_vowels_two}")


main()    # Call the main function