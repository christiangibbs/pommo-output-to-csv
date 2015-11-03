import sys

with open(sys.argv[1], "r") as word_list:
    words = word_list.read().split(' ')

print "Total number of emails parsed:", len(words)

f = open('output.csv', "a")
for word in words:
    f.write(word)
    f.write("\n")
