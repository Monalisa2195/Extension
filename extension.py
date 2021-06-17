name = input("Enter the file name: ")
a = name.split(".")
ext=a[1]
if  ext=='py':
 print("The extension of the file is python")
elif ext=='js':
 print("The extension of the file is Javascript")
elif ext=='cpp':
 print("The extension of the file is C++")
elif ext=='java':
  print("The extension of the file is Java")
elif ext=='c':
 print("The extension of the file is C")
else :
 print("Unidentified extension")
