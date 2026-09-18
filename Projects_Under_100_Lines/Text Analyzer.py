text = input("Enter your Text:")

print("\nText Received Successfully!")
print(f"Text : {text}")

character_count = len(text)
print(f"Total Character : {character_count}")

words = text.split()
words_count =len(words)
print(f"Total Words : {words_count}")


vowels = "aeiou"
vowel_count = 0

for char in text.lower():
    
    if char in vowels:
        vowel_count += 1
        
print(f"Total Vowels : {vowel_count}")


word_frequency = {}

for word in words:
    word = word.lower()
    
    if word in word_frequency:
        word_frequency[word] += 1
         
    else:
        word_frequency[word] = 1
        
print("\n =====WORD FREQUENCY=====")

for word, count in word_frequency.items():
    print(f"{word} : {count}")
        