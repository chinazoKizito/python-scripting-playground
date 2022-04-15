print("Enter a Line of text")
inputer = input('')

# Read a text file or a sentence
if inputer.endswith('.txt'):
    fhandle = open(inputer)
    for line in fhandle:
        line = line.rstrip()
        words = line.split()
else:
    words = inputer.split()


print("Words:", words)

print("counting words")
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
print(counts)

high = []
for k, v in counts.items():
    high.append((v, k))
high.sort()
high.reverse()
print("First Ten Occurring words: ", high[:10])
