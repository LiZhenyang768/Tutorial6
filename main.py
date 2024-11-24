from calendar import firstweekday

print("### f(x)=-x^2+3x-2 from a=1 to b=2 ###")
def f(x):
    y=-x**2+3*x-2
    return y

h=0.1
x1=1
x2=2
x=x1+0.1
while x1<=x2+0.000001:
    print("When x =",x1,"=> f(x)=",f(x1))
    x1+=h

print("### Example of Trapezium Rule Values ###")
first=f(1)
last=f(2)
print("First Height:",first)
print("Last Height:",last)

sum=0
while x<x2:
    sum += f(x)
    x+=h
print("Middle Sum:", sum)

i=(first+last+sum*2)*(h/2)
print("𝑰𝒏𝒕𝒆𝒈𝒓𝒂𝒕𝒊𝒐𝒏 𝒊𝒔 𝒂𝒑𝒑𝒓𝒐𝒙𝒊𝒎𝒂𝒕𝒆𝒍𝒚 =",i)
print("Ture value of integration is 1/6")
e=(1/6-i)/(1/6)*100
print("Therefore the error is ",e,"%")