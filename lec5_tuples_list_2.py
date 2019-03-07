def q_and_rem (x,y):
    q = x//y
    r = x % y
    p = x / y
    return[q,r,p]

# (quot, remdr, asd) = 
a=q_and_rem(10,3)
# print(tuple(a),type(a))


def get_data(aTuple):#aTuple=((int,string),(int,string))
    #int into num
    #string into words
    """
    aTuple, tuple of tuples (int, string)
    Extracts all integers from aTuple and sets them as elements in a new tuple.
    Extracts all unique strings from from aTuple and sets them as elements in a new tuple.
    Returns a tuple of the minimum integer, the
    maximum integer, and the number of unique strings
    """
    num=()
    words=()
    for t in aTuple:
        num=num+(t[0],)
        if t[1] not in words:
            words=words+(t[1],)

    min_n=min(num)
    max_n=max(num)
    unique_words=len(words)
    return(min_n, max_n, unique_words)


#############
##min year, max year, total no of unique people
#############

def matching(aTuple):
    num = ()
    words = ()
    for t in aTuple:
        # print(t)
        # print(t[1])
        # print(t[0])
        num = num + (t[0],)
        # print('th num value is',num)
        if t[1] not in words:
            words = words + (t[1],)
            # print(words)
    min_n = min(num)
    # print('the min_n is',min_n)
    max_n = max(num)
    u_words = len(words)    # unique_words
    # print('no of totall people work with singer',u_words)
    return (min_n, max_n, u_words)

test=((2014,"Katy"),(2014, "Harry"),(2012,"Jake"),
        (2010,"Taylor"),(2014,"Joe"),(1993,'Harry'))

(min_year, max_year, num_people)=matching(test)
# print('from year', min_year,'to', max_year,'and the people count is',num_people)



############
##some operations on tupels
############

# p=((2014,"Katy"),(2014, "Harry"),(2012,"Jake"),(2010,"Taylor"),(2008,"Joe"))
# for d in p:
#     # print(d,type(d))
#     a=len(d[1])
#     # print(a)
#     if a==6 :
#         print(d)



############
##sort
### object_name.sort, sorted(object_name)
############

cool=['red','yellow','green']
cool=[1,2,5,89,3,2,6]
new=cool.sort()
# print(cool)
# print(new)
cool=[7,9,4,1,7,0,2]
new1=sorted(cool)
cool.sort()
# print(new1)
# print(cool)


###########
##list of list
###nested list
###########
warm=['yellow','orange']
hot=['red']
brcl=[warm]
# print(brcl)
brcl.append(hot)
# print(brcl)
hot.append('pink')
# print(hot)
# print(brcl)


############
##tis is wrong method to remove duplicate elements from list
###the correct one is below that
############
def remove_dups(l1,l2):
     for e in l1:
         print('for loop',e)
         if e in l2:
             print('if loop',e)
             l1.remove(e)

l1=[1,5,3,4]
l2=[1,2,5,6]
new=remove_dups(l1,l2)
print(new)
print('l1 is',l1)
print('l2 is',l2)

############
##to remove duplicate elements from list    
############

def remove_dups(l1,l2):
    l1_copy=l1[:]
    for e in l1_copy:
        if e in l2:
            l1.remove(e)
l1=[1,2,3,4]
l2=[1,2,5,6]
remove_dups(l1,l2)
print(l1)
print(l2)

