mystry = 'hello'
mystry2 = 'world'
mystry = mystry+' '+mystry2
print(mystry)

#functions
def MySum(a,b):
    return(a+b)
a=1
b=2
MySum(a,b)

#list
mylist = ['a','b','c',1,2,3]

def getBondPrice(y, face, couponRate, m, ppy=1):
    pvcfsum = 0
    cf = couponRate * face
    for t in range (1, m+1):
        pv = (1+y)**(-t)
        pvcf = pv*cf
        pvcfsum =+ pvcf
        print(pvcfsum)
    bondprice = pvcfsum + pv*face
    return(bondprice)