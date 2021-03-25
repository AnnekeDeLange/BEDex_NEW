from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = 'c545bc87620d4ced81cbddb8a90b4a51'
__human_name__ = 'for'


""" Write your functions here. """

alphabet = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','o',
          'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# functions for Part1 - shortest_names

def shortest_names(names):
    shortest_country = []
    lengths = []
    for c in names:
        length_country = len(str(c))
        lengths.append(length_country)
    for c in names:
        if len(str(c)) == min(lengths):
            shortest_country.append(c)
    return shortest_country

# functions for Part2 - most_vowels

def number_of_vowels(string):
    lower_string = string.lower()
    number = 0
    for c in lower_string:
        if c in ['a', 'e', 'i', 'o', 'u']:
            number = number + 1
    return number

def vowels_per_country(countrylist):
    country_vowel_pairs= []
    for s in countrylist:
        t = [s, number_of_vowels(s)]
        country_vowel_pairs.append(t)
    return country_vowel_pairs

def most_vowels(country_list):
    paired_list = vowels_per_country(country_list)
    ordered_paired_list = sorted(paired_list, key=lambda x:x[1],reverse=True)
    top_3_countries = [ordered_paired_list[0][0], ordered_paired_list[1][0], ordered_paired_list[2][0]] 
    return top_3_countries

# functions for Part3 - alphabet_set

def my_remove_subset_from_list(subset, list):
    new_list = my_list_copy(list)
    elements = subset
    for e in elements:
        if e in new_list:
            test = True
            to_remove = e
            new_list.remove(str(e))
        else:
            continue
    return new_list

## prevenst unintentional modification of the original
def my_list_copy(input_list):
    check  = True
    output_list = []
    for element in input_list:
        if check == True:
            output_list.append(element)
    return output_list

def my_intersection(li1, li2):
    intersection = sorted(list( set(li1) & set(li2) ))
    return intersection

## different_chars_in_string returns a list of all unique unique letters in a string ; case insensitive
def different_chars_in_string(string):
    lower_string = string.lower()
    different_chars_in_string = list(sorted(set(lower_string) & set(alphabet)))
    return list(different_chars_in_string)

## picks one string from a list of string-elements, that best matches a specific character-set
def best_matching_country(chars_needed, country_list):
    provided_upto_now = []
    best_upto_now = []
    for c in country_list:
        chars_in_country = different_chars_in_string(c)
        possible_to_provide = my_intersection(chars_in_country, chars_needed)
        lengte1 = len(possible_to_provide)
        lengte2 = len(provided_upto_now)
        if len(possible_to_provide) > len(provided_upto_now):
            best_upto_now = [c]
            provided_upto_now = possible_to_provide
        else:
            continue
    return best_upto_now

## provides a list of string-elements that together provide a required list of character; i.e. the alphabet
# main function in Dl 3-FOR-exercise
def alphabet_set(country_list):
    ## initialiseren van variabelen
    missing_chars = my_list_copy(alphabet)
    countries_left = my_list_copy(country_list)
    countries_in_alphabet_set = []
    country_found = []
    ## functie body hierna
    for c in countries_left:
        if missing_chars == []:
            result = countries_in_alphabet_set
            break
        elif len(countries_in_alphabet_set) > 14:
            result = ('14 countries are not enough to provide the complete alphabet')
            break
        else:
            country_found = best_matching_country(missing_chars, countries_left)
            chars_in_country_found = different_chars_in_string(str([country_found]))
            missing_chars_provided_by_country =  my_intersection(chars_in_country_found, missing_chars)
            countries_in_alphabet_set = countries_in_alphabet_set + country_found
            countries_left = my_remove_subset_from_list(country_found, countries_left)
            missing_chars = my_remove_subset_from_list(missing_chars_provided_by_country, missing_chars)
    return result


# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == '__main__':
    countries = get_countries()
    shortest_names(countries)
    #print('Countries with shortest names are : ', shortest_names(countries))
    most_vowels(countries)
    #print('Top 3 countries with most vowels : ', most_vowels(countries))
    alphabet_set(countries)
    #print('Countries whose characters together provide the whole alphabet are : \n', alphabet_set(countries) )

""" Write the calls to your functions here. """


