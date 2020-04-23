import re
import string

patterns = [
    (r"\b(hi)\b", "Hello"),

    (r"\b(i'm|i am)\b", "YOU ARE"),
    (r"\b(i|me)\b", "YOU"),
    (r"\b(my)\b", "YOUR"),

    (r"\b(yes)\b", "HAPPY TO HEAR THAT"),
    (r"\b(no)\b", "SORRY.."),
    (r"\b(may be| maybe)\b", "YES, IT IS BETTER"),

    (r"\b(what) .* (name)\b", "I AM ELIZA"),
    (r"\b(what) .* ^(name)\b", "SORRY, I HAVE NO IDEA"),

    (r"\b(think|know) .* (love)\b", "IT IS BEAUTIFUL"),
    (r"\b(think|know) .* ^(love)\b", "SORRY, I AM NOT AN EXPERT"),

    (r"\b(you) .* (beautiful|pretty|lovely)\b", "THANK YOU VERY MUCH"),
    (r"\b.* (beautiful|pretty|lovely)\b", "THANK YOU"),
    (r"\b(sad)\b", "SAD ,I FEEL THE SAME"),

    (r".* all .*", "IN WHAT WAY"),
    (r".* always .* love", "LOVES"),
    (r"[%s]" % re.escape(string.punctuation), ""),
    ]

print("Welcome to ELIZA-IN-LOVE")
print("Hi, I am Eliza")

while True:
    comment = input()
    response = comment.lower()
    for match, replace in patterns:
        response = re.sub(match, replace, response)

    print(response.upper())

