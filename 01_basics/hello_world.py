# Python is an interpreted language because it iterprete codes line by line but it's code gets compiled to byte code also known as low-leve code which is platform independent
# The .pyc file is basically compiled python also known as Frozen-Binaries which only comes for imported file and never for top files
# Python's run time engine known as PVM or python interpreter is responsible for executing the code
# Byte code is not Machine code because it does not gives instruction to the hardware like machine code
# from importlib import reload -> To relod from terminal without having to import the file again after making a change in that file

print("Hello")   

def speak(n):
    print(n)
    
speak("Hello World")

# Mutables: List, Array, Set, ByteArray, Dictionary
# Immutables: Integer, Float, Boolean, String, Byte, Frozen Set

# Because everyting in Python is an Object, so everthing stored in the memory is in the form of an object
# Once an immutable object is created, its value cannot be modified.
# eg, x=5 (this means in memory x is pointing to 5)
# eg, x=10 (this creates a new integer object with the value 10, & that means in memory now x is pointing to 10. However 5 is still in the memory and remains unchained(Immutated). 5 continues to live in the memory as long as something is pointing at it if that's not the case then it gets garbage colleted and gets deleted from the memory but is never changed)

#  x = 1 
#  y = x (Here both x and y are pointing at 1 in the memory)
#  x = 2 (Now, x is pointing at 2 but y is still pointing at 1)
# (this does not mean x being an interger is immutable & still its' value got changed, it just started to point on another immutable Object i.e 2, the  immutable Object 1 was never changed, it can only be deleted by garbage collector when nothing points to it )
# Memory me 1 baar agr immutable object ban gaya, ab aap usse change nhi kr skte, haa jo variable uss immutable object ko point krra h woh immutable nhi h, usme aap dusri value rakh skte h, fir jo dusra object create ho memory me, woh variable uss new object ko point krne lagega, Phele wala immutable object change nhi hoga.