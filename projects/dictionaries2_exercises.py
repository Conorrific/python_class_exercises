#nested dictionaries
"""
contact = {
    'name': 'Paul',
    'favorite_foods': {
        'fast': 'burgers',
        'italian': 'pizza'
    }
}
print(contact['name'], contact['favorite_foods'])
"""

phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}
# print(phonebook_dict['Elizabeth'])
phonebook_dict['Kareem'] = '938-489-1234'
del phonebook_dict['Alice']
phonebook_dict['Bob'] = '968-345-2345'
# print(phonebook_dict)

ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}
print(ramit['email'])
#for the line below, just do 0 for the first activity
#if you need all the activities, use 0:4 or whatever the index
#not sure how to cherry pick indexes.. first and third etc..
#print(ramit['interests'][0])
#call the name, key, index and value.
print(ramit['friends'][0]['email'])
print(ramit['friends'][1]['interests'][1])
#def letter_histogram(letter):
 #   for letter in letter_histogram('banana'):
  #      count = 0
   #     if letter > 0:
  #          letter += 1
        


word = 'Hello there'

counts = {}

for char in word:
    if char not in counts:
        counts[char] = 1
    else:
        counts[char] += 1

print(counts)

def word_histogram(word):
    words = ""
    word_list = []
    word_lib = {}
    for i in range(len(word)):
        if word[i] == " ":
            word_list.append(words)
            words = ""

        elif i == len(word)-1:
            words = words + word[i]
            word_list.append(words)

        else:
            words = words + word[i]

    for j in range(len(word_list)):
        word_lib[word_list[j]] = word_lib.get(word_list[j],0)
        word_lib[word_list[j]] = word_lib[word_list[j]] + 1
    print(word_lib)
word_histogram('It is better to be thought a fool and remain silent then to open ones mouth and remove all doubt')

def word_histograms(word):
    words = ""
    word_list = []
    word_lib = {}
    for i in range(len(word)):
        if word[i] == " ":
            word_list.append(words)
            words = ""
        elif i == len(word)-1:
            words = words + word[i]
            word_list.append(words)

        else:
            words = words + word[i]

    for j in range(len(word_list)):
        word_lib[word_list[j]] = word_lib.get(word_list[j],0)
        word_lib[word_list[j]] = word_lib.get(word_list[j],0)
    print(word_lib)
    word_histograms('With great power comes great responsibility')





    