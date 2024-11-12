# HASH TABLE IN PYTHON (DICTIONARY)

# ex 1

student = {
    "name" : "Feyza",
    "age" : 22,
    "department" : "computer engineering",
    "interest" : "python"    
}

for key, value in student.items():
    print(f"{key} : {value}")
    
# ex 2

phone_book = {
    "name" : "Feyza",
    "number" : 12345
}

phone_book["Efe"] = 55555 # adding
phone_book["Feyza"] = 33333 # update

print(phone_book["Efe"]) # accessing value

for key, value in phone_book.items():
    print(f"{key} : {value}")
    
# ex 3

def letter_frequency(sentence):
    frequency = {}
    for char in sentence:
        if char.isalpha():
            char = char.lower()
            frequency[char] = frequency.get(char,0) + 1
    return frequency
sentence = "Hash tables in Python!"
print(letter_frequency(sentence))
            

# ex 4 

def find_common_elements(list1, list2):
    hash_table = {}
    common_elements = []
    
    for item in list1:
        hash_table[item] = True
    for item in list2:
        if item in hash_table:
            common_elements.append(item)
    return common_elements

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print(find_common_elements(list1, list2))

