import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if a valid common divisor string is possible
        if str1 + str2 != str2 + str1:
            return ""

        # Check string length less than 1
        if len(str1) < 1 or len(str2) < 1:
            print("Break: str1.length or str2.length < 1")
            return ""

        # Check string length more than 100
        if len(str1) > 100 or len(str2) > 100:
            print("Break: str1.length or str2.length > 100")
            return ""

        # Check string length more than 100
        if not str1.isupper or not str2.isupper:
            print("Break: str1 or str2 is not upper letter")
            return ""

        if not str1.isalpha or not str2.isalpha:
            print("Break: str1 or str2 is not alpha")
            return ""
        
        # Get the length of the greatest common divisor string
        gcd_len = math.gcd(len(str1), len(str2))
        #print("gcd_len = ", gcd_len)

        # The answer is the prefix of length gcd_len
        return str1[:gcd_len]


# manual test

if __name__ == "__main__":
    sol = Solution()
    print(sol.gcdOfStrings("ABCABC", "ABC"))
    print(sol.gcdOfStrings("ABABAB", "AB"))
    print(sol.gcdOfStrings("TYU", "ABC"))
    print(sol.gcdOfStrings("AAAAAB", "AAA"))
    print(sol.gcdOfStrings("", "ABC"))
    print(sol.gcdOfStrings("132", "ABC"))
    print(sol.gcdOfStrings("abcabc", "ABC"))