'''
What is the maximum 16-digit string for a "magic" 5-gon ring?

Full description with pictures at http://projecteuler.net/index.php?section=problems&id=68

Created on Feb 28, 2011

@author: Greg Charles
'''
import itertools
import poly

# Convenience method to compute sum of triples based on values at vertices of polygon
def computeTriplesSum(innerList):
    sides = len(innerList)
    totalSum = poly.triangle(2*sides)
    innerSum = sum(innerList)
    triplesSum = totalSum + innerSum
    return sides, triplesSum

# The sum of the five triples must be an even multiple of the number of sides.
# Otherwise it can't be a magic n-gon.
def isPossibleMagic(innerList):
    sides, triplesSum = computeTriplesSum(innerList)
    return triplesSum % sides == 0

# Make a magic n-gon if possible. Return false and an empty list if not possible.
def makeMagic(innerList):
    sides, triplesSum = computeTriplesSum(innerList)
    target = triplesSum / sides

    available = [True]*(2 * sides + 1)
    for x in innerList:
        available[x] = False

    triples = []
    for i in range(sides):
        x,y = innerList[i], innerList[(i+1)%sides]
        magic = target - x - y
        if magic < 1 or magic > (2 * sides) or not available[magic]:
            return False, []

        available[magic] = False
        triples.append([magic,x,y])

    return True, triples

# Rotate the triples list so the triple with the minimum outer value is first.
def rotate(triples):
    length = len(triples)
    minOuter, minIndex = triples[0][0], 0
    for i in range(length):
        if triples[i][0] < minOuter:
            minOuter, minIndex = triples[i][0], i

    newTriples = []
    for i in range(length):
        newTriples.append(triples[(minIndex + i) % length])

    return newTriples

# Convert the triples list to an integer.
def convert(triples):
    return int(''.join(map(str,[item for sub in triples for item in sub])))

# Finds the answer among available magic n-gons. In this case it's the one with
# the highest value without going over 16 digits.
def findAnswer(possibles):
    max = 0
    for magicList in possibles:
        value = convert(magicList)
        if value > max and value < 10 ** 16:
            max = value

    return max

# Main program
sides = 5
possibles = []
numberList = range(1, 2*sides+1)
maxValue = 0

# From the possible digits, pick all possible combinations for the vertices.
for innerList in itertools.combinations(numberList,sides):
    if isPossibleMagic(innerList):
        # For possible vertexes, try all possible permutations (taking into account rotational symmetry).
        for perm in itertools.permutations(innerList[0:-1]):
            newInnerList = list(perm)
            newInnerList.append(innerList[-1])
            valid, magicList = makeMagic(newInnerList)
            if valid:
                magicList = rotate(magicList)
                possibles.append(magicList)
                print magicList

print 'Answer is ', findAnswer(possibles)
