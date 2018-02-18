
fr_en = {
  "Bonjour": "Good morning",
  "Aurevoir": "Good bye"
}

word_to_translate = input("Enter a word in french")

if word_to_translate in fr_en:
  print(fr_en[word_to_translate])
else:
  print("Word doesn't exist")