# we use the build-in open() to open the file.
#with open ('shafi.txt' , 'r') as file: #--- this can also be one way to open the file
#file=open('shafi.txt', 'r')
#contents = file.read() #to read the file
#print(contents)

#for writing 
#file=open("shafi.txt","w")
#contents=file.write("hi shafii keep coding bro")
#print(contents)

file=open('shafi.txt', 'r+') #for reading and writing 
contents = file.read() #to read the file
print(contents)
file.write("its time to test what you have been writing through out the day")
file.seek(0)
upadate_contents=file.read()
print(upadate_contents)