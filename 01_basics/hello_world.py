# Python is an interpreted language because it iterprete codes line by line but it's code gets compiled to byte code also known as low-leve code which is platform independent
# The .pyc file is basically compiled python also known as Frozen-Binaries which only comes for imported file and never for top files
# Python's run time engine known as PVM or python interpreter is responsible for executing the code
# Byte code is not Machine code because it does not gives instruction to the hardware like machine code
# from importlib import reload -> To relod from terminal without having to import the file again after making a change in that file

# a=3
# - memory me immutable obj create hua as 3
# - a ke andr 3 ka reference aaya
# Also, Value ka datatype hamesha memery me rehta h value ke saath, variable me kbhi nhi jaat h
# mtln aap varible ko kabhi datatype assign nhi krte par memory me jo value store hoti h as a reference to that variable usse datatype assign hota h aur yeh datatype memory me hi rehta h apni value ke saath, varaible se datatype ka koi lena dena nhi h

print("Hello")   

def speak(n):
    print(n)
    
speak("Hello World")

# Mutables: List, Array, Set, ByteArray, Dictionary
# Immutables: Integer, Float, Boolean, String, Tuple, Byte, Frozen Set

# Because everyting in Python is an Object, so everthing stored in the memory is in the form of an object
# Once an immutable object is created, its value cannot be modified.
# eg, x=5 (this means in memory x is pointing to 5)
# eg, x=10 (this creates a new integer object with the value 10, & that means in memory now x is pointing to 10. However 5 is still in the memory and remains unchained(Immutated). 5 continues to live in the memory as long as something is pointing at it if that's not the case then it gets garbage colleted and gets deleted from the memory but is never changed)
# Ab hame pata h ki, agr memory me stored value ko bahar se koi point nhi krra toh garbage collector aaega aur uss value ko delete krdega, aur esa hi hota h par 1 exception h ki NUMBERS AUR STRINGS ke cases me yeh garbage collection immediately nhi hota, forcefully karwa skte ho, pr immediately nhi hota. (Kyun ke maybe same number ka refrence program ko next step me chahiye ho...``)

#  x = 1 
#  y = x (Here both x and y are pointing at 1 in the memory)
#  x = 2 (Now, x is pointing at 2 but y is still pointing at 1)
# (this does not mean x being an interger is immutable & still its' value got changed, it just started to point on another immutable Object i.e 2, the  immutable Object 1 was never changed, it can only be deleted by garbage collector when nothing points to it )
# Memory me 1 baar agr immutable object ban gaya, ab aap usse change nhi kr skte, haa jo variable uss immutable object ko point krra h woh immutable nhi h, usme aap dusri value rakh skte h, fir jo dusra object create ho memory me, woh variable uss new object ko point krne lagega, Phele wala immutable object change nhi hoga.

# So, each object in the memory can be refrenced by multiple variables. Also, we can get the count of how many variables are referring a specific object, the count is known as referenceCount/refCount. But sys.getrefcount() gives the same count for every string or integer
# sys.getrefcount("Uzair") -> 4294967295
# sys.getrefcount("U") -> 4294967295

# Immutable eg:
# x=1, y=1 (Because Interger are immutable, both x & y are pointing at the same reference of value 1)
# x=1, y=x (Because Interger are immutable, both x & y are pointing at the same reference of value 1)

# Mutable eg:
# x=[1,2,3], y=[1,2,3] (Because list are mutable, both x & y are pointing at the differenct reference of value [1,2,3] & [1,2,3] created in the memory)
# x=[1,2,3], y=x (Here both x & y are pointing at the same reference of value [1,2,3])


