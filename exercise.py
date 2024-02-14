sentence_length = 4
sentences = []
for i in range(4):
    sentence = input("Enter you sentence").lower()
    sentences.append(sentence)
    print(sentence)

character_counts = {}
for sentence in sentences:
    for character in sentence:
        # character_counts[character] = character_counts.get(character, 0) + 1
        # print(character_counts)

        if character in character_counts.keys():
            character_counts[character] += 1
        else:
            character_counts[character] = 1

print(character_counts)
