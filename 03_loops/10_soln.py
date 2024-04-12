import time

def typeStr():
    waitTime = 1
    retries = 0

    while retries < 5:
        inputStr = input("Enter Yahoo")
        if inputStr == "Yahoo":
            print("Correct input received!")
            break
        else:
            print("Incorrect input. Retrying in", waitTime, "second(s)...")
            time.sleep(waitTime)
            waitTime *= 2
            retries += 1
    else:
        print("Maximum retries reached. Exiting...")

typeStr()