text = input("Enter your Text:")

print("\nText Received Successfully!")
print(f"Text : {text}")

character_count = len(text)
print(f"Total Character : {character_count}")

words = text.split()
words_count =len(words)
print(f"Total Words : {words_count}")