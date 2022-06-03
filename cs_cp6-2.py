# Question 1
print("# Question 1")
cars = ["Myvi", "Axia", "Bezza"]
print(cars)
cars.remove("Axia")
cars.append("X50")
print(cars)
print() # Pretty printing

# Question 2
print("# Question 2")
marks = [88, 67, 90, 55, 60]
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)
print() # Pretty printing

# Question 3
print("# Question 3")
participants = ['A', 'B', 'C']
print(f"""{participants}
Action 1: Append a new participant
Action 2: Remove an existing participant""")
decision = input("Choose an action to perform: ")
if decision == '1':
    participants.append(input("Participant name to be appended: "))
elif decision == '2':
    participants.remove(input("Participant name to be removed: "))
else:
    print("Invalid action. ")
print(f"Current participants: {participants}")
print() # Pretty printing

# Question 4
print("# Question 4")
lyrics = list("hello hello can you hear me as I scream your name hello hello do you need me before I fade away Is this a place that I call home to find what I've become walk along the path unknown we live we love we lie deep in the dark I don't need the light there's a ghost inside me It all belongs to the other side we live we love we lie hello hello nice to meet you voice inside my head hello hello I believe you how can I forget")
VALID_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "
for idx, char in enumerate(lyrics):
    if char not in VALID_CHARS:
        lyrics.pop(idx)
lyrics = ''.join(lyrics)
print(f"Lyrics without punctuation: \n{lyrics}\n")
words = lyrics.split(' ')
print(f"Words in the lyrics: \n{words}\n")
print("There are {} words in the lyrics. \n".format(len(words)))
query = input("Word to be counted: ")
print("The word \"{}\" occured {} times in the lyrics. ".format(query, lyrics.count(query)))
print() # Pretty printing

# Question 5
print("# Question 5")
student_marks = [[65, 99],
                 [44, 30],
                 [89, 70],
                 [70, 66]]
seat_to_name = {
    0: 'A',
    1: 'B',
    2: 'C',
    3: 'D',
}
sjctr_to_subject = {
    0: "Electrical",
    1: "Computer Science",
}
for seat, mark in enumerate(student_marks):
    print("Total mark of student {}: {}".format(seat_to_name[seat], sum(mark)))
for sjctr in range(len(student_marks[0])):
    tmp = 0
    for i in student_marks:
        tmp += i[sjctr]
    print("Average mark of {}: {}".format(sjctr_to_subject[sjctr], tmp / len(student_marks)))
print() # Pretty printing

# Question 6
print("# Question 6")
files = ["d1.jpg", "d2.png", "d3.gif", "d4.gif", "d5.jpg", "d6.png"]
jpg = []
png = []
gif = []
for i in files:
    if i.endswith(".jpg"):
        jpg.append(i)
    elif i.endswith(".png"):
        png.append(i)
    elif i.endswith(".gif"):
        gif.append(i)
    else:
        print(f"{i} has an unrecognized file extension type")
print(f"jpg: {jpg}")
print(f"png: {png}")
print(f"gif: {gif}")
print() # Pretty printing

# Question 7
print("# Question 7")
string = input("Input a string to determine if its a HTTP/HTTPS link: ")
if string.startswith("http://") or string.startswith("https://"):
    print(f"\"{string}\" is a HTTP/HTTPS link")
else: 
    print(f"\"{string}\" is not a HTTP/HTTPS link")
print() # Pretty printing
