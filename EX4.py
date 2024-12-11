def compte_occurences(list):
   occurrences = {}
   for mot in list:
        if mot in occurrences:
            occurrences[mot] += 1
        else:
            occurrences[mot] = 1
   return occurrences

test_list = ["Hossam", "Soufiane", "Walid", "Ahmad", "Soufiane", "Walid"]
Occurence = compte_occurences(test_list)
print("Les occurrences des mots :", Occurence)