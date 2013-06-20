import sys

class palindromes:
    """Builds a catalog of all palindromic "substrings" given an indexable object
    
    Note that indexable file objects could be used for very large data
    Also one might use this for more than just character strings
    Basically anything that is an indexable sequence of units that are comparable

    Cataloging approach motivated by:
    1: the whole string could be a palindrome
    2: all the palindromes have a 2 or 3 length seed palindrome and expand on that
    ...lead me to suspect scanning for those and expanding is a good approach

    I make no claim this is the best approach in any way!

    Potential improvements:
    1: only store indicies
    2: use dict ( palindrome, [locations] )
    
    It was fun to think about and code, maybe others will find it useful.
    Stranger things have been know to happen!

    This code written by Joseph P. Silva and is in the public domain
    per The GNU General Public License version 2 (GPLv2)
    """
    s = None
    smallest = []
    larger = []
    maxLength = 0

    def maxCheck(self,length):
        if length > self.maxLength:
            self.maxLength = length


    def foundSmall(self,index,pali):
        self.smallest.append([index,pali])
        self.maxCheck(len(pali))

    def foundLarger(self,index,pali):
        self.larger.append([index,pali])
        self.maxCheck(len(pali))

    def expand(self,x):
        s = self.s
        first = x[0] - 1
        last = x[0] + len(x[1])
        # until we expand past ends of our input string
        # or the expanded substring is not a plaindrome
        # we found a larger palindrome
        while (first >= 0) and (last < len(s)) and (s[first]==s[last]):
            newPali = s[first:last+1]
            self.foundLarger(first,newPali)
            first -= 1
            last += 1

    def __init__(self,s):
        self.s = s
        
        # first we find all the 2 and 3 length palindromes
        # then we check if any of them are part of larger palindromes
        
        # no sting or empty string or length 1 string have nothing and we are done
        if (not s) or (len(s)<2):
            return
        
        # check the first length 2 because next checks are
        # for all length 2 and 3 that end at same position
        if s[0]==s[1]:
           self.foundSmall(0,s[0:2])
        
        # from start to end check all the length 2 and 3 subseqs
        # which end at same position
        i=0
        lastIndex = len(s) - 3
        while i<= lastIndex:
            if s[i] == s[i+2]:
                self.foundSmall(i,s[i:i+3])
            if s[i+1]==s[i+2]:
                self.foundSmall(i+1,s[i+1:i+3])
            i += 1

        # check if any are center of larger palindromes
        for x in self.smallest:
            self.expand(x)

    def printLargest(self):
        largest = self.smallest
        if len(self.larger)>0:
            largest = self.larger
        if len(largest)>0:
            print "Largest palindromes"
        for x in largest:
            if len(x[1])==self.maxLength:
                print x[0],x[1]
            

def main():
 s = sys.stdin.read()
 palies = palindromes(s)
 palies.printLargest()

if __name__ == "__main__":
    main()

