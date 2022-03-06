x = int(input("Enter a length of a Triangle side: "))
y = int(input("Enter a length of a Triangle side: "))
z = int(input("Enter a length of a Triangle side: "))

s1 = (y * y) + (z * z)
s2 = (x * x) + (z * z)
s3 = (x * x) + (y * y)

if s3 <= (x * x) + (y * y):
	print("The triangle is a right trianlge")
else:
	print("The triangle is not a right triangle")
