class Solution(object):
    def hammingDistance(self, x, y):
        w = x ^ y
        ans = 0
        while w > 0:
            if w % 2 ==1:
                ans = ans +1
            w = w // 2
        return ans

import sys
def readlines():
    for line in sys.stdin:
        yield line.strip('\n')

def main():
    lines = readlines()
    while True:
        try:
            line = lines.next()
            x = int(line)
            line = lines.next()
            y = int(line)
            
            ret = Solution().hammingDistance(x, y)

            out = str(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()
