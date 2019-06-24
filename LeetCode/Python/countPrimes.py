class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        prime = [True for x in range(n)]
        primeCount = 0

        for i in range(2, n):
            if prime[i] == True:
                primeCount += 1
                current = i
                while current < n:
                    prime[current] = False
                    current += i
        
        return primeCount
                    


