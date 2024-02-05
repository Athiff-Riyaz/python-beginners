#string formatting
nums=[4,5,6]
msg="Numbers:{0} {1}" .format(nums[0],nums[1])
print(msg)
print("{0}{1}{0}".format("abra","cad"))
a="{x},{y}".format(x=5,y=12)
print(a)
#function are in action
#some other functions
print(",".join(["spam","eggs","ham"]))
print("hello me".replace("me", "world"))
print("this is a sentence.".startswith("this"))
print("this is a sentence.".endswith("sentence."))
print("this is a sentence".upper())
print("AN ALL CAPS".lower())