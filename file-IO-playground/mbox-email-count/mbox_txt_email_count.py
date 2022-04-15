emails = []

fhand = open("mbox.txt")
for line in fhand:
    line.rstrip()
    if line.startswith("From"):
        line = line.split(' ')
        line1 = line[1].strip('\n')
        emails.append(line1)
print('Emails in mbox.txt -> :')
print(emails)

email_count = {}
for word in emails:
    email_count[word] = email_count.get(word, 0) + 1

print(" ")
print("Counting emails")
print(email_count)

sorted_email_count = dict(sorted(email_count.items(), key=lambda item: item[1], reverse=True))
print(" ")
print('Sorted email count in descending order')
print(sorted_email_count)

fhand.close()
