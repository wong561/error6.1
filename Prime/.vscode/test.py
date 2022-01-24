# # msg = "Hello World"
# # print(msg)

# # def my_function(x):
# #   print(x)

# # my_function('hi')


# # // write a function that takes in two numbers return the sum of those numbers


# g = -9.8

# mG = 0.5*g
# v=100
# y0=2
# vb=300

# def freefall(v):
#     t = v / -g
#     print('t is', t)
#     if t < 0 :
#         print('Great Scott! Are you in the delorean? You just traveled back in time!:' , t)
#     else:
#         return(t)


# tYm = freefall(v)
# print('tYm is', tYm)


# def mainfunction(mG,v,tym,y0):
#     vTym = v*tYm
#     print('distance:', vTym)
#     tymsq = tym * tym
#     gt2 =mG*tymsq
#     ymax = vTym+y0+gt2

#     return(ymax)

# ymax = mainfunction(mG,v,tYm,y0)
# print('ymax is', ymax)



# # def Yt(mG,v,t,y0)
# # #  def zeroG(ymax):
     


# def timeToGround(y0,ymax,decimal):

#     result = (y0+ymax)/-mG
#     roundedResult = round(result, decimal)
#     if result < 0 :
#         return 'error:' , result
#     else:
#         return result




# shift = timeToGround(y0,ymax,3)
# print('shift returns the number', shift)


# def Bullet(vb,shift):
#     x1=vb*shift
#     return(x1)

# print('Bullet', Bullet(vb,shift))

# names = ['megan', 'simon', 'steves', 'willy', 'freckles']
# def sayHello(name):
#     i = 0
#     length = len(name)
#     print('hello, ')
#     while i < length-1:
#         print(name[i])
#         i = i+1
#     print('and', names[-1],'!')


# sayHello(names)

promptText = input("What is your name?: ")
print("Hi", promptText, 'Nice to meet you!')
