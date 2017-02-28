'''
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic 
permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

Created on Oct 2, 2010

@author: Greg Charles
'''
class Permutation(object):
  
    def __init__(self, elements):
        self.elements = elements
        self.length = len(elements)
        self.factorials = self.factorialList(self.length-1)
 
    def factorialList(self, n):
        list = [1] 
        for i in range(2,n+1):
            list.append(i * list[-1])
            
        return list

    def getPosition(self, position):
        myelements = self.elements[:]
        remainder = position - 1
        answer = []

        for x in range(1, self.length):
            nextIndex = remainder / self.factorials[-x]
            answer.append(myelements.pop(nextIndex))
            remainder -=  (nextIndex * self.factorials[-x])

        answer.append(myelements[0])
        return answer

p = Permutation(range(0,10))
print ''.join(map(str, p.getPosition(1000000)))

