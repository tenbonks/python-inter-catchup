import requests

while True:

    # get the request
    response = requests.get("https://yesno.wtf/api")
    res_answer = response.json()["answer"]
    print("- - - - - - - - - -\n\
 - - Yes Or No? - -\n\nANSWER: " + res_answer.upper())

    while True:
        answer = str(input('Run again? (y/n): '))
        if answer in ('y', 'n'):
            break
        print("invalid input.")
    if answer == 'y':
        print("-_-_-_-_-_-_-_-_-_-")
        continue
    else:
        print("Goodbye")
        break
