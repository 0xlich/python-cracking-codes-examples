# Reverse cipher

# message = "This is a demostration of the reverse cipher in action!."
# message = ".!noitca ni rehpic esrever eht fo noitartsomed a si sihT"
print("Please input the string you want to cipher: ")
message = input()
translated = ''

i = len(message) - 1
while i >= 0:
        translated = translated + message[i]
        # i--
        i = i - 1

print (translated)
