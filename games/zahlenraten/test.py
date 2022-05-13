# Test for saving Highscores in a file

ui = input("Enter your name: ")
score = int(input("Enter your score: "))

#filew = open("highscores.txt", "a")
#filew.write(ui + "|" + str(score) + "\n")
#filew.close()

filer = open("highscores.txt", "r")
lines = filer.read().splitlines()
names = []
scores = []

#splits the file into two lists
for i in lines:
    names.append(i.split("|")[0])  # split the line into a list
    scores.append(int(i.split("|")[1]))
filer.close()

scores, names = zip(*sorted(zip(scores, names), reverse=True))  # sort the list

#convert tuple to list
names = list(names)
scores = list(scores)

print("names")
print(names)
print("scores")
print(scores)
print(" ")

for x in range(len(names)):
    if(score > int(scores[x])):
        names.insert(x, ui)
        scores.insert(x, score)
        break

#formats the scoreboard
for x in range(len(names)):
    if x == 5:
        break
    print(str(x+1) + ". " + names[x] + ": " + str(scores[x]))

#write the scoreboard to the file
filew = open("highscores.txt", "w")
for x in range(len(names)):
    if x == 5:
        break
    filew.write(names[x] + "|" + str(scores[x]) + "\n")
filew.close()