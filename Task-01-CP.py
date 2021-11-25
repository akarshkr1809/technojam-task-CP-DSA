n=input("Enter the Word - (word should comprise atleast 12 characters)")

l=len(n)

first_char = n[0]

last_char = n[l-1]

if (l<12):
    print("The word is Too short to be Abbreviated")

elif (l>100):
    print("The word is Too Large")

else:
    print(first_char,l-2,last_char,sep='')


