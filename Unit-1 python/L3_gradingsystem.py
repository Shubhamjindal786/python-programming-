# ------------ Grading System-------------

n=eval(input("Enter marks:"))

assert n>0 and n<=100
if n>=90:
    Grade="A+"
elif n>=80:
    Grade="A"
elif n>=70:
    Grade="B"
elif n>=60:
    Grade="C"
elif n>=50:
    Grade="D"
else:
    Grade="E"

print("The grading is ",Grade)

