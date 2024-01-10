#lambda
#result = (lambda x=10,y=20: x+y)(y=50)
#print(result)

#map
#number = [1,2,3,4,5]

#def square(x):
#    return x*x

#new_list = list(map(square,number))
#print(new_list)


#filter
#numbers = [1,2,3,4,5,6,7,8,9,10]

#odd_numbers = list(filter(lambda x: x%2==1,numbers))
#print(odd_numbers)

#generators
def even_generator(x):
    for i in range(x):
        if i%2==0:
            yield i
print(list(even_generator(11)))


